import os
import sys
import time

os.system('clear')
print("backing up your .bashrc file. -death xx")
os.system('mkdir ~/.bashrc_bak')
time.sleep(2)
os.system('sudo cp .bashrc ~/.bashrc_bak')
os.system('sudo cp .bashrc ~')

# Termux Installation


def termux():

    # girls know how to code

    print('welcome to grungegirl.')
    print('installing lynx on termux.')
    time.sleep(2)

    # inintializes the package managers of the most popular distros in order to ease installation process.

    print('initializing.')
    os.system('pkg install lynx')
    time.sleep(2)
    os.system('mkdir ~/.grungegirl')
    os.system('cp -r grungegirl/drugs/ ~/.grungegirl')
    os.system('cp -r grungegirl/astrology/ ~/.grungegirl/')
    os.system('cp -r grungegirl/astrology.py ~/.grungegirl')
    print("grungegirl created.")
    print("")
    time.sleep(1)
    os.system('cp termmain.py ~/.grungegirl')
    os.system('cp termastro.py ~/.grungegirl')
    os.system('cp termweb.py ~/.grungegirl')
    print("exporting drugs from columbia.")
    print(" ")
    print("harvesting shrooms. xx")
    print(" ")
    time.sleep(1)
    print('copying install files.')

    print("aliasing grungegirl.")
    time.sleep(2)
    print('use vpn with lynx for max security.')
    print(" ")
    time.sleep(3)
    os.system('cd && clear && . ~/.bashrc')


termux()
exit()