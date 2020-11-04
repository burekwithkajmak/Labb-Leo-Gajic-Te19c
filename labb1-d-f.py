# d-f)
import random as rnd


#Antalet punker som ska simuleras
antal = 5000
#En start variabel som används för att skriva ut hur många punkter som ligger inom cirkeln.
cirkelantal = 0
#Radie för cirkeln
cirkelradie = 1

#En for sats som har variabeln "antal" där du kan skriva in hur många punkter som ska simuleras.
for i in range(antal):
    #Både generator variablerna generar ett värde mellan -1 och 1 på både x och y ledet. 
    generatorx = rnd.uniform(-1,1)
    generatory = rnd.uniform(-1,1)
    #Här kollar jag om punkten är <= cirkelns radie som är 1 och om punkten är det så innebär det att punkten är inom cirkeln.
    if generatorx**2 + generatory**2 <= cirkelradie:
        #Här lägger jag till +1 för varje gång som punkten som har simulerats är inom cirkeln.
        cirkelantal = cirkelantal + 1
    print(f"punkt {i} är ({generatorx},{generatory})")

#Här räknar jag ut andelen punkter som är innanför cirkeln.
andelen = cirkelantal/antal
#Här multiplicerar jag andelen punkter som är innanför cirkeln med 4 och får då ju mer punkter som simuleras ett värde som liknar π
total = andelen*4

#Tre stycken prints som skriver ut olika värden.
print(f"Antalet punkter i cirkeln är {cirkelantal}")
print(f"Andelen punkter som är i cirkeln är {andelen}")
print(f"Andelen multiplicerat med 4 blir {total}")
