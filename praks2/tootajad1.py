from praks2.tootajad import Inimene

tootaja1 = Inimene("Danil", "Kersontsev", 9)
tootaja1.tutvustus()

tootaja2 = Inimene("Gervin", "Luide", 4)
tootaja2.tutvustus()

tootaja3 = Inimene("Viktor", "Lumiste", 6)
tootaja3.tutvustus()

if tootaja1.kutsekv < tootaja2.kutsekv and tootaja1.kutsekv < tootaja3.kutsekv:
    print(tootaja1.ees_nimi, tootaja1.pere_nimi, "Olete vallandatud")
    del tootaja1
elif tootaja2.kutsekv < tootaja1.kutsekv and tootaja2.kutsekv < tootaja3.kutsekv:
    print(tootaja2.ees_nimi, tootaja2.pere_nimi, "Olete vallandatud")
    del tootaja2
elif tootaja3.kutsekv < tootaja2.kutsekv and tootaja3.kutsekv < tootaja1.kutsekv:
    print(tootaja3.ees_nimi, tootaja3.pere_nimi, "Olete vallandatud")
    del tootaja3

input()
