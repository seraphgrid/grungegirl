import time
import random
import ggsave
import os
import rage_s
import rage_s_bakup

# Miner Stats
bp = ggsave.bpn
scraps = ggsave.scrapsn
money = ggsave.moneyn
mining_speed = ggsave.mining_speedn
price_bp = ggsave.price_bpn
price_ms = ggsave.price_msn
price_mr = ggsave.price_mrn
price_pwr = ggsave.price_pwrn
rate_multi = ggsave.rate_multin
mining_rate = ggsave.mining_raten
wallet = ggsave.walletn

# Attack Stats
ship_h = 250
enship_h = 200
dmgx = 11
attack_cnt = 15
attack = range(3, 13)
attack2 = range(3, 13)
shipchance = True
evchance = [False]
shield = 10
pwrcount = 4
pwrdmg = 20
aimed = False
en_aimed = False
reloaded = False
in_battle = False




def command_line():
    
    global bp
    global scraps
    global price_bp
    global price_ms
    global price_mr
    
    print("Scrap Metal:", scraps)
    
    
    if scraps == bp:
        print("Inventory at max capacity.")
    if wallet == 1:
        print(wallet, "Amerinium")
    if wallet == 0:
        print(wallet, "Ameriniates")
    if wallet > 1:
        print(wallet, "Ameriniates")

    valid_input = ['mine', 'sell', 'upgrade', 'save', 'automine']
    valid_util = [ 'clear', 'exit' ]
    command_line = input("Command: ")

    
    

    if command_line == valid_input[0]:
        mining()
        
    if command_line == valid_input[1]:
        sell()
        
    if command_line == valid_input[2]:
        upg()
        
    if command_line == valid_input[3]:
        sav()
        
    if command_line == valid_input[4]:
        automine()

    if command_line == valid_util[0]:
        os.system('clear')

    if command_line == valid_util[1]:
        sav()
        os.system('grungegirl')
        
    if command_line != valid_input:
        command_line = input("Command: ")
        valid_input = ['mine', 'sell', 'upgrade', 'save', 'automine', 'a' ]
        valid_util = ['clear', 'exit']
        
        if command_line == valid_input[0]:
            mining()
        
        if command_line == valid_input[1]:
            sell()
            
        if command_line == valid_input[2]:
            upg()
            
        if command_line == valid_input[3]:
            sav()
            
        if command_line == valid_input[4]:
            automine()

        if command_line == valid_util[0]:
            os.system('clear')

        if command_line == valid_util[1]:
            sav()
            os.system('grungegirl')
        
def player_aim():

    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    global shield
    global pwrdmg
    global pwrcount
    global wallet
    global aimed



    if enship_h > 0:
        print("Aiming cannon...")
        time.sleep(2)
        print("Locking on..")

        rngplus = [ 'a', 'b' ]
        rngplus2 = random.choice(rngplus)
        if rngplus2 == 'a':
            print("Your ship has been damaged by an asteroid!")
            ship_health = ship_h - random.choice(attack2)
            ship_h = ship_health
            print("Your ship at", ship_h, "health.")
        if rngplus2 == 'b':
            time.sleep(1)
            print("Locked on.")
            aimed = True
            shipattk()


def en_aim():

    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    global shield
    global pwrdmg
    global pwrcount
    global wallet
    global aimed
    global en_aimed

    if ship_h > 0:
        play_aim = True

    if play_aim == True:
        print("Enemy aiming cannon...")
        time.sleep(2)
        print("Locking on..")

        rngplus = [ 'a', 'b' ]
        rngplus2 = random.choice(rngplus)
        if rngplus2 == 'a':
            print("Enemy ship has been damaged by asteroid!")
            ship_health = enship_h - random.choice(attack2)
            enship_h = ship_health
            print("Enemy ship at", enship_h, "health.")
        if rngplus2 == 'b':
            time.sleep(1)
            print("Locked on.")
            en_aimed = True
            shipattk()


def rload():

    global reloaded
    global attack_cnt

    print("Reloading...")
    time.sleep(2)
    attack_cnt = 15
    reloaded = True
    print("Reloaded.")




