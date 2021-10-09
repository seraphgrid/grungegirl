#!/usr/bin/env python

# Imports
import os
import time

# uninstall
os.system('clear')
print("stitching bash shell back together.")
os.system('sudo cp ~/.bashrc_bak/.bashrc ~')
time.sleep(2)
os.system('sudo rm -r ~/.bashrc_bak')
time.sleep(2)
print("backup .bashrc file deleted.")
time.sleep(2)
os.system('sudo rm -r ~/.grungegirl')
print("grungegirl removed.")
time.sleep(1)
print('version 0.2 - babygirl')
print('')
print('i know u love me bitch')
time.sleep(3)
os.system('clear')
