from praks2.restoranvol3 import Restoraan
class Jaatisekiosk(Restoraan):
    jaatise_valik = ""
    def naita_jaatise_valik(self):
        print(self.jaatise_valik)