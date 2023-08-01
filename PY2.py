LiRun = int(input("how much:"))
Earn = 0
F1 = 0
F2 = 0
F3 = 0
F4 = 0
F5 = 0
F6 = 0

if LiRun >= 100000:
    F1 = 100000 * 0.1
    if LiRun >= 200000:
        F2 = (200000 - 100000) * 0.075
        if LiRun >= 400000:
            F3 = (400000 - 200000) * 0.05
            if LiRun >= 600000:
                F4 = (600000 - 400000) * 0.03
                if LiRun >= 1000000:
                    F5 = (1000000 - 600000) * 0.015
                    F6 = (LiRun - 1000000) * 0.01
                else:
                    F5 = (LiRun - 600000) * 0.015
            else:
                F4 = (LiRun - 400000) * 0.03
        else:
            F3 = (LiRun - 200000) * 0.05
    else:
        F2 = (LiRun - 100000) * 0.075
else:
    F1 = LiRun * 0.1

SuoDe = F1 + F2 + F3 + F4 + F5 + F6
print(SuoDe)