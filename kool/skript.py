from moodul import *

teemad = Andmed("Klass", "objekt", "pärilus", "polümorfism", "kapseldus")
anna = Opetaja()
kadi = Opilane()
mati = Opilane()


kadi.opib(teemad[3])
kadi.opib(teemad[1])
mati.opib(teemad[3])

kadi.unustada()