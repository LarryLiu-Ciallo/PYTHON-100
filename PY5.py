X = int(input("number A = "))
Y = int(input("number B = "))
Z = int(input("number C = "))

A1 = 0
A2 = 0
if X >= Y:
    A1 = Y
    A2 = X
else:
    A1 = X
    A2 = Y

B1 = 0
B2 = 0
if A2 >= Z:
    B1 = Z
    B2 = A2
else:
    B1 = A2
    B2 = Z

C1 = 0
C2 = 0
if A1 >= B1:
    C1 = B1
    C2 = A1
else:
    C1 = A1
    C2 = B1

L1 = [C1,C2,B2]
L = [X,Y,Z]
print(L)
L2 = sorted(L)
print(L2)
print(L1)
