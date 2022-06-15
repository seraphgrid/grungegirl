# Imports
import subprocess
import os
import time
import subprocess

# Foundation laid for using tor with browsh.

# search function
print('最大限のセキュリティのためにVPNと一緒に使用する')
search = input("debbieデビー --> ")

drug = search

# search.lower() conditions


if search.lower() == "nothing":
    os.system("browsh http://psychonautwiki.org/")

elif search.lower() == "":
    os.system("browsh http://psychonautwiki.org/")

elif search.lower() == "search":
    os.system('browsh http://psychonautwiki.org')

# help

elif search.lower() == "help":
    os.system("browsh https://www.brow.sh/docs/keybindings/")
    print("Finished helping!")

# Terraria Wiki (for the lulz also i need it lmao girls gotta game)

elif search.lower() == "terraria":
    os.system( "browsh https://terraria.fandom.com")
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
    os.system('clear')

elif search.lower() == "close":
    exit("closing debbie.")

elif search.lower() == "c":
    exit("closing debbie.")

elif search.lower() == 'a':
    os.system('python ~/.grungegirl/astrology.py')
    exit()

elif search.lower() == 't':
    os.system('python ~/.grungegirl/tarot.py')
    exit()

else:
    
    os.system('browsh http://psychonautwiki.org/wiki/' + drug.lower())


os.system('python ~/.grungegirl/query.py')

