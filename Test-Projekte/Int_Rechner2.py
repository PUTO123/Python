while True:
    num1 = input("Gib die erste Zahl ein: ")
    oper = input("Welche Rechenoperation soll durchgeführt werden? (+,-,/,*): ")
    num2 = input("Gib die zweite Zahl ein: ")

    num1 = int(num1)
    num2 = int(num2)

    if (oper == "+"):
        print("Deine Rechnung:", num1, " + ", num2)
        print("Ergebnis:", num1 + num2)

    elif (oper == "-"):
        print("Deine Rechnung:", num1, " - ", num2)
        print("Ergebnis:", num1 - num2)

    elif (oper == "/"):
        print("Deine Rechnung:", num1, " / ", num2)
        print("Ergebnis:", num1 / num2)

    elif (oper == "*"):
        print("Deine Rechnung:", num1, " * ", num2)
        print("Dein Ergebnis:", num1 * num2)
    else:
        print("Deine Eingaben sind nicht gültig")

    jein = input("Willst du weiter rechnen? (Ja/Nein)")

    if jein == 'nein':
        break
