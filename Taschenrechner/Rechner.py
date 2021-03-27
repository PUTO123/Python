import math
while True:
    print("----------------------------------------\nWillkommen im Taschenrechner\n----------------------------------------")
    print("Wähle deine Option: ")
    print("1) +")
    print("2) -")
    print("3) *")
    print("4) /")

    o = input("Wähle deine Rechenoperation: ")

    def Grundrechnungsarten():
        if o == "1":
            z1a = input("Deine erste Zahl: ")
            z2a = input("Deine zweite Zahl: ")
            try:
                z1a = int(z1a)
                z2a = int(z2a)
                print("Dein Ergebnis ist:", z1a + z2a)
            except:
                z1a = float(z1a)
                z2a = float(z2a)
                print("Dein Ergebnis ist:", z1a + z2a)


        if o == "2":
            z1s = input("Deine erste Zahl: ")
            z2s = input("Deine zweite Zahl: ")
            try:
                z1s = int(z1s)
                z2s = int(z2s)
                print("Dein Ergebnis ist:", z1s - z2s)
            except:
                z1s = float(z1s)
                z2s = float(z2s)
                print("Dein Ergebnis ist:", z1s - z2s)


        if o == "3":
            z1m = input("Deine erste Zahl: ")
            z2m = input("Deine zweite Zahl: ")
            try:
                z1m = int(z1m)
                z2m = int(z2m)
                print("Dein Ergebnis ist:", z1m * z2m)
            except:
                z1m = float(z1m)
                z2m = float(z2m)
                print("Dein Ergebnis ist:", z1m * z2m)


        if o == "4":
            z1d = input("Deine erste Zahl: ")
            z2d = input("Deine zweite Zahl: ")
            try:
                z1d = int(z1d)
                z2d = int(z2d)
                print("Dein Ergebnis ist:", z1d / z2d)
            except:
                z1d = float(z1d)
                z2d = float(z2d)
                print("Dein Ergebnis ist: ", z1d / z2d)
            
        
if __name__ == "__main__":
    Grundrechnungsarten()
    
w = input("Willst du weitermachen? Ja oder Nein: ")

if w == "Nein":
    exit()

input()
