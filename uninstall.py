#!/usr/bin/env python

# Imports
import os
import time

#folder check
uninstall_ask = input('Uninstalling on Void? (y/n) ')
valid_input = [ 'y', 'n' ]
if uninstall_ask == valid_input[0]:
    os.system('sh voidcheck.sh')

if uninstall_ask == valid_input[1]:
    os.system('sh filecheck.sh')


# uninstall
print('version 0.3 - bladee')
print('')
print('経験')
time.sleep(3)
os.system('clear')
