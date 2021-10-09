import os
import sys


def astro():

    query = input("strhckr --> ")


# Wiki

    if query.lower() == 'search':
        os.system('browsh https://www.astro.com/astrowiki/en/Main_Page')

    if query.lower() == '':
        os.system('browsh https://www.astro.com/astrowiki/en/Main_Page')

    if query.lower() == 'wiki':
        os.system('browsh https://www.astro.com/astrowiki/en/Main_Page')
# Signs

    elif query.lower() == "aries":
        os.system("python ~/.grungegirl/astrology/signs/aries.py")

    elif query.lower() == "taurus":
        os.system('python ~/.grungegirl/astrology/signs/taurus.py')

    elif query.lower() == 'gemini':
        os.system('python ~/.grungegirl/astrology/signs/gemini.py')

    elif query.lower() == 'cancer':
        os.system('python ~/.grungegirl/astrology/signs/cancer.py')

    elif query.lower() == 'leo':
        os.system('python ~/.grungegirl/astrology/signs/leo.py')

    elif query.lower() == 'virgo':
        os.system('python ~/.grungegirl/astrology/signs/virgo.py')

    elif query.lower() == 'libra':
        os.system('python ~/.grungegirl/astrology/signs/libra.py')

    elif query.lower() == 'scorpio':
        os.system('python ~/.grungegirl/astrology/signs/scorpio.py')

    elif query.lower() == 'sagittarius':
        os.system('python ~/.grungegirl/astrology/signs/sag.py')

    elif query.lower() == 'capricorn':
        os.system('python ~/.grungegirl/astrology/signs/cap.py')

    elif query.lower() == 'capricorn':
        os.system('python ~/.grungegirl/astrology/signs/cap.py')

    elif query.lower() == 'aquarius':
        os.system('python ~/.grungegirl/astrology/signs/aqua.py')

# Houses

    elif query.lower() == 'hs1':
        os.system('python ~/.grungegirl/astrology/houses/firsthouse.py')

    elif query.lower() == 'hs2':
        os.system('python ~/.grungegirl/astrology/houses/secondhouse.py')

    elif query.lower() == 'hs3':
        os.system('python ~/.grungegirl/astrology/houses/thirdhouse.py')

    elif query.lower() == 'hs4':
        os.system('python ~/.grungegirl/astrology/houses/fourthhouse.py')

    elif query.lower() == 'hs5':
        os.system('python ~/.grungegirl/astrology/houses/fifthhouse.py')

    elif query.lower() == 'hs6':
        os.system('python ~/.grungegirl/astrology/houses/sixthhhouse.py')

    elif query.lower() == 'hs7':
        os.system('python ~/.grungegirl/astrology/houses/seventhhouse.py')

    elif query.lower() == 'hs8':
        os.system('python ~/.grungegirl/astrology/houses/eighthhouse.py')

    elif query.lower() == 'hs9':
        os.system('python ~/.grungegirl/astrology/houses/ninthhouse.py')

    elif query.lower() == 'hs10':
        os.system('python ~/.grungegirl/astrology/houses/tenthhouse.py')

    elif query.lower() == 'hs11':
        os.system('python ~/.grungegirl/astrology/houses/eleventhhouse.py')

    elif query.lower() == 'hs12':
        os.system('python ~/.grungegirl/astrology/houses/twelfthhouse.py')

# Planets

    elif query.lower() == 'sun':
        os.system('python ~/.grungegirl/astrology/planets/sun.py')

    elif query.lower() == 'earth':
        os.system('python ~/.grungegirl/astrology/planets/earth.py')

    elif query.lower() == 'mercury':
        os.system('python ~/.grungegirl/astrology/planets/mercury.py')

    elif query.lower() == 'moon':
        os.system('python ~/.grungegirl/astrology/planets/moon.py')

    elif query.lower() == 'venus':
        os.system('python ~/.grungegirl/astrology/planets/venus.py')

    elif query.lower() == 'mars':
        os.system('python ~/.grungegirl/astrology/planets/mars.py')

    elif query.lower() == 'jupiter':
        os.system('python ~/.grungegirl/astrology/planets/jupiter.py')

    elif query.lower() == 'saturn':
        os.system('python ~/.grungegirl/astrology/planets/saturn.py')

    elif query.lower() == 'uranus':
        os.system('python ~/.grungegirl/astrology/planets/uranus.py')

    elif query.lower() == 'neptune':
        os.system('python ~/.grungegirl/astrology/planets/neptune.py')

    elif query.lower() == 'pluto':
        os.system('python ~/.grungegirl/astrology/planets/pluto.py')

# Aspects

    elif query.lower() == 'bi-quintile':
        os.system('python ~/.grungegirl/astrology/aspects/bi-quin.py')

    elif query.lower() == 'conjunction':
        os.system('python ~/.grungegirl/astrology/aspects/conjunction.py')

    elif query.lower() == 'opposition':
        os.system('python ~/.grungegirl/astrology/aspects/opposition.py')

    elif query.lower() == 'quincunx':
        os.system('python ~/.grungegirl/astrology/aspects/quincunx.py')

    elif query.lower() == 'quintile':
        os.system('python ~/.grungegirl/astrology/aspects/sem-quin.py')

    elif query.lower() == 'semi-sextile':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sextile.py')

    elif query.lower() == 'semi-square':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sq.py')

    elif query.lower() == 'sesquisquare':
        os.system('python ~/.grungegirl/astrology/aspects/sesquisq.py')

    elif query.lower() == 'square':
        os.system('python ~/.grungegirl/astrology/aspects/square.py')

    elif query.lower() == 'trine':
        os.system('python ~/.grungegirl/astrology/aspects/trine.py')

# Exit

    elif query.lower() == 'exit':
        exit('closing strhckr.')
        os.system('python ~/.grungegirl/main.py')

    elif query.lower() == 'clear':
        exit('closing strhckr.')
        os.system('python ~/.grungegirl/main.py')

    elif query.lower() == 'close':
        exit('closing strhckr.')
        os.system('python ~/.grungegirl/main.py')

    os.system('python ~/.grungegirl/astrology.py')


astro()
