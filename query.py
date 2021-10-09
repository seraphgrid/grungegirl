# Imports
import subprocess
import os
import time
import subprocess

# Foundation laid for using tor with browsh.

# search function
search = input("debbie --> ")

# search.lower() conditions


def query():

    if search.lower() == "nothing":
        os.system(
            "browsh http://psychonautwiki.org/w/index.php?search=&title=Special%3ASearch&go=Go")

    elif search.lower() == "":
        os.system(
            "browsh http://psychonautwiki.org/w/index.php?search=&title=Special%3ASearch&go=Go")

# Weed
    if search.lower() == "weed":
        os.system("browsh http://psychonautwiki.org/wiki/Weed")
        print("Finished searching about weed!")

# Amphet

    elif search.lower() == "meth":
        os.system("browsh http://psychonautwiki.org/wiki/Meth")
        print("Finished searching for meth!")

    elif search.lower() == "speed":
        os.system("browsh http://psychonautwiki.org/wiki/Speed")
        print("Finished searching for speed!")

    elif search.lower() == "mdma":
        os.system("browsh http://psychonautwiki.org/wiki/MDMA")
        print("Finished searching for MDMA!")


# Psychedelics

    elif search.lower() == "shrooms":
        os.system("browsh http://psychonautwiki.org/wiki/Shrooms")
        print("Finished searching for shrooms!")

    elif search.lower() == "lsd":
        os.system("browsh http://psychonautwiki.org/wiki/LSD")
        print("Finished searching for LSD! Hold on to that burrito!")

    elif search.lower() == "peyote":
        os.system("browsh http://drugs.tripsit.me/peyote")
        print("Finished searching for peyote (tripsit)!")

    elif search.lower() == "salvia":
        os.system("browsh http://psychonautwiki.org/wiki/Salvia")
        print("Finished searching for salvia!")

    elif search.lower() == '1p':
        os.system("browsh https://psychonautwiki.org/wiki/1P-LSD")
        print('Finished searching for 1P-LSD!')

# Dissociatives / Downers

    elif search.lower() == "dxm":
        os.system("browsh http://psychonautwiki.org/wiki/Dxm")
        print("Finished searching for DXM!")

    elif search.lower() == "ambien":
        os.system("browsh http://psychonautwiki.org/wiki/Ambien")
        print("Finished searching for ambien!")

    elif search.lower() == "xanax":
        os.system("browsh http://psychonautwiki.org/wiki/Xanax")
        print("Finished searching for xanax!")

    elif search.lower() == "alc":
        os.system("browsh http://psychonautwiki.org/wiki/Alcohol")
        print("Finished searching for alcohol! Bleh!")

# mdma

# Fuck these drugs
    elif search.lower() == "fentanyl":
        os.system("browsh http://psychonautwiki.org/wiki/Fentanyl")
        print("Finished searching for fentanyl! Slow down, rockstar!")

    elif search.lower() == "dph":
        os.system("browsh http://psychonautwiki.org/wiki/Dph")
        print("Finished searching for DPH, you fucking idiot!")

# Coke

    elif search.lower() == "coke":
        os.system(
            "browsh http://psychonautwiki.org/wiki/Cocaine")
        print("Finished searching for cocaine!")

    elif search.lower() == 'cocaine':
        os.system('browsh http://psychonautwiki.org/wiki/Cocaine')
        print("Finished searching for cocaine!")


    # help

    elif search.lower() == "help":
        os.system("browsh https://www.brow.sh/docs/keybindings/")
        print("Finished helping!")

# Terraria Wiki (for the lulz also i need it lmao girls gotta game)

    elif search.lower() == "terraria":
        os.system(
            "browsh https://terraria.fandom.com")
        print("Finished searching Terraria!")

# OpenTTD wiki (also need dis)

    elif search.lower() == 'ttd':
        os.system("browsh https://wiki.openttd.org/en/")

# Minecraft wiki (also dis)

    elif search.lower() == 'minecraft':
        os.system('browsh https://minecraft.fandom.com/wiki/Minecraft_Wiki')

    elif search.lower() == 'mc':
        os.system('browsh https://minecraft.fandom.com/wiki/Minecraft_Wiki')

# exit software
    elif search.lower() == "exit":
        exit("closing debbie.")

    elif search.lower() == "clear":
        exit("closing debbie.")

    elif search.lower() == "clear":
        exit("closing debbie.")
query()

os.system('python ~/grungegirl/query.py')
