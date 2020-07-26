#!/bin/bash

set -e
echo "Prepares the FM transmitter..."

# Update submodules
git submodule update --init --recursive

echo "Installing dependencies"
sudo apt install -y gunicorn3 ffmpeg python3-pip
sudo pip3 install flask

cd fm_transmitter
make
cd ..

echo "All set up. Start the app via ./run.sh"