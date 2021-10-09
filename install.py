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
    print('installing browsh on debian-based system.')
    time.sleep(2)

    # inintializes the package managers of the most popular distros in order to ease installation process.

    print('initializing.')
    os.system('sh browsh.sh')
    time.sleep(2)
    print('installing browsh on red-hat systems.')
    time.sleep(1)
    os.system('sh browsh-fedora.sh')
    time.sleep(1)
    os.system('yay -a browsh')
    print('yay installation complete. we love you, baby.')
    os.system('mkdir ~/.grungegirl')
    os.system('cp -r drugs/ ~/.grungegirl')
    os.system('cp -r astrology/ ~/.grungegirl/')
    os.system('cp -r astrology.py ~/.grungegirl')
    print("grungegirl created.")
    print("")
    time.sleep(1)
    os.system('cp main.py ~/.grungegirl')
    print("exporting drugs from columbia.")
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
    print('use vpn with browsh for max security.')
    print(" ")
    time.sleep(1)


v8()
