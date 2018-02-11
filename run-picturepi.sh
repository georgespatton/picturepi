#!/bin/bash

#If run from the command line, headless, or from cron, make sure to utilize the display.
export DISPLAY=:0.0

cd /home/pi/picturepi/

su pi -c ./gather_files.py
su pi -c ./gallery.py

