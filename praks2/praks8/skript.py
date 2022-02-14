from moodul import *

print("Ruumi möötud: ")
pikkus = float(input("Pikkus: "))
laius = float(input("Laius: "))
korgus = float(input("Kõrgus: "))

ruum = Ruum(pikkus, laius, korgus)

vastus = input("Kas olemas aknda/uksed? jah/ei ")
while vastus == "jah":
    laius = float(input("Akna/ukse laius: "))
    korgus = float(input("Akna/ukse kõrgus: "))
    aknen_uks = Aknaduksed(laius, korgus)
    vastus = input("Kas on olemas aknad/uksed? jah/ei ")
print("Tapeedi rulli mõõtud: ")
tl = float(input("tapeedi rulli laius "))
tp = float(input("tapeedi rulli pikkus "))

print("Tapeedid on vaja kleepid " + str(Aknaduksed.toopind) + "ruutmeetrites" )
print("Tapeedi rullide arv " + str(Aknaduksed.tapeedid(tp, tl)))
