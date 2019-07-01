import datetime

maanden = ["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december"]
dagen = ["zondag","maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag"]

# datetime-object naar leesbare tekst
def datumobjectnaartekst(datumobj):
    maand = maanden[int(datumobj.strftime("%m")) -1] #-1 omdat een list bij 0 begint en maanden bij 1
    dag = int(datumobj.strftime("%d"))
    weekdag = dagen[int(datumobj.strftime("%w"))]
    return "{} {} {}".format(weekdag, dag, maand)

# lijst naar leesbare tekst
def lijstnaartekst(woorden):
    if len(woorden) == 1:
        return woorden[0]
    return "{} en {}".format(", ".join(woorden[:-1]),  woorden[-1])
    
# datetime object naar string
def datumobjectnaarstring(datumobj, met_tijd = False):
    if met_tijd:
        date_time = datumobj.strftime("%Y-%m-%d, %H:%M:%S")
    else:
        date_time = datumobj.strftime("%Y-%m-%d")
    return date_time

# zet string om in datetime-object 
def stringnaardatumobject(datumobj):
    try:
        return datetime.datetime.strptime(datumobj, '%Y-%m-%d')
    except:
        return None