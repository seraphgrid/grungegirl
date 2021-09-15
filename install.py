#!/usr/bin/env python

# Setting the stage
import os

# The V8 Engine
def v8():

    os.system('yay -s browsh')

    os.system('mkdir ~/grungegirl')
    print("grungegirl created.")

    os.system('cp main.py ~/grungegirl')
    print("exporting drugs from columbia.")
    print(" ")
    os.system('cp drugs/alc.py ~/grungegirl')
    os.system('cp drugs/ambien.py ~/grungegirl')
    os.system('cp drugs/coke.py ~/grungegirl')
    os.system('cp drugs/dph.py ~/grungegirl')
    os.system('cp drugs/dxm.py ~/grungegirl')
    os.system('cp drugs/fent.py ~/grungegirl')
    os.system('cp drugs/mdma.py ~/grungegirl')
    os.system('cp drugs/meth.py ~/grungegirl')
    os.system('cp drugs/pey.py ~/grungegirl')
    os.system('cp drugs/salvia.py ~/grungegirl')
    os.system('cp drugs/shrooms.py ~/grungegirl')
    os.system('cp drugs/speed.py ~/grungegirl')
    os.system('cp drugs/weed.py ~/grungegirl')
    os.system('cp drugs/xanax.py ~/grungegirl')
    print("harvesting shrooms.")
    print(" ")
    print("integrating browsh functionality.")
    os.system('cp query.py ~/grungegirl')
    os.system('cp bind-alias.sh ~/grungegirl')
    print("aliasing grungegirl.")
    os.system('sh ~/grungegirl/bind-alias.sh')
    print("browsh needed to use web search.")
    print("if the install was successful then ignore this.")


# verify

verify = input("Are you root (y/n)? ")

if verify == "n":
    exit()

if verify == "y":
    print("Starting program.")
    v8()
