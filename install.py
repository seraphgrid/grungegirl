#!/usr/bin/env python

# Setting the stage

import os
import time

# making backup bashrc file
os.system('clear')
print("backing up your .bashrc file. -death xx")
os.system('mkdir ~/.bashrc_bak')
time.sleep(2)
os.system('sudo cp ~/.bashrc ~/.bashrc_bak')

verify1 = input('Are you using Termux? (y/n) ')

if verify1 == 'y':
    os.system('python ~/grungegirl/termux/termux.py')
    exit()

if verify1 == '':
    os.system('python ~/grungegirl/termux/termux.py')
    exit()

# The V8 Engine


def v8():

    # girls know how to code

    print('歓迎するグランジガール.')
    time.sleep(1)
    print('Debianベースのシステムにブラウザをインストールします.')
    time.sleep(2)

    # inintializes the package managers of the most popular distros in order to ease installation process.

    print('初期化')
    os.system('sh browsh.sh')
    time.sleep(2)
    print('Red-Hatシステムにブラウザをインストールする。')
    time.sleep(1)
    os.system('sh browsh-fedora.sh')
    time.sleep(1)
    os.system('yay -a browsh')
    print('yayのインストールが完了しました。 私たちはあなたを愛し、赤ちゃん。')
    os.system('mkdir ~/.grungegirl')
    os.system('cp -r drugs/ ~/.grungegirl')
    os.system('cp -r astrology/ ~/.grungegirl/')
    os.system('cp -r astrology.py ~/.grungegirl')
    os.system('cp -r tarot.py ~/.grungegirl')
    os.system('cp -r tarot/ ~/.grungegirl')
    print("グランジガール 作成した.")
    print("")
    time.sleep(1)
    os.system('cp main.py ~/.grungegirl')
    print("コロンビアから薬を輸出する。")
    print(" ")
    print("SHROOMSの収穫 xx.")
    print(" ")
    time.sleep(1)
    print('インストールファイルのコピー')
    os.system('cp query.py ~/.grungegirl')
    os.system('cp bind-alias.sh ~/.grungegirl')
    print("エイリアスグランジガール.")
    time.sleep(2)
    os.system('sh ~/.grungegirl/bind-alias.sh')
    print('Max Security browsh/lynxでは、VPNを使用してください')
    print(" ")
    time.sleep(3)
    os.system('cd && clear && . ~/.bashrc')


v8()
