import os
import sys


def astro():

    search = [ 'search', '', 'wiki' ]

    nnode = [ 'north node', 'nnode', 'nn' ]

    snode = [ 'south node', 'snode', 'sn' ]

    asc = [ 'asc', 'ascendant', 'ascendent' ]

    hse1 = [ 'hs1', 'the first house', 'house one', 'first house' ]

    hs2 = [ 'hs2', 'the second house', 'second house', 'house two']

    query = input("星hacker --> ")


    # Wiki

    if query.lower() == search[0:2]:
        os.system('lynx https://www.astro.com/astrowiki/en/Main_Page')
        os.system('clear')

# Horoscope

    elif query.lower() == 'daily':
        os.system('lynx https://www.astrosage.com/horoscope/daily-horoscope-todays-horoscope.asp')
        os.system('clear')

    elif query.lower() == 'tomorrow':
        os.system('lynx https://www.astrosage.com/horoscope/tomorrow-horoscope.asp')
        os.system('clear')

    elif query.lower() == 'weekly':
        os.system('lynx https://www.astrosage.com/horoscope/weekly-horoscope.asp')
        os.system('clear')

    elif query.lower() == 'monthly':
        os.system('lynx https://www.astrosage.com/horoscope/monthly-aries-horoscope.asp')
        os.system('clear')
    elif query.lower() == 'day':
        os.system('lynx https://www.astrosage.com/horoscope/daily-horoscope-todays-horoscope.asp')
        os.system('clear')
    elif query.lower() == 'week':
        os.system('lynx https://www.astrosage.com/horoscope/tomorrow-horoscope.asp')
        os.system('clear')
    elif query.lower() == 'month':
        os.system('lynx https://www.astrosage.com/horoscope/weekly-horoscope.asp')
        os.system('clear')
    elif query.lower() == 'pro':
        os.system('lynx https://www.astro.com/cgi/atxgen.cgi?btyp=wh')
        os.system('clear')

# Points

    elif query.lower() == nnode[0:2]:
        os.system('python ~/.grungegirl/astrology/points/nnode.py')

    elif query.lower() == snode[0:2]:
        os.system('python ~/.grungegirl/astrology/points/snode.py')

# ----------------------- Ascendant

    elif query.lower() == asc[0:2]:
        os.system('python ~/.grungegirl/astrology/points/ascendant.py')

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

    elif query.lower() == 'pisces':
        os.system('python ~/.grungegirl/astrology/signs/pisces.py')

