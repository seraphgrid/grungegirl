
#!/usr/bin/env python

# Setting the stage
import os
import time

# making backup bashrc file
print("backing up your .bashrc file. -death xx")
os.system('mkdir ~/.bashrc_bak')
time.sleep(2)
os.system('sudo cp ~/.bashrc ~/.bashrc_bak')

# The V8 Engine


def v8():

    # girls know how to code
    print('welcome to grungegirl.')
    print('currently supporting the most popular distros to autoinstall w3m.')
    time.sleep(4)
    # inintializes the package managers of the most popular distros in order to ease installation process.
    print('initialiizing')
    os.system(
        'sudo apt-get update -y && sudo apt upgrade -y && sudo apt-get install -y w3m')
    os.system('sudo pacman -Syu w3m')
    os.system('sudo zypper refresh && zypper install w3m')
    os.system('sudo dnf update && sudo dnf install w3m')
    os.system('')
    os.system('mkdir ~/.grungegirl')
    os.system('cp -r drugs/ ~/.grungegirl')
    os.system('cp -r astrology/ ~/.grungegirl/')
    os.system('cp -r astrology.py ~/.grungegirl')
    print("grungegirl created.")
    print(" ")
    time.sleep(1)
    os.system('cp main.py ~/.grungegirl')
    print("exporting drugs from columbia.")
    time.sleep(1)
    print(" ")
    print("harvesting shrooms. xx")
    print(" ")
    time.sleep(1)
    print('copying install files.')
    os.system('cp query.py ~/.grungegirl')
    os.system('cp bind-alias.sh ~/.grungegirl')
    print("aliasing grungegirl.")
    time.sleep(2)
    os.system('sh ~/.grungegirl/bind-alias.sh')
    print('use vpn with w3m for max security.')
    print(" ")
    time.sleep(1)

# verify


verify = input("Do you have access to root privileges (y/n)? ")

if verify == "n":
    exit("exiting.")

if verify == "y":
    print("Starting installation.")
    time.sleep(1)
    v8()

elif verify == "":
    print("Starting installation.")
    time.sleep(1)
    v8()
