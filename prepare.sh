#!/bin/bash

set -e
echo "Prepares the FM transmitter..."

# Update submodules
git submodule update --init --recursive

echo "Installing dependencies"
sudo apt install -y gunicorn3 python3-pip sox libsox-fmt-all
sudo pip3 install flask

cd fm_transmitter
make
cd ..

# Create upload directory for all files
mkdir -p uploads

echo "All set up. Start the app via ./run.sh"