class Privileegid():
    def __init__(self, privileegid):
        self.privileegid = []
        self.privileegid.append(privileegid)
    def naita_privileegid(self):
        print(self.privileegid)

class Admin():
    privileegid = "lubatud lisada kasutajad, lubatud eemaldada kasutajad, lubatud blokeerida kasutajad"
    def naita_privileegid(self):
        print(self.privileegid)

class Kasutaja():
    def __init__(self, e_nimi, p_nimi, vanus_1, mail):
        self.eesnimi = e_nimi
        self.perenimi = p_nimi
        self.vanus = vanus_1
        self.gmail = mail

    def kirjelda_kasutaja(self):
        print("Ees ja perenimi " + self.eesnimi + " " + self.perenimi)
        print("vanus " + self.vanus)
        print("E-mail " + self.gmail)

    def tervita_kasutaja(self):
        print("Tere tulemast " + self.eesnimi + "! ")