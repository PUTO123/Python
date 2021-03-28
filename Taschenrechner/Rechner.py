
while True:
    print("----------------------------------------\nWillkommen im Taschenrechner\n----------------------------------------")
    print("Wähle deine Option: ")
    print("1) +")
    print("2) -")
    print("3) *")
    print("4) /")

    o = input("Wähle deine Rechenoperation: ")
    z1 = input("Deine erste Zahl: ")
    z2 = input("Deine zweite Zahl: ")
    
    def Grundrechnungsarten():
        if o == "1":
            try:
                z1 = int(z1)
                z2 = int(z2)
                print("Dein Ergebnis ist: ", z1 + z2) 
            except:
                z1 = float(z1)
                z2 = float(z2)
                print("Dein Ergebnis ist: ", z1 + z2)
                
        if o == "2":
            try:
                z1 = int(z1)
                z2 = int(z2)
                print("Dein Ergebnis ist: ", z1 - z2)

if __name__ == "__main__":
    Grundrechnungsarten()
    
w = input("Willst du weitermachen? Ja oder Nein:" )
if w == "Nein":
    break
