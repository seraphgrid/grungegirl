#!/usr/bin/env python

# Imports
import os
import time

# uninstall
os.system('clear')
print("スティッチバッシュシェルを一緒に戻します。")
os.system('sudo cp ~/.bashrc_bak/.bashrc ~')
time.sleep(2)
os.system('sudo rm -r ~/.bashrc_bak')
time.sleep(2)
print("バックアップ.BASHRCファイルが削除されました。")
time.sleep(2)
os.system('sudo rm -r ~/.grungegirl')
print("グランジガールNS")
time.sleep(1)
print('version 0.3 - bladee')
print('')
print('経験')
time.sleep(3)
os.system('clear')