def shipattk():
    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    global shield
    global pwrcount
    global attack_cnt
    global reloaded
    global in_battle

    in_battle = True
    sav()
    sav2()

    if enship_h < 0:
	    pwrcount = 4
	    ship_h = 200
	    enship_h = 200
	    shield = 10
	
        
    
    if ship_h < 0:
	    pwrcount = 4
	    ship_h = 200
	    enship_h = 200
	    shield = 10
		
        
    
    sav2()
    print("Health:", ship_h)
    print("en_Health:", enship_h)
    attackprompt = input("C: ")
    valid_attack = [ 'a', 'shield', 'powershot' ]
    valid_def = [ 'aim', 'reload' ]
    utilcom = [ 'clear', 'exit' ]

    if attackprompt.lower() == valid_attack[0]:
        while True:

            # Flip coin.

            a = ['a', 'b']
            fns2 = random.choice(a)
            # If coin lands on side a, misfire.

            if fns2 == 'a':
                fns3 = random.choice(a)
                if fns3 == 'a':
                    if attack_cnt < 0:
                        reloaded = False
                        print("Out of ammo. Reload needed.")
                        shipattk()
                    if reloaded == True:
                        attack_cnt -= 1
                        print('You missed!')
                        shipattk()


                # If coin lands on side b, the shot lands.

                if fns3 == 'b':
                    if attack_cnt < 0:
                        reloaded = False
                    if reloaded == True:
                        attack_cnt -= 1
                        damage_enemy()
                        shipattk()
                    if reloaded == False:
                        print("Out of ammo. Reload needed.")
                        shipattk()


            # The enemy can land a shot before you do, but also misfire.
            # This is due to the lore of the game. Mining ships probably wouldn't be the most combat-adept.
            elif fns2 == 'b':
                fns5 = random.choice(a)
                if fns5 == 'a':
                    print('The enemy ship missed!')
                    shipattk()
                if fns5 == 'b':
                    damage_player()
                    shipattk()
                    
    # Triggering various attack parameters.
    if attackprompt.lower() == valid_attack[1]:
        shieldless()
        shipattk()

    if attackprompt.lower() == valid_attack[2]:
        poweratk()
        aimed = False

    # Triggering various defense parameters.

    if attackprompt.lower() == valid_def[0]:
        player_aim()

    if attackprompt.lower() == valid_def[1]:
        rload()

    if attackprompt.lower() == utilcom[0]:
        os.system('clear')

    if attackprompt.lower() == utilcom[1]:
        sav()
        os.system('grungegirl')
        
    if attackprompt.lower() != valid_attack:
        shipattk()

    if attackprompt.lower() != valid_def:
        shipattk()





def mining():

    global bp
    global scraps
    global money
    global mining_speed
    global wallet

    
    if scraps < bp:
        pass
        print("Preparing laser...")
        time.sleep(3)
        print("Stabilizing...")
        time.sleep(2)
        rng = [ 'a', 'b' ]
        rng2 = random.choice(rng)
        if rng2 == 'a':
            print("You've been attacked!")
            shipattk()
        if rng2 == 'b':
            time.sleep(4)
            print("Mining space junk...")
            scraps += mining_rate
            time.sleep(mining_speed)
            print(scraps, "scraps of metal and plastic collected thus far.")
            sav()

        command_line()

    elif scraps == bp:
        command_line()
    
    
def am():
    
    global bp
    global scraps
    global money
    global mining_speed
    global wallet
    
    a = range(2, 5)
    scraps += random.choice(a)
    print("Quick mining (returns less).")
    time.sleep(mining_speed)
    print(scraps, "scraps of metal and plastic collected thus far.")
    print("Inventory dump in progress.")
    time.sleep(4)
    money = scraps / random.choice(rate_multi)
    wallet = wallet + money
    money = 0
    scraps = 0
    print(wallet, "Amerinium in bank account.")
    sav()
    
def automine():
    
    global bp
    global scraps
    global money
    global mining_speed
    global wallet

    am()
    am()
    am()
    am()
    am()