# Houses

    hse1 = ['hs1', 'the first house', 'first house']

    hs2 = ['hs2', 'the second house', 'second house']

    elif query.lower() == hse1[0:2]:
        os.system('python ~/.grungegirl/astrology/houses/firsthouse.py')

    elif query.lower() == 'hs2':
        os.system('python ~/.grungegirl/astrology/houses/secondhouse.py')

    elif query.lower() == 'the second house':
        os.system('python ~/.grungegirl/astrology/houses/secondhouse.py')

    elif query.lower() == 'second house':
        os.system('python ~/.grungegirl/astrology/houses/secondhouse.py')

    elif query.lower() == 'hs3':
        os.system('python ~/.grungegirl/astrology/houses/thirdhouse.py')

    elif query.lower() == 'the third house':
        os.system('python ~/.grungegirl/astrology/houses/thirdhouse.py')

    elif query.lower() == 'house three':
        os.system('python ~/.grungegirl/astrology/houses/thirdhouse.py')

    elif query.lower() == 'third house':
        os.system('python ~/.grungegirl/astrology/houses/thirdhouse.py')


    elif query.lower() == 'hs4':
        os.system('python ~/.grungegirl/astrology/houses/fourthhouse.py')

    elif query.lower() == 'the fourth house':
        os.system('python ~/.grungegirl/astrology/houses/fourthhouse.py')

    elif query.lower() == 'house four':
        os.system('python ~/.grungegirl/astrology/houses/fourthhouse.py')

    elif query.lower() == 'fourth house':
        os.system('python ~/.grungegirl/astrology/houses/fourthhouse.py')

    elif query.lower() == 'hs5':
        os.system('python ~/.grungegirl/astrology/houses/fifthhouse.py')

    elif query.lower() == 'the fifth house':
        os.system('python ~/.grungegirl/astrology/houses/fifthhouse.py')

    elif query.lower() == 'house five':
        os.system('python ~/.grungegirl/astrology/houses/fifthhouse.py')

    elif query.lower() == 'fifth house':
        os.system('python ~/.grungegirl/astrology/houses/fifthhouse.py')

    elif query.lower() == 'hs6':
        os.system('python ~/.grungegirl/astrology/houses/sixthhouse.py')

    elif query.lower() == 'the sixth house':
        os.system('python ~/.grungegirl/astrology/houses/sixthhouse.py')

    elif query.lower() == 'house six':
        os.system('python ~/.grungegirl/astrology/houses/sixthhouse.py')

    elif query.lower() == 'sixth house':
        os.system('python ~/.grungegirl/astrology/houses/sixthhouse.py')

    elif query.lower() == 'hs7':
        os.system('python ~/.grungegirl/astrology/houses/seventhhouse.py')

    elif query.lower() == 'the seventh house':
        os.system('python ~/.grungegirl/astrology/houses/seventhhouse.py')

    elif query.lower() == 'house seven':
        os.system('python ~/.grungegirl/astrology/houses/seventhhouse.py')

    elif query.lower() == 'seventh house':
        os.system('python ~/.grungegirl/astrology/houses/seventhhouse.py')

    elif query.lower() == 'hs8':
        os.system('python ~/.grungegirl/astrology/houses/eighthhouse.py')

    elif query.lower() == 'the eighth house':
        os.system('python ~/.grungegirl/astrology/houses/eighthhouse.py')

    elif query.lower() == 'house eight':
        os.system('python ~/.grungegirl/astrology/houses/eighthhouse.py')

    elif query.lower() == 'eighth house':
        os.system('python ~/.grungegirl/astrology/houses/eighthhouse.py')

    elif query.lower() == 'hs9':
        os.system('python ~/.grungegirl/astrology/houses/ninthhouse.py')

    elif query.lower() == 'the ninth house':
        os.system('python ~/.grungegirl/astrology/houses/ninthhouse.py')

    elif query.lower() == 'house nine':
        os.system('python ~/.grungegirl/astrology/houses/ninthhouse.py')

    elif query.lower() == 'ninth house':
        os.system('python ~/.grungegirl/astrology/houses/ninthhouse.py')

    elif query.lower() == 'hs10':
        os.system('python ~/.grungegirl/astrology/houses/tenthhouse.py')

    elif query.lower() == 'the tenth house':
        os.system('python ~/.grungegirl/astrology/houses/tenthhouse.py')

    elif query.lower() == 'house ten':
        os.system('python ~/.grungegirl/astrology/houses/tenthhouse.py')

    elif query.lower() == 'tenth house':
        os.system('python ~/.grungegirl/astrology/houses/tenthhouse.py')

    elif query.lower() == 'hs11':
        os.system('python ~/.grungegirl/astrology/houses/eleventhhouse.py')

    elif query.lower() == 'the elevnth house':
        os.system('python ~/.grungegirl/astrology/houses/eleventhhouse.py')

    elif query.lower() == 'house eleven':
        os.system('python ~/.grungegirl/astrology/houses/eleventhhouse.py')

    elif query.lower() == 'eleventh house':
        os.system('python ~/.grungegirl/astrology/houses/eleventhhouse.py')

    elif query.lower() == 'hs12':
        os.system('python ~/.grungegirl/astrology/houses/twelfthhouse.py')

    elif query.lower() == 'the twelfth house':
        os.system('python ~/.grungegirl/astrology/houses/twelfthhouse.py')

    elif query.lower() == 'house twelve':
        os.system('python ~/.grungegirl/astrology/houses/twelfthhouse.py')

    elif query.lower() == 'twelfth house':
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

