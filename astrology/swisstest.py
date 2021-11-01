import swisseph as swe

def swiss():

    swe.set_ephe_path('/usr/share/ephe')  # set path to ephemeris files
    now = swe.julday(2007, 3, 3)  # get Julian day number
    res = swe.lun_eclipse_when(now)  # find next lunar eclipse (from now on)
    ecltime = swe.revjul(res[1][0])  # get date UTC
    ecltime()
    jd = swe.julday(2008, 3, 21)
    swe.calc_ut(jd, swe.AST_OFFSET + 13681)[0]  # asteroid Monty Python
    help(swe)


swiss()