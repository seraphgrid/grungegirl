#!/usr/bin/env python

# Imports
import os

# version name, version tagline, drug search
print("grungegirl - 0.1.3 - Party Girls")
print("Hitomi Tanaka... my god...")
drug = input("Drug: ")

if drug == "web":
	os.system('python ~/grungegirl/query.py')

# Weed

if drug == "weed":
	os.system('python ~/grungegirl/weed.py')

# DXM

elif drug == "dxm":
	os.system('python ~/grungegirl/dxm.py')

# Alcohol

elif drug == "alc":
	os.system('python ~/grungegirl/alc.py')

# LSD

elif drug == "lsd":
	os.system('python ~/grungegirl/lsd.py')

# MDMA

elif drug == "mdma":
	os.system('python ~/grungegirl/mdma.py')

# Meth

elif drug == "meth":
	os.system('python ~/grungegirl/meth.py')

# Fentanyl

elif drug == "fentanyl":
	os.system('python ~/grungegirl/fent.py')

# Coke

elif drug == "coke":
	os.system('python ~/grungegirl/coke.py')

# Speed

elif drug == "speed":
	os.system('python ~/grungegirl/speed.py')

# Peyote

elif drug == "peyote":
	os.system('python ~/grungegirl/pey.py')

# Ambien

elif drug == "ambien":
	os.system('python ~/grungegirl/ambien.py')

# Salvia

elif drug == "salvia":
	os.system('python ~/grungegirl/salvia.py')

# Xanax

elif drug == "xanax":
	os.system('python ~/grungegirl/xanax.py')

# shrooms

elif drug == "shrooms":
	os.system('python ~/grungegirl/shrooms.py')

# dph

elif drug == "dph":
	os.system('python ~/grungegirl/dph.py')

# exit software
elif drug == "exit":
	exit("Goodbye!")

os.system('python ~/grungegirl/main.py')
