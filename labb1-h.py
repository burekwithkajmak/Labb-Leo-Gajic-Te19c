# h) - dokumenteringen finns länst ner
import random as rnd
import matplotlib.pyplot as plt

#Antalet punker som ska simuleras
antal = 200000
#En start variabel som används för att skriva ut hur många punkter som ligger inom cirkeln.
cirkelantal = 0
#Radie för cirkeln
cirkelradie = 0.7

#En variabel där jag sparar en list med alla x-kordinater som ligger utanför cirkeln
xutan=[]
#En variabel där jag sparar en list med alla y-kordinater som ligger utanför cirkeln
yutan=[]

#En variabel där jag sparar en list med alla x-kordinater som ligger innanför cirkeln
xinnan=[]
#En variabel där jag sparar en list med alla y-kordinater som ligger innanför cirkeln
yinnan=[]

#En for sats som har variabeln "antal" där du kan skriva in hur många punkter som ska simuleras.
for i in range(antal):
  #Både generator variablerna generar ett värde mellan -1 och 1 på både x och y ledet. 
    generatorx = rnd.uniform(-1,1)
    generatory = rnd.uniform(-1,1)
    #Här kollar jag om punkten är <= cirkelns radie som är 1 och om punkten är det så innebär det att punkten är inom cirkeln.
    if generatorx**2 + generatory**2 <= cirkelradie:
      #Här lägger jag till +1 på cirkelantal variablen för varje gång som punkten som har simulerats är inom cirkeln.
        cirkelantal = cirkelantal + 1
        #Här appendar jag kordinaterna till x och y variablerna som ligger innanför cirkeln och de sparas i form av en lista.
        xinnan.append(generatorx)
        yinnan.append(generatory)
    else:
        #Här appendar jag kordinaterna till x och y som variablerna som ligger utanför cirkeln och de sparas i form av en lista
        xutan.append(generatorx)
        yutan.append(generatory)
    #print(f"punkt {i} är ({generatorx},{generatory})")

#Här räknar jag ut andelen punkter som är innanför cirkeln.
andelen = cirkelantal/antal
#Här multiplicerar jag andelen punkter som är innanför cirkeln med 4 och får då ju mer punkter som simuleras ett värde som liknar π
total = andelen*4

#Här definerar jag maximala y värde på grafen
plt.ylim(-1,1)
#Här definerar jag maximala x värde på grafen
plt.xlim(-1,1)
#Här skapar jag punkterna på grafen som ligger utanför cirkeln med färgen blå
plt.plot(xutan,yutan,'*b')
#Här skapar jag punkterna på grafen som ligger innanför cirkeln med färgen röd
plt.plot(xinnan,yinnan,'*r')
#Här ritar jag upp axlarna till grafen.
plt.axvline(0)
plt.axhline(0)

#Detta användes bara för att se om alla värden appendas rätt till listorna
#print(f"Punkter utanför - x {xutan}")
#print(f"Punkter utanför - y {yutan}")

#print(f"Punkter innanför - x {xinnan}")
#print(f"Punkter innanför - y {yinnan}")


#Här skriver jag ut olika värden
print(f"Antalet punkter i cirkeln är {cirkelantal}")
print(f"Andelen punkter som är i cirkeln är {andelen}")
print(f"Andelen multiplicerat med 4 blir {total}")


#Dokumentering
#Jag har testat med olika radier och den enda skillnaden är att cirkeln antingen skalenligt ökar eller minskar beroende på om man öka eller minskar radien.
#Jag har även testat att minska och höja simuleringen utav punkter och skillnaden blir att cirkeln antingen blir mer fylld eller mer gles beroende på om man ökar eller minskar antal simuleringar. 
