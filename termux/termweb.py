# Imports
import subprocess
import os
import time
import subprocess

# Foundation laid for using tor with lynx.

# search function
search = input("debbie --> ")

# search.lower() conditions


def query():

    if search.lower() == "nothing":
        os.system(
            "lynx http://psychonautwiki.org/")

    elif search.lower() == "":
        os.system(
            "lynx http://psychonautwiki.org/")

    elif search.lower() == "search":
        os.system('lynx http://psychonautwiki.org')

# Weed
    if search.lower() == "weed":
        os.system("lynx http://psychonautwiki.org/wiki/Weed")
        print("Finished searching about weed!")

# Amphet

    elif search.lower() == "meth":
        os.system("lynx http://psychonautwiki.org/wiki/Meth")
        print("Finished searching for meth!")

    elif search.lower() == "speed":
        os.system("lynx http://psychonautwiki.org/wiki/Speed")
        print("Finished searching for speed!")

    elif search.lower() == "mdma":
        os.system("lynx http://psychonautwiki.org/wiki/MDMA")
        print("Finished searching for MDMA!")


# Psychedelics

    elif search.lower() == "shrooms":
        os.system("lynx http://psychonautwiki.org/wiki/Shrooms")
        print("Finished searching for shrooms!")

    elif search.lower() == "lsd":
        os.system("lynx http://psychonautwiki.org/wiki/LSD")
        print("Finished searching for LSD! Hold on to that burrito!")

    elif search.lower() == "peyote":
        os.system("lynx http://drugs.tripsit.me/peyote")
        print("Finished searching for peyote (tripsit)!")

    elif search.lower() == "salvia":
        os.system("lynx http://psychonautwiki.org/wiki/Salvia")
        print("Finished searching for salvia!")

    elif search.lower() == '1p':
        os.system("lynx https://psychonautwiki.org/wiki/1P-LSD")
        print('Finished searching for 1P-LSD!')

# Dissociatives / Downers

    elif search.lower() == "dxm":
        os.system("lynx http://psychonautwiki.org/wiki/Dxm")
        print("Finished searching for DXM!")

    elif search.lower() == "ambien":
        os.system("lynx http://psychonautwiki.org/wiki/Ambien")
        print("Finished searching for ambien!")

    elif search.lower() == "xanax":
        os.system("lynx http://psychonautwiki.org/wiki/Xanax")
        print("Finished searching for xanax!")

    elif search.lower() == "alc":
        os.system("lynx http://psychonautwiki.org/wiki/Alcohol")
        print("Finished searching for alcohol! Bleh!")

# mdma

# Fuck these drugs
    elif search.lower() == "fentanyl":
        os.system("lynx http://psychonautwiki.org/wiki/Fentanyl")
        print("Finished searching for fentanyl! Slow down, rockstar!")

    elif search.lower() == "dph":
        os.system("lynx http://psychonautwiki.org/wiki/Dph")
        print("Finished searching for DPH, you fucking idiot!")

# Coke

    elif search.lower() == "coke":
        os.system(
            "lynx http://psychonautwiki.org/wiki/Cocaine")
        print("Finished searching for cocaine!")

    elif search.lower() == 'cocaine':
        os.system('lynx http://psychonautwiki.org/wiki/Cocaine')
        print("Finished searching for cocaine!")


    # help

    elif search.lower() == "help":
        os.system("lynx https://www.brow.sh/docs/keybindings/")
        print("Finished helping!")

# Terraria Wiki (for the lulz also i need it lmao girls gotta game)

    elif search.lower() == "terraria":
        os.system(
            "lynx https://terraria.fandom.com")
        print("Finished searching Terraria!")

# OpenTTD wiki (also need dis)

    elif search.lower() == 'ttd':
        os.system("lynx https://wiki.openttd.org/en/")

# Minecraft wiki (also dis)

    elif search.lower() == 'minecraft':
        os.system('lynx https://minecraft.wiki/w/Minecraft_Wiki')

    elif search.lower() == 'mc':
        os.system('lynx https://minecraft.wiki/w/Minecraft_Wiki')

# exit software
    elif search.lower() == "exit":
        exit("closing debbie.")

    elif search.lower() == "clear":
        exit("closing debbie.")

    elif search.lower() == "close":
        exit("closing debbie.")

query()

os.system('python ~/.grungegirl/termweb.py')
