from flask import Flask, request, redirect, flash, render_template, url_for
from werkzeug.utils import secure_filename
import threading
import os
import time
import atexit

PLAY_QUEUE = []
HERTZ = "88.2"
KILL_THREAD = False

def radio_player_func(stop):
    global PLAY_QUEUE
    global HERTZ
    global KILL_THREAD

    while True:
        print("Starting loop")
        while len(PLAY_QUEUE) == 0:
            if stop():
                return
            time.sleep(1)

        current = PLAY_QUEUE[0]
        print("Playing", current)
        os.system(f"sudo fm_transmitter/fm_transmitter -f {HERTZ} 'uploads/{current}'")
        PLAY_QUEUE = PLAY_QUEUE[1:]
        os.remove(f"uploads/{current}")

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")

ALLOWED_EXTENSIONS = {'mp3','wav', "m4a"}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # max 16Mb

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY', 'dev')

THREAD = threading.Thread(target=radio_player_func, args=lambda: KILL_THREAD)

THREAD.start()

def close_thread():
    global KILL_THREAD
    KILL_THREAD = True
    THREAD.join()

atexit.register(close_thread)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/converting", methods=["GET"])
def checking_file():
    global PLAY_QUEUE
    filename = request.args.get("filename")
    if filename == "":
        return redirect(url_for("upload_file"))
    else:
        # Extract the extension
        ext = filename.rsplit(".", 1)[1].lower()
        filename_without_ext = filename.rsplit(".", 1)[0]
        if ext == "wav":
            PLAY_QUEUE.append(filename)
            return redirect(url_for("index_page"))
        elif ext == "mp3" or ext == "m4a":
            # convert with ffmpeg
            if os.system(f"sudo sox 'uploads/{filename}' -r 22050 -c 1 -b 16 -t wav 'uploads/{filename_without_ext}.wav'") == 0:
                PLAY_QUEUE.append(f"{filename_without_ext}.wav")
                return redirect(url_for("index_page"))
            else:
                flash("An error occured")
                return redirect(url_for("upload_file"))

@app.route("/upload", methods=["GET","POST"])
def upload_file():
    if request.method == "POST":
        if 'audiofile' not in request.files:
            flash("No file part")
            return redirect(request.url)
        audiofile = request.files['audiofile']
        if audiofile.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if audiofile and allowed_file(audiofile.filename):
            filename = secure_filename(audiofile.filename)
            audiofile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('checking_file',filename=filename))

    # if not post, we show the upload form
    return render_template("upload.html")

@app.route("/")
def index_page():
    global PLAY_QUEUE
    return render_template("index.html", queue=PLAY_QUEUE)

if __name__ == "__main__":
    app.run()