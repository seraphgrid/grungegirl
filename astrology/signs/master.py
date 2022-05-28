import re

fire = [ 'aries', 'leo', 'sagittarius' ] 

water = [ 'cancer', 'scorpio', 'pisces' ]

earth = [ 'taurus', 'virgo', 'capricorn' ]

air = [ 'gemini', 'libra', 'aquarius' ]

input_a = input(str("Sign: "))
 
def astro_info(sign): 

    
    if sign in fire:
        element = "Fire"
        print(element)
    elif sign in water:
        element = "Water"
        print(element)
    elif sign in earth:
        element = "Earth" 
        print(element)
    elif sign in air:
        element = "Air"
        print(element)
        
astro_info(sign=input_a)
