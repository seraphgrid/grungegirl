# Imports
import subprocess
import os

# Search function
search = input("Web Search: ")

# Search conditions

if search == "weed":
    subprocess.run(["lynx", "--anonymous", "https://psychonautwiki.org/wiki/Weed"])
    print("Finished searching about weed!")

elif search == "meth":
    subprocess.run(["lynx", "--anonymous", "https://psychonautwiki.org/wiki/Meth"])
    print("Finished searching for meth!")
else:
    print("Query returns no results.")

os.system('python ~/grungegirl/main.py')
