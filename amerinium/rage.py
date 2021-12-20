import random
import time
import os
import rage_s
import rage_s_bakup
import main

ship_h = 100
enship_h = 100
dmgx = 11
attack = 13.5
attack2 = 14.5
shipchance = True
evchance = [False]
shield = 100


print("You've been attacked!")


def sav2():
    # open file
    file = open("rage_s.py", "w")

    # convert variable to string
    region = "import random"
    region2 = "import time"
    region3 = "import os"
    file.write(region + "\n")
    file.write(region2 + "\n")
    file.write(region3 + "\n")
    str1 = repr(ship_h)
    file.write("ship_hn = " + str1 + "\n")
    str2 = repr(enship_h)
    file.write("enship_hn = " + str2 + "\n")
    str3 = repr(dmgx)
    file.write("dmgxn = " + str3 + "\n")
    str4 = repr(attack)
    file.write("attackn = " + str4 + "\n")
    str5 = repr(attack2)
    file.write("attack2n = " + str5 + "\n")
    str6 = repr(shipchance)
    file.write("shipchancen = " + str6 + "\n")
    str7 = repr(evchance)
    file.write("evchancen = " + str7 + "\n")
    str8 = repr(shield)
    file.write("shieldn = " + str8 + "\n")

    # close file
    file.close()

    f = open('rage_s.py', 'r')
    if f.mode == 'r':
        contents = f.read()

def damage_enemy():
    
    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    
    print("Firing laser...")
    enship_health = enship_h - attack
    enship_h = enship_health
    print("Enemy ship at", enship_h, "health.")
    while enship_h < 0:
        print("Enemy ship defeated!")
        os.system('python main.py')


    
                        
           
def damage_player():
    
    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    global shield

    print("Your ship has been damaged!")
    ship_health = ship_h - attack2
    ship_h = ship_health
    print("Your ship at", ship_h, "health.")
    while ship_h < 0:
        print("Your ship defeated!")
        os.system('python main.py')

    
    
def shipattk():
    
    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance

    sav2()
    print("Health:", ship_h)
    print("en_Health:", enship_h)
    attackprompt = input("C: ")

    if attackprompt.lower() == "a":
        while True:
            a = [ 'a', 'b' ] 
            fns2 = random.choice(a)
            if fns2 == 'a':
                fns3 = random.choice(a)
                if fns3 == 'a':
                    print('You missed!')
                    shipattk()
                if fns3 == 'b':
                    damage_enemy()
                    shipattk()
            elif fns2 == 'b':
                fns3 = random.choice(a)
                if fns3 == 'a':
                    print('The enemy ship missed!')
                    shipattk()
                if fns3 == 'b':
                    damage_player()
                    shipattk()
    if attackprompt.lower() == 's':
        shieldless()
        shipattk()


def shieldless():

    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    global shield

    if shield == 0:
        damage_player()
        shipattk()
    elif shield > 0:
        shieldful = [ 'a', 'b' ]
        shieldful2 = random.choice(shieldful)
        if shieldful2 == 'a':
            damage_player()
            shipattk()
        if shieldful2 == 'b':
            ship_h = ship_h + attack2
            shield -= 5
            print("Shields sustaining at", shield)
            shipattk()

        
shipattk()

ship_h = rage_s.ship_hn
enship_h = rage_s.enship_hn
dmgx = rage_s.dmgxn
attack = rage_s.attackn
attack2 = rage_s.attack2n
shield = rage_s.shieldn
# Useless Variables for now
shipchance = rage_s.shipchancen
evchance = rage_s.evchancen