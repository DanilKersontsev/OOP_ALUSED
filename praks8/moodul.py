class Ruum():
    def __init__(self, pikkus, laius, korgus):
        self.pikkus = pikkus
        self.laius = laius
        self.korgus = korgus
        self.aknad_uksed = []

class Aknaduksed():
    def __init__(self, laius, korgus):
        self.pindala = laius * korgus
    def Lisaken_uks(self, laius, korgus):
        self.aknad_uksed.append(Aknaduksed(laius, korgus))
    def taispind(self):
        return 2 + self.korgus * (self.pikkus + self.laius)
    def toopind(self):
        uus_pindala = self.taispind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
            return uus_pindala
    def tapeedid(self, tp, tl):
        return int(self.toopind() / (tp * tl))