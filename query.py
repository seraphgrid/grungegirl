# Imports
import subprocess
import os
import time
import subprocess
import requests

# Foundation laid for using tor with w3m.

# search function
search = input("Web search: ")

print("tor integration coming soon lovelies. be patient or contribute! x -death <33")

# search.lower() conditions


def query():

    if search.lower() == "nothing":
        os.system(
            "w3m http://psychonautwiki.org/w/index.php?search=&title=Special%3ASearch&go=Go")

    elif search.lower() == "":
        os.system(
            "w3m http://psychonautwiki.org/w/index.php?search=&title=Special%3ASearch&go=Go")

# Weed
    if search.lower() == "weed":
        os.system("w3m http://psychonautwiki.org/wiki/Weed")
        print("Finished searching about weed!")

# Meth
    elif search.lower() == "meth":
        os.system("w3m http://psychonautwiki.org/wiki/Meth")
        print("Finished searching for meth!")

# Psychedelics

    elif search.lower() == "shrooms":
        os.system("w3m http://psychonautwiki.org/wiki/Shrooms")
        print("Finished searching for shrooms!")

    elif search.lower() == "lsd":
        os.system("w3m http://psychonautwiki.org/wiki/LSD")
        print("Finished searching for LSD! Hold on to that burrito!")

    elif search.lower() == "peyote":
        os.system("w3m http://drugs.tripsit.me/peyote")
        print("Finished searching for peyote (tripsit)!")

    elif search.lower() == "salvia":
        os.system("w3m http://psychonautwiki.org/wiki/Salvia")
        print("Finished searching for salvia!")

    elif search.lower() == '1p':
        os.system("w3m https://psychonautwiki.org/wiki/1P-LSD")
        print('Finished searching for 1P-LSD!')

# Dissociatives

    elif search.lower() == "dxm":
        os.system("w3m http://psychonautwiki.org/wiki/Dxm")
        print("Finished searching for DXM!")

    elif search.lower() == "ambien":
        os.system("w3m http://psychonautwiki.org/wiki/Ambien")
        print("Finished searching for ambien!")

    elif search.lower() == "xanax":
        os.system("w3m http://psychonautwiki.org/wiki/Xanax")
        print("Finished searching for xanax!")

# Alcohol

    elif search.lower() == "alc":
        os.system("w3m http://psychonautwiki.org/wiki/Alcohol")
        print("Finished searching for alcohol! Bleh!")

# mdma
    elif search.lower() == "mdma":
        os.system("w3m http://psychonautwiki.org/wiki/MDMA")
        print("Finished searching for MDMA!")

# fentanyl
    elif search.lower() == "fentanyl":
        os.system("w3m http://psychonautwiki.org/wiki/Fentanyl")
        print("Finished searching for fentanyl! Slow down, rockstar!")

# Coke
    elif search.lower() == "coke":
        os.system("w3m http://psychonautwiki.org/wiki/Cocaine")
        print("Finished searching for cocaine!")

# Speed
    elif search.lower() == "speed":
        os.system("w3m http://psychonautwiki.org/wiki/Speed")
        print("Finished searching for speed!")

# dph
    elif search.lower() == "dph":
        os.system("w3m http://psychonautwiki.org/wiki/Dph")
        print("Finished searching for DPH, you fucking idiot!")

# exit software
    elif search.lower() == "exit":
        exit("Goodbye!")

    elif search.lower() == "clear":
        exit("Goodbye!")


query()

os.system('python ~/grungegirl/query.py')
