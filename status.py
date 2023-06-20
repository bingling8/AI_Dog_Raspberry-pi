#!/usr/bin/env/python3
# File name   : status.py
# Description : status interfaces.

status_file = '/home/pi/Workspace/led_status/audio_status'

def write0():
    with open(status_file, 'w') as f:
        f.write('0')

def write1():
    with open(status_file, 'w') as f:
        f.write('1')

def write2():
    with open(status_file, 'w') as f:
        f.write('2')


if __name__ == '__main__':
    write0()

