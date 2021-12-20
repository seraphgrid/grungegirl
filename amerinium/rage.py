import random
import time

ship_h = 100
enship_h = 100  
dmgx = random.randrange(1, 30)
attack = 2.5 + dmgx
attack2 = 3.5 + dmgx
shipchance = random.choice([True, False])
evchance = random.choices([True, False])

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
    if enship_h < 0:
        print("Enemy ship defeated!")
        break
    
                        
           
def damage_player():
    
    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance
    
    print("Your ship has been damaged!")
    ship_health = ship_h - attack2
    ship_h = ship_health
    print("Your ship at", ship_h, "health.")
    if ship_h < 0:
        print("Your ship defeated!")
        break
    
    
def shipattk():
    
    global evchance
    global enship_h
    global ship_h
    global dmgx
    global attack
    global attack2
    global shipchance

    
    attackprompt = input("C: ")

    if attackprompt.lower() == "a":
        while True:
            a = [ 'a', 'b' ] 
            fns2 = random.choice(a)
            if fns2 == 'a':
                damage_enemy()
                shipattk()
                break
            elif fns2 == 'b':
                damage_player()
                shipattk()
                
            

        


shipattk()
            
        
