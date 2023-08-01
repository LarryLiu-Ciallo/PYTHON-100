Cun1 = []
a1 = 1
while a1 < 5:
    Bai = a1 * 100
    Cun1.append(Bai)
    a1 = a1 + 1

a2 = 1
Cun2 = []
while a2 < 5:
    Shi = a2 * 10
    for x in Cun1:
        ErWei = x + Shi
        Cun2.append(ErWei)  
    a2 = a2 + 1

a3 = 1
Cun3 = []
while a3 < 5:
    Ge = a3
    for y in Cun2:
        GeWei = y + Ge
        Cun3.append(GeWei)
    a3 = a3 + 1

Cun3.sort()

L1 = []
for z in Cun3:
    c1 = z // 100
    c2 = z // 10 - c1 * 10
    c3 = z - c1 * 100 - c2 * 10
    if c1 == c2 or c1 == c3 or c2 == c3:
        pass
    else:
        L1.append(z)

Length = len(L1)
print(L1)



