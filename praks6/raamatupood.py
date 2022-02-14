from praks6 import raamat
from praks6.raamat import Raamat

class Raamatupood():
    def __init__(self, nimi, reiting):
        self.nimi = nimi
        self.reiting = reiting


    raamatulist = []
    def saan_lisada_raamat(self,raamat):
        for raamatud in self.raamatulist:
            if raamat.auto == raamatud.autor:
                return False
            else:
                if raamat.pealkiri == raamatud.pealkiri:
                    return False
                else:
                    if raamat.reiting >= self.reiting:
                        return True
                    else:
                            return False

    def lisa_raamat(self, raamat):
        if self.saan_lisada_raamat(raamat) == True:
            self.raamatulist.append(raamat)
        elif self.saan_lisada_raamat(raamat) == False:
            print('Seda raamatud ei saa poodi lisada')

    def saan_eemaldada_raamat(self, raamat):
        for raamatud in self.raamatulist:
            if raamat.autor == raamatud.autor and raamat.pealkiri == raamatud.pealkiri:
                return True
            else:
                return False
    def eemalda_raamat(self):
        if self.saan_eemaldada_raamat(raamat) == True:
            self.raamatulist.remove(raamat)
            print('Raamat on eemaldatud')


    def naita_koik_raamatud(self):
        return self.raamatulist

    def naita_koige_populaarsem_raamat(self):
        if self.reiting >= self.raamatulist:
            print( self.nimi, "See raamat on kõige populaarsem")
    def naita_raamatud_hinna_jargi(self):
        if hind >= self.raamatulist:
            return self.hind
