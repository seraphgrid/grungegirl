#!/usr/bin/env python

import os
import time

def neko():
    
    print("wooooowwwwww")
    time.sleep(2)
    print("Rainbow cat. Phase reader. Blast keg.")
    time.sleep(2)

    distrol = [ 'slackware', 'debian', 'fedora', 'void', 'void linux', 'arch', 'arch linux', 'termux' ]

    distro = input("Distribution: ")
    
    if distro.lower() != distrol[3:4]:
        os.system('clear')
        print("backing up your .bashrc file. -death xx") 
        time.sleep(2)
        os.system('cp -rv ~/.bashrc ~/.bashrc_bak')

    if distro.lower() == distrol[0]:
        
        os.system('mkdir ~/.grungegirl')
        os.system('cp -rv tarot/ drugs/ astrology/ ~/.grungegirl') 
        os.system('cp -rv slack/*.py ~/.grungegirl') 
                
        print('VPN recommended for browsh/lynxでは、VPNを使用してください')
        time.sleep(3)

        os.system('sh bind-alias.sh')
        time.sleep(1)

        print("Slackware installation complete.")
        exit()

    elif distro.lower() == distrol[1]:
        
        print("Debian selected.")
        os.system('mkdir ~/.grungegirl')
        os.system('cp -rv drugs/ tarot/ astrology/ ~/.grungegirl') 
        os.system('cp -rv mainf/*.py ~/.grungegirl')
         
        os.system('wget https://github.com/browsh-org/browsh/releases/download/v1.6.4/browsh_1.6.4_linux_amd64.deb')
        os.system('sudo dpkg -i ./browsh_1.6.4_linux_amd64.deb')
        os.system('sudo rm -rfv ./browsh_1.6.4_linux_amd64.deb')
        os.system('echo "browsh installation complete."')
        
        print('VPN recommended for browsh/lynxでは、VPNを使用してください')
        time.sleep(3)

        os.system('sh bind-alias.sh')
        time.sleep(1) 


        exit()

    elif distro.lower() == distrol[2]:
        
        print('Red-Hatシステムにブラウザをインストールする。')
        os.system('wget https://github.com/browsh-org/browsh/releases/download/v1.6.4/browsh_1.6.4_linux_amd64.rpm')
        os.system('sudo rpm -i ./browsh_1.6.4_linux_amd64.rpm') 
        os.system('rm -rfv ./browsh_1.6.4_linux_amd64.rpm')
        os.system('mkdir ~/.grungegirl')
        os.system('cp -rv mainf/*.py ~/.grungegirl')  
        os.system('cp -rv tarot/ drugs/ astrology/ ~/.grungegirl')
       
        print('歓迎するグランジガール.')
       
        time.sleep(1)
        

        print('VPN recommended for browsh/lynxでは、VPNを使用してください')
        time.sleep(1)

        os.system('sh bind-alias.sh')
        time.sleep(1)
 
        exit("Red-hat installation complete. there was a stupid joke behind that sentence once")

    elif distro.lower() == distrol[3:4]:
       
        print("Installing Lynx...")
        time.sleep(2)
        os.system('sudo xbps-install -Suv lynx')

        # Creates Directories and Moves Downloaded Directories to ~/.grungegirl
        print("Moving directories...")
        os.system('cp -r voidgirls/astrology.py voidgirls/query.py mainf/tarot.py mainf/main.py ~/.grungegirl') 
        os.system('cp -r tarot/ astrology/ drugs/ ~/.grungegirl') 
        time.sleep(1)
        print("グランジガール 作成した.")
        print(" ")
        time.sleep(1) 
        os.system('sudo touch ~/.bashrc')
        os.system('sh ~/.grungegirl/voidgirls/bind-void.sh') 
        print('VPN recommended for browsh/lynxでは、VPNを使用してください')
        time.sleep(1)

        os.system('sh bind-alias.sh')
        time.sleep(1)

        
        exit()

    elif distro.lower() == distrol[5:6]:
        
        print("yay required to proceed. otherwise you will get some stupid error.")
        time.sleep(2)
        print("and im just gonna run yay anyway, but error handling will come")
        time.sleep(2)
        os.system('cp -r drugs/ tarot/ astrology/ ~/.grungegirl') 
        os.system('cp -r mainf/*.py ~/.grungegirl')
        
        os.system('yay -a browsh')
        print('yayのインストールが完了しました。 私たちはあなたを愛し、赤ちゃん。')
        time.sleep(2)

        print('VPN recommended for browsh/lynxでは、VPNを使用してください')
        time.sleep(1)
        os.system('sh bind-alias.sh')
        time.sleep(1)
 
        exit() 

    elif distro.lower() == distrol[7]:
        os.system('python termux/termux.py')
        exit()

neko()
