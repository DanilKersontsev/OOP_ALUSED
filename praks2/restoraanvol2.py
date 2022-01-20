class Restoraan():
    def __init__(self, res_nimi, s_tyyp):
        self.restoraani_nimi = res_nimi
        self.soogi_tyyp = s_tyyp

    def kirjelda_restoraan(self):
        print("Restoraan" + self.restoraani_nimi + " pakub" + self.soogi_tyyp)

    def ava_restoraan(self):
        print("Restoraan on avatud")
