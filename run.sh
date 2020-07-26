#!/bin/bash

set -e

gunicorn -b 0.0.0.0:80 app:app