class Restoraan():
    def __init__(self, res_nimi, s_tyyp):
        self.restoraani_nimi = res_nimi
        self.soogi_tyyp = s_tyyp

    teenindatud_kylastajad = 0

    def m22ra_teenindatud_kylastajad(self, kulaliste_arv):
         self.teenindatud_kylastajad = kulaliste_arv



    def suurenda_teenindatud_kylalise(self, suurenda_kulaliste_arv):
        self.teenindatud_kylastajad += suurenda_kulaliste_arv

    def kirjelda_restoraan(self):
        print("Restoraan" + self.restoraani_nimi + " pakub" + self.soogi_tyyp)

    def ava_restoraan(self):
        print("Restoraan on avatud")