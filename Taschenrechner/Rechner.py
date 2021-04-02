while True:
    print("----------------------------------------\nWillkommen im Taschenrechner\n----------------------------------------")
    print("Wähle deine Option: ")
    print("1) Addieren")
    print("2) Subtrahieren")
    print("3) Multiplizieren")
    print("4) Dividieren")

    o = input("Wähle deine Rechenoperation: ")

    def Grundrechnungsarten():
        if o == "1":
            try:
                z1 = input("Deine erste Zahl: ")
                z2 = input("Deine zweite Zahl: ")
                z1 = int(z1)
                z2 = int(z2)
                print("Dein Ergebnis ist: ", z1 + z2)
            except:
                z1 = input("Deine erste Zahl: ")
                z2 = input("Deine zweite Zahl: ")
                z1 = float(z1)
                z2 = float(z2)
                print("Dein Ergebnis ist: ", z1 + z2)

        if o == "2":
            try:
                z1 = input("Deine erste Zahl: ")
                z2 = input("Deine zweite Zahl: ")
                z1 = int(z1)
                z2 = int(z2)
                print("Dein Ergebnis ist: ", z1 - z2)
            except:
                z1 = input("Deine erste Zahl: ")
                z2 = input("Deine zweite Zahl: ")
                z1 = float(z1)
                z2 = float(z2)
                print("Dein Ergebnis ist: ", z1 - z2)
            
        if o == "3":
            try:
                z1 = input("Deine erste Zahl: ")
                z2 = input("Deine zweite Zahl: ")
                z1 = int(z1)
                z2 = int(z2)
                print("Dein Ergebnis ist: ", z1 * z2)
            except:
                z1 = input("Deine erste Zahl: ")
                z2 = input("Deine zweite Zahl: ")
                z1 = float(z1)
                z2 = float(z2)
                print("Dein Ergebnis ist: ", z1 * z2)

        if o == "4":
            try:
                z1 = input("Deine erste Zahl: ")
                z2 = input("Deine zweite Zahl: ")
                z1 = int(z1)
                z2 = int(z2)
                print("Dein Ergebnis ist: ", z1 / z2)
            except:
                z1 = input("Deine erste Zahl: ")
                z2 = input("Deine zweite Zahl: ")
                z1 = float(z1)
                z2 = float(z2)
                print("Dein Ergebnis ist: ", z1 / z2)

    if __name__ == "__main__":
        Grundrechnungsarten()

    w = input("Willst du weitermachen? Ja/Nein: ")
    if w == "Nein":
        break