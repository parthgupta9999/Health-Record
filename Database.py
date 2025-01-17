from deta import Deta

DETA_KEY = "d0766v41og3_uQbENmdvfA1VsFN5RYF3mvWwpYmSKwnu"

deta = Deta(DETA_KEY)

db= deta.Base("demo")

def record(name,cur_med,ecg,rep):
    return db.put({"key":name, "cur_med":cur_med, "ecg":ecg, "rep":rep})

##name = "Premlata"
##cur_med = ["CertalBeta50 - 1 perday"]
##ecg = 'demo_ecg'
##rep = 'demo_ecg'

##record(name,cur_med,ecg,rep)

def getp(namee):
    return db.get(namee)

