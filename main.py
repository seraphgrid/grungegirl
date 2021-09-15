# Imports
import os

# version name, version tagline, drug search
print("grungegirl - 0.1.6 - why is fentanyl real")
print("there is no reason for fentanyl to exist")
drug = input("Drug: ")

if drug.lower() == "web":
	os.system('python ~/grungegirl/query.py')

# Weed

if drug.lower() == "weed":
	os.system('python ~/grungegirl/weed.py')

# DXM

elif drug.lower() == "dxm":
	os.system('python ~/grungegirl/dxm.py')

# Alcohol

elif drug.lower() == "alc":
	os.system('python ~/grungegirl/alc.py')

# LSD

elif drug.lower() == "lsd":
	os.system('python ~/grungegirl/lsd.py')

# MDMA

elif drug.lower() == "mdma":
	os.system('python ~/grungegirl/mdma.py')

# Meth

elif drug.lower() == "meth":
	os.system('python ~/grungegirl/meth.py')

# Fentanyl

elif drug.lower() == "fentanyl":
	os.system('python ~/grungegirl/fent.py')

# Coke

elif drug.lower() == "coke":
	os.system('python ~/grungegirl/coke.py')

# Speed

elif drug.lower() == "speed":
	os.system('python ~/grungegirl/speed.py')

# Peyote

elif drug.lower() == "peyote":
	os.system('python ~/grungegirl/pey.py')

# Ambien

elif drug.lower() == "ambien":
	os.system('python ~/grungegirl/ambien.py')

# Salvia

elif drug.lower() == "salvia":
	os.system('python ~/grungegirl/salvia.py')

# Xanax

elif drug.lower() == "xanax":
	os.system('python ~/grungegirl/xanax.py')

# shrooms

elif drug.lower() == "shrooms":
	os.system('python ~/grungegirl/shrooms.py')

# dph

elif drug.lower() == "dph":
	os.system('python ~/grungegirl/dph.py')

# exit software
elif drug.lower() == "exit":
	exit("Goodbye!")

os.system('python ~/grungegirl/main.py')