def upg():

    global money
    global mining_speed
    global bp
    global price_bp
    global price_ms
    global price_mr
    global mining_rate
    global wallet


    print("""Mining Rate: """, price_mr, """
Mining Speed: """, price_ms, """
Inventory: """, price_bp)
    selection = input("""Upgrade Parts: """)

    if selection == 'i':
        if wallet >= price_bp:
            bp += 5
            wallet -= price_bp
            if wallet < 0:
                wallet = 0
            print("Inventory upgraded.")
            print("You now have", wallet, "Amerinium.")
            sav()
        else:
            print("Not enough Amerinium.")

    if selection == 'ms':
        
        if wallet >= price_ms:
            mining_speed -= 1
            wallet -= price_ms
            if wallet < 0:
                wallet = 0
            print("Mining speed upgraded.")
            print("You now have", wallet, "Amerinium.")
            sav()
        else:
            print("Not enough Amerinium.")

    if selection == 'mr':
        if wallet >= price_mr:
            mining_rate += 2
            bp += 5
            wallet -= price_mr
            if wallet < 0:
                wallet = 0
            print("Mining rate upgraded to", mining_rate)
            print("You now have", wallet, "Amerinium.")
            sav()
        else:
            print("Not enough funds.")

    if selection == 'pwr':
        wallet -= price_pwr
        pwrdmg += 2
        if wallet < 0:
            wallet = 0
        print("Powershot damage upgraded.")
        print("You now have", wallet, "Amerinium.")

    command_line()

def sell():
    
    global scraps
    global money
    global bp
    global wallet

    if scraps > 0:
        
        print("Inventory release. Stand away from the door.")
        time.sleep(5)
        money = scraps + random.randrange(4, 20)
        wallet = wallet + money
        money = 0
        scraps = 0
        print(wallet, "Amerinium in bank account.")
        time.sleep(1)
        sav()
        command_line()
       

def sav():

    # open file
    file = open("ggsave.py", "w")

    # convert variable to string
    region = "import random"
    file.write(region + "\n")
    str1 = repr(bp)
    file.write("bpn = " + str1 + "\n")
    str2 = repr(scraps)
    file.write("scrapsn = " + str2 + "\n")
    str3 = repr(money)
    file.write("moneyn = " + str3 + "\n")
    str4 = repr(mining_speed)
    file.write("mining_speedn = " + str4 + "\n")
    str5 = repr(price_bp)
    file.write("price_bpn = " + str5 + "\n")
    str6 = repr(price_ms)
    file.write("price_msn = " + str6 + "\n")
    str11 = repr(price_pwr)
    file.write("price_pwrn = " + str11 + "\n")
    str7 = repr(rate_multi)
    file.write("rate_multin = " + str7 + "\n")
    str8 = repr(price_mr)
    file.write("price_mrn = " + str8 + "\n")
    str9 = repr(mining_rate)
    file.write("mining_raten = " + str9 + "\n")
    str10 = repr(wallet)
    file.write("walletn = " + str10 + "\n")

    # close file
    file.close()

    f = open('ggsave.py', 'r')
    if f.mode == 'r':
        contents = f.read()


# Combat Information Save State
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
    str9 = repr(pwrcount)
    file.write("pwrcountn = " + str8 + "\n")
    str10 = repr(pwrdmg)
    file.write("pwrdmgn = " + str8 + "\n")


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
    global wallet
    global in_battle

    print("Firing laser...")
    enship_health = enship_h - random.choice(attack)
    enship_h = enship_health
    print("Enemy ship at", enship_h, "health.")
    while enship_h < 0:
        wallet += 100
        time.sleep(2)
        print("Enemy ship defeated! Amerinium awarded!")
        in_battle = False
        sav()
        command_line()


def damage_player():
    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    global shield
    global wallet
    global in_battle

    print("Your ship has been damaged!")
    ship_health = ship_h - random.choice(attack2)
    ship_h = ship_health
    print("Your ship at", ship_h, "health.")
    if ship_h < 0:
        wallet -= 250
        if wallet < 0:
            wallet = 0
        print("Your ship defeated! 250 Amerinium lost!")
        in_battle = False
        sav()
        command_line()


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
    if shield > 0:
        ship_h = ship_h + random.choice(attack2)
        shield -= 5
        print("Shields sustaining at", shield)
        shipattk()


def poweratk():
    
    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    global shield
    global pwrdmg
    global pwrcount
    global wallet
    global aimed


    if pwrcount == 0:
        shipattk()

    if aimed == True:
        print("Firing laser...")
        enship_health = enship_h - pwrdmg
        pwrcount -= 1
        enship_h = enship_health
        aimed = False
        print("Enemy ship at", enship_h, "health.")
        while enship_h < 0:
            wallet += 200
            print("You obliterated them... Amerinium awarded!")
            aimed = False
            command_line()



    if aimed == False:
        print("You have not aimed!")

if in_battle == True:
    shipattk()
if in_battle == False:
    command_line()
os.system('python ~/.grungegirl/amerinium/trash.py')

