#!/usr/bin/env python

# Setting the stage

import os
import time

# making backup bashrc file


# The V8 Engine


def v8():

    # girls know how to code

    print('歓迎するグランジガール.')
    time.sleep(1)
    print('Debianベースのシステムにブラウザをインストールします.')
    time.sleep(2)

    # inintializes the package managers of the most popular distros in order to ease installation process.

    # Debian-based Distros
    print('初期化')
    os.system('sh browsh.sh')
    time.sleep(2)

    # Fedora/Red-Hat
    print('Red-Hatシステムにブラウザをインストールする。')
    time.sleep(1)
    os.system('sh browsh-fedora.sh')
    time.sleep(1)

    # Arch Linux using yay
    os.system('yay -a browsh')
    print('yayのインストールが完了しました。 私たちはあなたを愛し、赤ちゃん。')
    os.system('')


    # Creates Directories and Moves Downloaded Directories to ~/.grungegirl
    print("Moving directories...")
    time.sleep(1)
    os.system('mkdir ~/.grungegirl')
    os.system('cp -r drugs/ ~/.grungegirl')
    os.system('cp -r astrology/ ~/.grungegirl/')
    os.system('cp -r astrology.py ~/.grungegirl')
    os.system('cp -r tarot.py ~/.grungegirl')
    os.system('cp -r tarot/ ~/.grungegirl')
    os.system('cp -r amerinium/ ~/.grungegirl')
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

    # Alias binding script so "grungegirl" works on the command line.
    os.system('sh ~/.grungegirl/bind-alias.sh')

    # Warning advising use of VPN with Browser for safety purposes.
    print('VPN recommended for browsh/lynxでは、VPNを使用してください')
    time.sleep(3)
    # Go back to the directory, clear terminal buffer, and reset using .bashrc as source file.
    os.system('cd && clear && . ~/.bashrc')


# Void
def v9():

    # Void Linux

    # Install Lynx

    print("Installing Lynx...")
    time.sleep(2)
    os.system('sudo xbps-install -Suv lynx')

    # Creates Directories and Moves Downloaded Directories to ~/.grungegirl
    print("Moving directories...")
    time.sleep(1)
    os.system('mkdir ~/.grungegirl && cp -r voidgirls/ ~/.grungegirl && cp -r drugs/ ~/.grungegirl && cp -r astrology/ ~/.grungegirl/ && cp -r astrology.py ~/.grungegirl')
    os.system('cp -r tarot.py ~/.grungegirl && cp -r tarot/ ~/.grungegirl && cp -r amerinium/ ~/.grungegirl')
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

    # Alias binding script so "grungegirl" works on the command line.
    os.system('sudo touch ~/.bashrc')
    os.system('sh ~/.grungegirl/voidgirls/bind-void.sh')

    # Warning advising use of VPN with Browser for safety purposes.
    print('VPN recommended for browsh/lynxでは、VPNを使用してください')
    time.sleep(3)
    # Go back to the directory, clear terminal buffer, and reset using .bashrc as source file.
    os.system('cd && clear && . ~/.bashrc')

os.system('clear')
print("backing up your .bashrc file. -death xx")
os.system('mkdir ~/.bashrc_bak')
time.sleep(2)
os.system('sudo cp ~/.bashrc ~/.bashrc_bak')

# Ask to install Termux
verify1 = input('Are you using Termux? (y/n) ')
veri_valid = [ 'y', 'n' ]

if verify1 == veri_valid[0]:
    os.system('python ~/grungegirl/termux/termux.py')

if verify1 == veri_valid[1]:
    void_query = input("Do you have Void Linux? (y/n) ")
    void_valid = ['y', 'n']
    if void_query == void_valid[0]:
        v9()
    if void_query == void_valid[1]:
        v8()