# Asteroids

    elif query.lower() == 'lilith':
        os.system('python ~/.grungegirl/astrology/asteroids/lilith.py')

    elif query.lower() == 'chiron':
        os.system('python ~/.grungegirl/astrology/asteroids/chiron.py')

    elif query.lower() == 'pallas':
        os.system('python ~/.grungegirl/astrology/asteroids/pallas.py')

# Aspects

# ------------------------ Bi-Quintile

    elif query.lower() == 'bi-quintile':
        os.system('python ~/.grungegirl/astrology/aspects/bi-quin.py')

    elif query.lower() == 'biquintile':
        os.system('python ~/.grungegirl/astrology/aspects/bi-quin.py')

    elif query.lower() == 'biquin':
        os.system('python ~/.grungegirl/astrology/aspects/bi-quin.py')

    elif query.lower() == 'biq':
        os.system('python ~/.grungegirl/astrology/aspects/bi-quin.py')


# ------------------------ Conjunction

    elif query.lower() == 'conjunction':
        os.system('python ~/.grungegirl/astrology/aspects/conjunction.py')

    elif query.lower() == 'conj':
        os.system('python ~/.grungegirl/astrology/aspects/conjunction.py')

    elif query.lower() == 'conjunct':
        os.system('python ~/.grungegirl/astrology/aspects/conjunction.py')

    elif query.lower() == 'con':
        os.system('python ~/.grungegirl/astrology/aspects/conjunction.py')

# ------------------------ Opposition

    elif query.lower() == 'opposition':
        os.system('python ~/.grungegirl/astrology/aspects/opposition.py')

    elif query.lower() == 'opp':
        os.system('python ~/.grungegirl/astrology/aspects/opposition.py')

# ------------------------- Quincunx

    elif query.lower() == 'quincunx':
        os.system('python ~/.grungegirl/astrology/aspects/quincunx.py')

    elif query.lower() == 'inconjunct':
        os.system('python ~/.grungegirl/astrology/aspects/quincunx.py')

    elif query.lower() == 'inconjunction':
        os.system('python ~/.grungegirl/astrology/aspects/quincunx.py')

# ------------------------- Quintile

    elif query.lower() == 'quintile':
        os.system('python ~/.grungegirl/astrology/aspects/quintile.py')

    elif query.lower() == 'quint':
        os.system('python ~/.grungegirl/astrology/aspects/quintile.py')

    elif query.lower() == 'quin':
        os.system('python ~/.grungegirl/astrology/aspects/quintile.py')

    elif query.lower() == 'qui':
        os.system('python ~/.grungegirl/astrology/aspects/quintile.py')

# ------------------------- Semi-Quintile

    elif query.lower() == 'semqui':
        os.system('python ~/.grungegirl/astrology/aspects/sem-quin.py')

    elif query.lower() == 'sem-quin':
        os.system('python ~/.grungegirl/astrology/aspects/sem-quin.py')

    elif query.lower() == 'semquin':
        os.system('python ~/.grungegirl/astrology/aspects/sem-quin.py')

    elif query.lower() == 'semiquintile':
        os.system('python ~/.grungegirl/astrology/aspects/sem-quin.py')

    elif query.lower() == 'semi-quintile':
        os.system('python ~/.grungegirl/astrology/aspects/sem-quin.py')

    elif query.lower() == 'semiquin':
        os.system('python ~/.grungegirl/astrology/aspects/sem-quin.py')

    elif query.lower() == 'semi-quin':
        os.system('python ~/.grungegirl/astrology/aspects/sem-quin.py')

# ------------------------ Semi-Sextile

    elif query.lower() == 'semi-sextile':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sextile.py')

    elif query.lower() == 'semsex':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sextile.py')

    elif query.lower() == 'semi-sex':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sextile.py')

    elif query.lower() == 'semisex':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sextile.py')

    elif query.lower() == 'sem-sex':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sextile.py')

