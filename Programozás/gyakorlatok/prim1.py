import math

def prim_e(n):
    ez_bizony_prim = True
    for osztó in range(2,math.floor(math.sqrt(n))+1):
        if n%osztó == 0:
            ez_bizony_prim = False
    return ez_bizony_prim
print("### PRÍMSZÁM MEGMONDÓ ###\n")
szám = int(input("Adj meg egy számot! "))
if prim_e(szám):
    print("Ez prímszám.")
else:
    print("Ez nem prím.")
print("\nPrímszám listázó")
meddig = int(input("Meddig írjam ki a prímszámokat? "))
print("For ciklussal")
számok = []
for n in range(2, meddig+1):
    if prim_e(n):
        számok.append(str(n))
print(", ".join(számok))
print()
print("While ciklussal")
számok = list()
n = 2
while n <= meddig:
    if prim_e(n):
        számok.append(str(n))
    n += 1
print(", ".join(számok))
