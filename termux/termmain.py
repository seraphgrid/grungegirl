# Imports
import os


# version name, version tagline, drug search

print("grungegirl - 0.2 - babygirl")
print("you're so beautiful. angels never die.")
print(" ")
print("XMR Donation Address:")
print("46KrXnQKeG7JDWnRBQBRsiezxEaop2ZYC2t8LyXsbjEgLynVb8T9V6Zc9KX1jEfhozhucbGXt44SVYjWn8iyAiFf6As1RqA")
print(" ")
drug = input("grungegirl --> ")

# Web (Debbie)

if drug.lower() == "web":
	os.system('python ~/.grungegirl/termweb.py')

if drug.lower() == "debbie":
	os.system('python ~/.grungegirl/termweb.py')

if drug.lower() == "deb":
	os.system('python ~/.grungegirl/termweb.py')

if drug.lower() == 'w':
	os.system('python ~/.grungegirl/termweb.py')
# Weed

if drug.lower() == "weed":
	os.system('python ~/.grungegirl/drugs/weed.py')

# Alcohol

elif drug.lower() == "alc":
	os.system('python ~/.grungegirl/drugs/alc.py')

# MDMA

# Fentanyl

elif drug.lower() == "fentanyl":
	os.system('python ~/.grungegirl/drugs/fent.py')

# Coke

elif drug.lower() == "coke":
	os.system('python ~/.grungegirl/drugs/coke.py')

# Amphetamines
elif drug.lower() == "mdma":
	os.system('python ~/.grungegirl/drugs/amphet/mdma.py')

elif drug.lower() == "speed":
	os.system('python ~/.grungegirl/drugs/amphet/speed.py')

elif drug.lower() == "meth":
	os.system('python ~/.grungegirl/drugs/amphet/meth.py')

# Psychedelics

elif drug.lower() == "peyote":
	os.system('python ~/.grungegirl/drugs/psychedelics/pey.py')

elif drug.lower() == "salvia":
	os.system('python ~/.grungegirl/drugs/psychedelics/salvia.py')

elif drug.lower() == "lsd":
	os.system('python ~/.grungegirl/drugs/psychedelics/lsd.py')

elif drug.lower() == "shrooms":
	os.system('python ~/.grungegirl/drugs/psychedelics/shrooms.py')

elif drug.lower() == '1p':
	os.system('python ~/.grungegirl/drugs/psychedelics/1P_LSD.py')

elif drug.lower() == 'dmt':
	os.system('python ~/.grungegirl/drugs/psychedelics/dmt.py')


# Dissociatives

elif drug.lower() == "ambien":
	os.system('python ~/.grungegirl/drugs/ambien.py')

elif drug.lower() == "dxm":
	os.system('python ~/.grungegirl/drugs/dxm.py')

elif drug.lower() == "xanax":
	os.system('python ~/.grungegirl/drugs/xanax.py')

# dph

elif drug.lower() == "dph":
	os.system('python ~/.grungegirl/drugs/dph.py')

# astrology (strhckr)

elif drug.lower() == "astro":
	os.system('python ~/.grungegirl/termastro.py')

elif drug.lower() == "astrology":
	os.system('python ~/.grungegirl/termastro.py')

elif drug.lower() == "strhckr":
	os.system('python ~/.grungegirl/termastro.py')

elif drug.lower() == "starhacker":
	os.system('python ~/.grungegirl/termastro.py')

elif drug.lower() == 'str':
	os.system('python ~/.grungegirl/termastro.py')

elif drug.lower() == 'a':
	os.system('python ~/.grungegirl/termastro.py')

# exit software

elif drug.lower() == "exit":
	os.system('cd && clear')
	exit("grungegirl exiting.")

elif drug.lower() == "clear":
	os.system('cd && clear')
	exit("grungegirl exiting.")


elif drug.lower() == 'close':
	os.system('cd && clear')
	exit('grungegirl exiting.')

os.system('python ~/.grungegirl/termmain.py')
