# Pi FM Station with GUI
 
Install [Raspberry PI OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) onto your raspberry pi.

Run `git clone https://github.com/maede97/PI-FM-Station-with-Web-GUI`.

All further setup is done by the file `prepare.sh`, so simply run `./prepare.sh` inside the directory `PI-FM-Station-with-Web-GUI`.

Edit the configuration file `config.ini`.

After this, simply run `./run.sh`.

PS: Don't forget to connect a jumper wire to your raspberry PI on GPIO pin 4. (refer to the [manual](https://www.raspberrypi.org/documentation/usage/gpio/) and turn in with your radio at the frequency you set inside the configuration)