# ------------------------- Semi-Square

    elif query.lower() == 'semi-square':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sq.py')

    elif query.lower() == 'semisquare':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sq.py')

    elif query.lower() == 'semsq':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sq.py')

    elif query.lower() == 'semisq':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sq.py')

    elif query.lower() == 'sem-sq':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sq.py')

    elif query.lower() == 'semseq':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sq.py')

    elif query.lower() == 'sem-seq':
        os.system('python ~/.grungegirl/astrology/aspects/semi-sq.py')

# ------------------------- Sesquiquadrate

    elif query.lower() == 'sesquisquare':
        os.system('python ~/.grungegirl/astrology/aspects/sesquisq.py')

    elif query.lower() == 'sesquisq':
        os.system('python ~/.grungegirl/astrology/aspects/sesquisq.py')

    elif query.lower() == 'sesquiquadrate':
        os.system('python ~/.grungegirl/astrology/aspects/sesquisq.py')

    elif query.lower() == 'sesqui':
        os.system('python ~/.grungegirl/astrology/aspects/sesquisq.py')

    elif query.lower() == 'sesq':
        os.system('python ~/.grungegirl/astrology/aspects/sesquisq.py')

# ------------------------- Square

    elif query.lower() == 'square':
        os.system('python ~/.grungegirl/astrology/aspects/square.py')

    elif query.lower() == 'sqre':
        os.system('python ~/.grungegirl/astrology/aspects/square.py')

    elif query.lower() == 'sqr':
        os.system('python ~/.grungegirl/astrology/aspects/square.py')

    elif query.lower() == 'sq':
        os.system('python ~/.grungegirl/astrology/aspects/square.py')

# -------------------------- Trine

    elif query.lower() == 'trine':
        os.system('python ~/.grungegirl/astrology/aspects/trine.py')

    elif query.lower() == 'tri':
        os.system('python ~/.grungegirl/astrology/aspects/trine.py')

    elif query.lower() == 'tr':
        os.system('python ~/.grungegirl/astrology/aspects/trine.py')

# -------------------------- Septile

    elif query.lower() == 'septile':
        os.system('python ~/.grungegirl/astrology/aspects/septile.py')

    elif query.lower() == 'sep':
        os.system('python ~/.grungegirl/astrology/aspects/septile.py')

    elif query.lower() == 'sept':
        os.system('python ~/.grungegirl/astrology/aspects/septile.py')

    elif query.lower() == 'sp':
        os.system('python ~/.grungegirl/astrology/aspects/septile.py')

# --------------------------- Sextile

    elif query.lower() == 'sextile':
        os.system('python ~/.grungegirl/astrology/aspects/sextile.py')

    elif query.lower() == 'sex':
        print('lol you typed sex... wtf')
        os.system('python ~/.grungegirl/astrology/aspects/sextile.py')

    elif query.lower() == 'sext':
        os.system('python ~/.grungegirl/astrology/aspects/sextile.py')

    elif query.lower() == 'sx':
        os.system('python ~/.grungegirl/astrology/aspects/sextile.py')
# Exit

    elif query.lower() == 'exit':
        exit('closing strhckr.')

    elif query.lower() == 'c':
        exit('closing strhckr.')

    elif query.lower() == 'clear':
        os.system('clear')

    elif query.lower() == 'close':
        exit('closing strhckr.')

    elif query.lower() == 'w':
        os.system('python ~/.grungegirl/query.py')
        exit()

    elif query.lower() == 'a':
        os.system('python ~/.grungegirl/astrology.py')
        exit()

    elif query.lower() == 't':
        os.system('python ~/.grungegirl/tarot.py')
        exit()

    elif query.lower() == 'g':
        os.system('python ~/.grungegirl/main.py')
        exit()

astro()

os.system('python ~/.grungegirl/astrology.py')