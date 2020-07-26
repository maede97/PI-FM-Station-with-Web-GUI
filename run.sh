#!/bin/bash

set -e

sudo gunicorn3 -b 0.0.0.0:80 app:app