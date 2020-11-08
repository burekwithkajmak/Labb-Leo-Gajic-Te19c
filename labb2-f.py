"""
uppgift f - Detta är en utvecklad version utav uppgift e där man har mycket fler möjligheter.

1. Man väljer ett startintervall och slutintervall
2. Därefter anger man hur många multiplar man vill skapa
3. Därefter anger man vilka multiplar de ska vara och vad som ska skrivas ut vid varje multipel
4. Sedan skrivs allt ut och även antalet utav alla mutliplar som du har angivit.
"""

#En variabel som används för att spara datan från input som användaren matar in.
startintervall = int(input("Ange startintervall: "))
#En variabel som används för att spara datan från input som användaren matar in.
slutintervall = int(input("Ange slutintervall: "))
#En variabel som lägger till +1 på det värdet man har matat in i inputen slutintervall för att den ska räkna rätt i for satsen. 
omvandlare = slutintervall + 1
#En variabel som används för att spara datan från input som användaren matar in.
multiplar = int(input("Ange hur många multiplar du vill skapa: "))
#En variabel som jag använder för att spara en lista.
multipel = []
#En variabel som jag använder för att spara en lista.
string = []
#En variabel som jag använder för att spara en lista.
antalstring = []

#En for sats som kör så många gånger du har matat in i variabeln multiplar.
for g in range(multiplar):
    #Här lägger jag till +1 på g för att den ska börja räkna från 1 och inte 0.
    g = g + 1
    #En variabel som används för att spara datan från input som användaren matar in.
    multipelinput = float(input(f"Ange multipel för multipel nr {g}: "))
    #En variabel som används för att spara datan från input som användaren matar in.
    multipelstring = input(f"Ange vad som ska skrivas vid multipel {multipelinput:.0f}: ")
    #Här appendar jag värderna från variabeln multipelinput på listan multipel.
    multipel.append(multipelinput)
    #Här appendar jag värderna från variabeln multipelstring på listan string.
    string.append(multipelstring)

#En for sats som körs från 1 till det tal som användaren har matat in i variabeln slutintervall.
for i in range(startintervall,omvandlare):
    #En if sats som kör igenom listan multipel och kollar om talet i inte är en multipel utav någon av multiplarna som finns i listan och printar då i. 
    if all([i%z!=0 for z in multipel]):
        print(i)
    #En for sats som kör igenom både multipel och string listan.
    for (x,y) in zip(multipel,string):
        #En if sats som kollar om talet i är en multipel av någon av multiplarna i listan och skriver då ut stringen till den multipeln.
        if i%x ==0:
            print(y)
            #Här appendar jag alla strings till en lista för att sedan kunna räkna antalet utav alla strings.
            antalstring.append(y)

#Här skapar jag en tom dict som jag sedan använder för att skriva ut antalet strings utav olika multiplar.
antal = {}

#En fors sats som kollar variabeln antalstring.
for q in set(antalstring):
    #Här räknar antalet strings utav olika multiplar som sedan skrivs ut separat.
    antal[q] = antalstring.count(q)
    #Här printar jag ut dicten antal och får då ut hur många mutliplar som har skrivits ut utav varje. 
print(f"Totala antalet utav utskrivningar är {antal}")



