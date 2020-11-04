#En variabel som används för att spara datan från input som användaren matar in. 
tal = int(input("Ange hur många tal som ska skrivas ut: "))
#En variabel som används för att spara datan från input som användaren matar in. 
burr = int(input("Ange multipel för burr: "))
#En variabel som används för att spara datan från input som användaren matar in. 
birr = int(input("Ange multipel för birr: "))
#En variabel som används för att lägga till +1 varje gång stringen "Burr" skrivs ut.
antalburr = 0
#En variabel som används för att lägga till +1 varje gång stringen "Birr" skrivs ut.
antalbirr = 0

#En variabel som lägger till +1 på det värdet man har matat in i inputen tal för att den ska räkna rätt i for satsen. 
omvandlare = tal + 1

#En for sats som körs från 1 till det tal som användaren har matat in i variabeln tal.
for i in range(1, omvandlare):
    #En if sats som kollar om i värdet är en multipel av variabeln burr och skriver då ut stringen "Burr" men också lägger till +1 på variabeln antalburr.
    if i%burr == 0:
        print("Burr") 
        antalburr = antalburr + 1
    #En if sats som kollar om i värdet är en multipel av variabeln birr och skriver då ut stringen "Birr" men också lägger till +1 på variabeln antalbirr.
    if i%birr == 0:
        print("Birr")
        antalbirr = antalbirr + 1
    #En if sats som kontrollerar om i värdet inte är en multipel av variabeln burr eller birr och skriver då ut variabeln i.
    if i%birr != 0 and i%burr != 0:
        print(i)
#En variabel som adderar antalet birr och burr.
total = antalburr + antalbirr

#Tre stycken prints där det skrivs ut olika värden. 
print(f"Antalet birr är {antalbirr}")
print(f"Antalet burr är {antalburr}")
print(f"Totala antalet birr och burr är {total}")

