# Imports
import subprocess
import os

# search function
search = input("Web search: ")

# search.lower() conditions

if search.lower() == "nothing":
    os.system("browsh")

elif search.lower() == "":
    os.system("browsh")

# Weed
if search.lower() == "weed":
    os.system("browsh https://psychonautwiki.org/wiki/Weed")
    print("Finished searching about weed!")

# Meth
elif search.lower() == "meth":
    os.system("browsh https://psychonautwiki.org/wiki/Meth")
    print("Finished searching for meth!")

# Shrooms
elif search.lower() == "shrooms":
    os.system("browsh https://psychonautwiki.org/wiki/Shrooms")
    print("Finished searching for shrooms!")

# Dxm
elif search.lower() == "dxm":
    os.system("browsh https://psychonautwiki.org/wiki/Dxm")
    print("Finished searching for DXM!")

# Alcohol
elif search.lower() == "alc":
    os.system("browsh https://psychonautwiki.org/wiki/Alcohol")
    print("Finished searching for alcohol! Bleh!")

# LSD
elif search.lower() == "lsd":
    os.system("browsh https://psychonautwiki.org/wiki/LSD")
    print("Finished searching for LSD! Hold on to that burrito!")

# mdma
elif search.lower() == "mdma":
    os.system("browsh https://psychonautwiki.org/wiki/MDMA")
    print("Finished searching for MDMA!")

# fentanyl
elif search.lower() == "fentanyl":
    os.system("browsh https://psychonautwiki.org/wiki/Fentanyl")
    print("Finished searching for fentanyl! Slow down, rockstar!")

# Coke
elif search.lower() == "coke":
    os.system("browsh https://psychonautwiki.org/wiki/Cocaine")
    print("Finished searching for cocaine!")

# Speed
elif search.lower() == "speed":
    os.system("browsh https://psychonautwiki.org/wiki/Speed")
    print("Finished searching for speed!")

# peyote
elif search.lower() == "peyote":
    os.system("browsh https://drugs.tripsit.me/peyote")
    print("Finished searching for peyote (tripsit)!")

# ambien
elif search.lower() == "ambien":
    os.system("browsh https://psychonautwiki.org/wiki/Ambien")
    print("Finished searching for ambien!")

# salvia
elif search.lower() == "salvia":
    os.system("browsh https://psychonautwiki.org/wiki/Salvia")
    print("Finished searching for salvia!")

# xans
elif search.lower() == "xanax":
    os.system("browsh https://psychonautwiki.org/wiki/Xanax")
    print("Finished searching for xanax!")

# dph
elif search.lower() == "dph":
    os.system("browsh https://psychonautwiki.org/wiki/Dph")
    print("Finished searching for DPH, you fucking idiot!")

# exit software
elif search.lower() == "exit":
	exit("Goodbye!")

os.system('python ~/grungegirl/query.py')
