# Imports
import os
import pandas as panda

# version name, version tagline, drug search

print("グランジガール  - 0.4 - telepath")
print("愛は痛みです。 愛は至福です。")
print(" ")
print("THE興VOID+ --> https://discord.gg/EJj9sJsSTN")
print(" ")
drug = input("グランジガール --> ")
drug_selected = drug
drugs = {
        depressants = [ 'alc', 'diazepam', 'kratom', 'hydrocodone', 'gabapentin', 'heroin', 'xanax', 'fentanyl' ]
        amphetamines = [ 'coke', 'mdma', 'speed', 'meth' ]
        }
# Web (Debbie)

debbie_commands = [ 'debbie', 'deb', 'w', 'web' ] 

if drug.lower() in debbie:
	os.system('python3 ~/.grungegirl/query.py')

# Tarot Reader

tarot_commands = [ 'tarot', 'trot', 't', 'card', 'cards' ] 

if drug.lower() in tarot: 
	os.system('python3 ~/.grungegirl/tarot.py')
# Weed

if drug.lower() == "weed":
	os.system('python3 ~/.grungegirl/drugs/w.py')

# Depressants

elif drug.lower() == "alc":
	os.system('python3 ~/.grungegirl/drugs/depress/alc.py')

elif drug.lower() == 'diazepam':
	os.system('python3 ~/.grungegirl/drugs/depress/diaz.py')

elif drug.lower() == 'kratom':
	os.system('python3 ~/.grungegirl/drugs/depress/kratom.py')

elif drug.lower() == 'hydrocodone':
	os.system('python3 ~/.grungegirl/drugs/depress/hydro.py')

elif drug.lower() == 'gabapentin':
	os.system('python3 ~/.grungegirl/drugs/depress/gaba.py')

elif drug.lower() == 'heroin':
	os.system('python3 ~/.grungegirl/drugs/depress/heroin.py')

elif drug.lower() == 'xanax':
	os.system('python3 ~/.grungegirl/drugs/depress/xanax.py')

# Fentanyl

elif drug.lower() == "fentanyl":
	os.system('python3 ~/.grungegirl/drugs/fent.py')

# Amphetamines

elif drug.lower() == "coke":
	os.system('python3 ~/.grungegirl/drugs/coke.py')

elif drug.lower() == "mdma":
	os.system('python3 ~/.grungegirl/drugs/amphet/mdma.py')

elif drug.lower() == "speed":
	os.system('python3 ~/.grungegirl/drugs/amphet/speed.py')

elif drug.lower() == "meth":
	os.system('python3 ~/.grungegirl/drugs/amphet/meth.py')

# Psychedelics

elif drug.lower() == "peyote":
	os.system('python3 ~/.grungegirl/drugs/psychedelics/pey.py')

elif drug.lower() == "salvia":
	os.system('python3 ~/.grungegirl/drugs/psychedelics/salvia.py')

elif drug.lower() == "lsd":
	os.system('python3 ~/.grungegirl/drugs/psychedelics/lsd.py')

elif drug.lower() == "shrooms":
	os.system('python3 ~/.grungegirl/drugs/psychedelics/shrooms.py')

elif drug.lower() == '1p':
	os.system('python3 ~/.grungegirl/drugs/psychedelics/1P_LSD.py')

elif drug.lower() == 'dmt':
	os.system('python3 ~/.grungegirl/drugs/psychedelics/dmt.py')

elif drug.lower() == "2cb":
	os.system('python3 ~/.grungegirl/drugs/psychedelics/2C-B-Fly.py')

elif drug.lower() == 'aco':
	os.system('python3 ~/.grungegirl/drugs/psychedelics/4-AcO-Met.py')

elif drug.lower() == '4ho':
	os.system('python3 ~/.grungegirl/drugs/psychedelics/4homet.py')

elif drug.lower() == 'ayahuasca':
	os.system('python3 ~/.grungegirl/drugs/psychedelics/ayahuasca.py')

# Dissociatives

elif drug.lower() == "ambien":
	os.system('python3 ~/.grungegirl/drugs/ambien.py')

elif drug.lower() == "dxm":
	os.system('python3 ~/.grungegirl/drugs/dxm.py')

# Deliriants

elif drug.lower() == "dph":
	os.system('python3 ~/.grungegirl/drugs/dph.py')

# astrology (strhckr)

astral_commands = [ 'astro', 'astrology', 'strhckr', 'starhacker', 'str', 'a' ] 

elif drug.lower() in astral_commands:
	os.system('python3 ~/.grungegirl/astrology.py')

# Game

elif drug.lower() == 'amerinium':
	os.system('python3 ~/.grungegirl/amerinium/trash.py')

elif drug.lower() == 'am':
	os.system('python3 ~/.grungegirl/amerinium/trash.py')

# exit software
exit_commands = [ 'exit', 'close', 'c' ] 
elif drug.lower() == "exit":
	os.system('clear')
	exit("grungegirl exiting.")

elif drug.lower() == "clear":
	os.system('clear')

if drug.lower() in exit_commands:
	os.system('clear')
	exit('grungegirl exiting.\n')

os.system('python3 ~/.grungegirl/main.py')
