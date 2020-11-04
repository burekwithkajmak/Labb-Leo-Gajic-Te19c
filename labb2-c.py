#En variabel som används för att lägga till +1 varje gång while satsen körs tills variabeln har nått värdet 100.
n = 0
#En variabel som används för att spara datan från input som användaren matar in. 
burr = float(input("Mata in en multipel som kommer vara burr: "))

#En while sats som körs tills variabeln n har nått värdet 100.
while n < 100:
    n = n + 1
    #En if sats som kontrollerar om n värdet inte är en multipel av variabeln burr och skriver då ut variabeln n.
    if not n%burr == 0:
        print(n)
    #En elif sats som kontrollerar om n värdet är en multipel av variabeln burr och skriver då ut stringen "Burr".
    elif n%burr == 0:
        print('Burr')
