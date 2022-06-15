#!/bin/sh
# launcher.sh
# navigate to home directory, then execute python script, then back home
cd /
cd home/ssrl-pi/Desktop/LabMonitor
python3 LabEnvironmentMonitor.py
cd /
