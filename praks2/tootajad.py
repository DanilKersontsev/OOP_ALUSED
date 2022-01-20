class Inimene():
    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon = 1):
        self.ees_nimi = eesnimi
        self.pere_nimi = perenimi
        self.kutsekv = kutsekvalifikatsioon


    def __del__(self):
        print("Kõige head")

    def tutvustus(self):
        print("Tere, olen", self.ees_nimi, self.pere_nimi)