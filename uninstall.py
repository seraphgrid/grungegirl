#!/usr/bin/env python

# Imports
import os
import time
import shutil as sh

#folder check

grungegirl = "alias grungegirl='python ~/.grungegirl/main.py'"
home = '/home/' + os.getlogin() + '/'

with open(f'{home}.bashrc') as rc:

    rclines = rc.readlines()

    with open(f'{home}.bashrc_bak', "w") as rcb:

        for alias in rclines:
            if alias.strip('\n') != grungegirl:
                rcb.write(alias)

        rc.close()
        rcb.close()

        os.system(f'mv {home}.bashrc_bak {home}.bashrc')

        os.system(f'rm -rfv {home}.bashrc_bak {home}.grungegirl/')
        
        print("grungegirl removed.")

        
# uninstall
print('version 0.5 - telepath')
print('')
print('経験')
time.sleep(2)
os.system('clear')
