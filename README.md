# Pi FM Station with GUI
 
Install [Raspberry PI OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) onto your raspberry pi.

Run `git clone https://github.com/maede97/PI-FM-Station-with-Web-GUI`.

All further setup is done by the file `prepare.sh`, so simply run `./prepare.sh` inside the directory `PI-FM-Station-with-Web-GUI`.

Now, set the secret key of the app: `export SECRET_KEY=YOUR_SECRET_KEY`

After the setup is complete, simply run `./run.sh`.

PS: Don't forget to connect a jumper wire to your raspberry PI on GPIO pin 4. (refer to the [manual](https://www.raspberrypi.org/documentation/usage/gpio/))

# Further settings
To change the frequency, run `EXPORT HERTZ=90.0 ./run.sh`.