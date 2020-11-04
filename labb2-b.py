#En variabel som används för att lägga till +1 varje gång while satsen körs tills variabeln har nått värdet 100.
n = 0

#En while sats som körs tills variabeln n har nått värdet 100.
while n < 100:
    n = n + 1
    #En if sats som kontrollerar om n värdet inte är en multipel av 5 och skriver då ut variabeln n.
    if not n%5 == 0:
        print(n)
    #En elif sats som kontrollerar om n värdet är en multipel av 5 och skriver då ut stringen "Burr".
    elif n%5 == 0:
        print('Burr')
