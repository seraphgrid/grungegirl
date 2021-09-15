# Imports
import subprocess
import os

# Search function
search = input("Web Search: ")

# Search conditions

if search == "nothing":
    os.system("browsh")

# Weed
if search == "weed":
    os.system("browsh https://psychonautwiki.org/wiki/Weed")
    print("Finished searching about weed!")

# Meth
elif search == "meth":
    os.system("browsh https://psychonautwiki.org/wiki/Meth")
    print("Finished searching for meth!")

# Shrooms
elif search == "shrooms":
    os.system("browsh https://psychonautwiki.org/wiki/Shrooms")
    print("Finished searching for shrooms!")

# Dxm
elif search == "dxm":
    os.system("browsh https://psychonautwiki.org/wiki/Dxm")
    print("Finished searching for DXM!")

# Alcohol
elif search == "alc":
    os.system("browsh https://psychonautwiki.org/wiki/Alcohol")
    print("Finished searching for alcohol! Bleh!")

# LSD
elif search == "lsd":
    os.system("browsh https://psychonautwiki.org/wiki/LSD")
    print("Finished searching for LSD! Hold on to that burrito!")

# mdma
elif search == "mdma":
    os.system("browsh https://psychonautwiki.org/wiki/MDMA")
    print("Finished searching for MDMA!")

# fentanyl
elif search == "fentanyl":
    os.system("browsh https://psychonautwiki.org/wiki/Fentanyl")
    print("Finished searching for fentanyl! Slow down, rockstar!")

# Coke
elif search == "coke":
    os.system("browsh https://psychonautwiki.org/wiki/Cocaine")
    print("Finished searching for cocaine!")

# Speed
elif search == "speed":
    os.system("browsh https://psychonautwiki.org/wiki/Speed")
    print("Finished searching for speed!")

# peyote
elif search == "peyote":
    os.system("browsh https://drugs.tripsit.me/peyote")
    print("Finished searching for peyote (tripsit)!")

# ambien
elif search == "ambien":
    os.system("browsh https://psychonautwiki.org/wiki/Ambien")
    print("Finished searching for ambien!")

# salvia
elif search == "salvia":
    os.system("browsh https://psychonautwiki.org/wiki/Salvia")
    print("Finished searching for salvia!")

# xans
elif search == "xanax":
    os.system("browsh https://psychonautwiki.org/wiki/Xanax")
    print("Finished searching for xanax!")

# dph
elif search == "dph":
    os.system("browsh https://psychonautwiki.org/wiki/Dph")
    print("Finished searching for DPH, you fucking idiot!")

# exit software
elif search == "exit":
	exit("Goodbye!")

os.system('python ~/grungegirl/query.py')
