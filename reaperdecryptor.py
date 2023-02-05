#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file=="reaper.py" or file == "key.key" or file== "reaperdecryptor.py" or "FILESENCRYPTED.txt":
		continue
	if os.path.isfile(file):
		files.append(file)

print (files)

with open ("key.key", "rb") as key:
	secretkey = key.read()


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted  = Fernet(secretkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)

print ("Files Decrypted!")

os.remove( "key.key")

