# d-f)
import random as rnd
import matplotlib.pyplot as plt

antal = 20
cirkelantal = 0
cirkelradie = 1

xutan=[]
yutan=[]

xinnan=[]
yinnan=[]
for i in range(antal):
    generatorx = rnd.uniform(-1,1)
    generatory = rnd.uniform(-1,1)
    x.append(generatorx)
    y.append(generatory)
    if generatorx**2 + generatory**2 <= cirkelradie:
        cirkelantal = cirkelantal + 1
        xinnan.append(generatorx)
        yinnan.append(generatory)
    else:
        xutan.append(generatorx)
        yutan.append(generatory)
    #print(f"punkt {i} är ({generatorx},{generatory})")

andelen = cirkelantal/antal
total = andelen*4

plt.ylim(-1,1)
plt.xlim(-1,1)
plt.axvline(0)
plt.axhline(0)
plt.plot(xutan,yutan,'*b')
plt.plot(xinnan,yinnan,'*r')

print(f"Punkter utanför - x {xutan}")
print(f"Punkter utanför - y {yutan}")

print(f"Punkter innanför - x {xinnan}")
print(f"Punkter innanför - y {yinnan}")




print(f"Antalet punkter i cirkeln är {cirkelantal}")
print(f"Andelen punkter som är i cirkeln är {andelen}")
print(f"Andelen multiplicerat med 4 blir {total}")
