#En variabel som används för att spara datan från input som användaren matar in. 
burr = int(input("Ange multipel för burr: "))
#En variabel som används för att spara datan från input som användaren matar in. 
birr = int(input("Ange multipel för birr: "))

#En for sats som körs från 1-100
for i in range(1, 101):
    #En if sats som kontrollerar om i värdet är en multipel av variabeln burr och skriver då ut stringen "Burr".
    if i%burr == 0:
        print("Burr") 
    #En if sats som kontrollerar om i värdet är en multipel av variabeln birr och skriver då ut stringen "Birr".
    if i%birr == 0:
        print("Birr")
    #En if sats som kontrollerar om i värdet inte är en multipel av variabeln burr eller birr och skriver då ut variabeln i.
    if i%birr != 0 and i%burr != 0:
        print(i)


