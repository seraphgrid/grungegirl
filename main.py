# Imports
import os


# version name, version tagline, drug search
print("grungegirl - 0.2 - babygirl")
print("you're so beautiful. angels never die.")
print(" ")
print("XMR Donation Address:")
print("42VzGghQCyMN1yskNbZ4isRLQEkaNXoNZfcg3cR3EsxJQp4YCQzG4uBNZFQBj3zgQLgTQjNj1G6b8ZLv1VrSJqmCQTsVyhZ")
print(" ")
drug = input("Drug: ")

if drug.lower() == "web":
	os.system('python ~/.grungegirl/query.py')

# Weed

if drug.lower() == "weed":
	os.system('python ~/.grungegirl/drugs/weed.py')

# DXM

elif drug.lower() == "dxm":
	os.system('python ~/.grungegirl/drugs/dxm.py')

# Alcohol

elif drug.lower() == "alc":
	os.system('python ~/.grungegirl/drugs/alc.py')

# LSD

elif drug.lower() == "lsd":
	os.system('python ~/.grungegirl/drugs/lsd.py')

# MDMA

elif drug.lower() == "mdma":
	os.system('python ~/.grungegirl/drugs/mdma.py')

# Meth

elif drug.lower() == "meth":
	os.system('python ~/.grungegirl/drugs/meth.py')

# Fentanyl

elif drug.lower() == "fentanyl":
	os.system('python ~/.grungegirl/drugs/fent.py')

# Coke

elif drug.lower() == "coke":
	os.system('python ~/.grungegirl/drugs/coke.py')

# Speed

elif drug.lower() == "speed":
	os.system('python ~/.grungegirl/drugs/speed.py')

# Peyote

elif drug.lower() == "peyote":
	os.system('python ~/.grungegirl/drugs/pey.py')

# Ambien

elif drug.lower() == "ambien":
	os.system('python ~/.grungegirl/drugs/ambien.py')

# Salvia

elif drug.lower() == "salvia":
	os.system('python ~/.grungegirl/drugs/salvia.py')

# Xanax

elif drug.lower() == "xanax":
	os.system('python ~/.grungegirl/drugs/xanax.py')

# shrooms

elif drug.lower() == "shrooms":
	os.system('python ~/.grungegirl/drugs/shrooms.py')

# dph

elif drug.lower() == "dph":
	os.system('python ~/.grungegirl/drugs/dph.py')

# astrology

elif drug.lower() == "astro":
	os.system('python ~/.grungegirl/astrology.py')

# exit software
elif drug.lower() == "exit":
	exit("Goodbye!")

elif drug.lower() == "clear":
	exit("Goodbye!")

os.system('python ~/.grungegirl/main.py')
