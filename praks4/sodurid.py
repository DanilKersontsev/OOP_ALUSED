from random import randint

from praks4.sodur import Sodur

armee1 = []
armee2 = []
armee1_id = []
armee2_id = []


for a in range(1, 21):
    armee_va: int = randint(1, 2)
    if armee_va == 1:
        armee1.append(Sodur(armee_va))
    else:
        armee2.append(Sodur(armee_va))
for sodur in armee1:
    armee1_id.append(sodur.id)
for sodur in armee2:
    armee2_id.append(sodur.id)

print("1. armees on sõdurid id-ga " + str(armee1_id))
print("2. armees on sõdurid id-ga" + str(armee2_id))
