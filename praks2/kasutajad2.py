from praks2.kasutaja2 import Kasutaja

kasutaja = Kasutaja("Danil", "Kersontsev", "17", "danil.kersontsev@voco.ee")

kasutaja.kirjelda_kasutaja()
kasutaja.tervita_kasutaja()


print(kasutaja.suurenda_sisselogimiskatsed(3))
kasutaja.suurenda_sisselogimiskatsed(6)
print("Olete sisseloginud", kasutaja.sisselogimiskatsed, "korda ")

kasutaja.reset_sisselogimiskatsed()
print(kasutaja.sisselogimiskatsed)
