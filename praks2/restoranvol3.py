from praks2.restoraanvol3 import Restoraan

res = Restoraan(" Kolm tilli", " suppi")
res.kirjelda_restoraan()
res.ava_restoraan()

res.m22ra_teenindatud_kylastajad(10)
print("Teenindatud ", res.teenindatud_kylastajad, "külalist")
res.suurenda_teenindatud_kylalise(10)
print("Päeva jooksul on teenindatud ", res.teenindatud_kylastajad, "külalist")
