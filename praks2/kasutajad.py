class Kasutaja():
    eesnimi = ""
    perenimi = ""
    vanus = ""
    mail = ""



    def kirjelda_kasutaja(self):
        print("Ees ja perenimi " + self.eesnimi + " " + self.perenimi)
        print("vanus " + self.vanus)
        print("E-mail " + self.mail)

    def tervita_kasutaja(self):
        print("Tere tulemast " + self.eesnimi + "!")
