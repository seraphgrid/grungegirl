import time
import random
import ggsave
import os
import rage

bp = ggsave.bpn
crystals = ggsave.crystalsn
money = ggsave.moneyn
mining_speed = ggsave.mining_speedn
price_bp = ggsave.price_bpn
price_ms = ggsave.price_msn
price_mr = ggsave.price_mrn
rate_multi = ggsave.rate_multin
mining_rate = ggsave.mining_raten
wallet = ggsave.walletn



def command_line():
    
    global bp
    global crystals
    global price_bp
    global price_ms
    global price_mr
    
    print("Scrap Metal:", crystals)
    if crystals == bp:
        print("inventory_maximum_capacity_alert")
    print(wallet, "Amerinium")
    command_line = input("Command: ")
    valid_input = ['m', 's', 'u', 'ss', 'am']

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


def mining():

    global bp
    global crystals
    global money
    global mining_speed
    global wallet

    
    if crystals < bp:
        pass
        print("Preparing laser...")
        time.sleep(3)
        print("Stabilizing...")
        rng = [ 'a', 'b' ]
        rng2 = random.choice(rng)
        if rng2 == 'a':
            os.system('python rage.py')
        if rng2 == 'b':
            time.sleep(4)
            print("Mining space junk...")
            crystals += mining_rate
            time.sleep(mining_speed)
            print(crystals, "scraps of metal and plastic collected thus far.")
            sav()

        command_line()
    elif crystals == bp:
        command_line()
    
def automine():
    
    global bp
    global crystals
    global money
    global mining_speed
    global wallet


    if crystals < bp:
        crystals += bp
        sav()
        time.sleep(mining_speed)
        print(crystals, "scraps of metal and plastic collected thus far.")
        print("Inventory dump in progress.")
        time.sleep(4)
        money = crystals / random.randrange(4, 20)
        wallet = wallet + money
        money = 0
        crystals = 0
        print(wallet, "Amerinium in bank account.")
        sav()
        automine()
        





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

    if selection == 'bp':
        if wallet >= price_bp:
            bp += 5
            wallet -= wallet - price_bp
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
            wallet =  wallet - price_ms
            if wallet < 0:
                wallet = 0
            print("Mining speed upgraded.")
            print("You now have", wallet, "Amerinium.")
            sav()
        else:
            print("Not enough Amerinium.")

    if selection == 'mr':
        if wallet >= price_mr:
            mining_rate + random.randrange(4, 20)
            bp += 5
            wallet = price_mr - wallet
            if wallet < 0:
                wallet = 0
            print("Mining rate upgraded.")
            print("You now have", wallet, "Amerinium.")
            sav()
        else:
            print("Not enough funds.")

    command_line()

def sell():
    
    global crystals
    global money
    global bp
    global wallet

    if crystals > 0:
        
        print("Inventory release. Stand away from the door.")
        time.sleep(5)
        money = crystals + random.randrange(4, 20)
        wallet = wallet + money
        money = 0
        crystals = 0
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
    str2 = repr(crystals)
    file.write("crystalsn = " + str2 + "\n")
    str3 = repr(money)
    file.write("moneyn = " + str3 + "\n")
    str4 = repr(mining_speed)
    file.write("mining_speedn = " + str4 + "\n")
    str5 = repr(price_bp)
    file.write("price_bpn = " + str5 + "\n")
    str6 = repr(price_ms)
    file.write("price_msn = " + str6 + "\n")
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

    command_line()

sav()
os.system('python main.py')