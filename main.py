#!/usr/bin/env python

# Imports
import os
import sys

# version name, version tagline, drug search
print("grungegirl - 0.1 - Party Kids")
print("This one is for you, Ronald Reagan!")
drug = input("Drug: ")


# Weed

if drug == "weed":
	os.system('python weed.py')

# DXM

elif drug == "dxm":
	os.system('python dxm.py')

# Alcohol

elif drug == "alc":
	os.system('python alc.py')

# LSD

elif drug == "lsd":
	os.system('python lsd.py')

# MDMA

elif drug == "mdma":
	os.system('python mdma.py')

# Meth

elif drug == "meth":
	os.system('python meth.py')

# Fentanyl

elif drug == "fentanyl":
	os.system('python fent.py')

# Coke

elif drug == "coke":
	os.system('python coke.py')

# Speed

elif drug == "speed":
	os.system('python speed.py')

# Peyote

elif drug == "peyote":
	os.system('python pey.py')

# Ambien

elif drug == "ambien":
	os.system('python ambien.py')

# Salvia

elif drug == "salvia":
	os.system('python salvia.py')

# Xanax

elif drug == "xanax":
	os.system('python xanax.py')

# shrooms

elif drug == "shrooms":
	os.system('python shrooms.py')

# dph

elif drug == "dph":
	os.system('python dph.py')

os.system('python main.py')
