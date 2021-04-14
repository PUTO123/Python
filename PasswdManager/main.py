print("Willkommen im Passwort-Manager")
print("""
Was willst du tun?
1) Eintrag erstellen
""")
AuswahlOption = input("Deine Wahl:" )
def EintrageErstellen:
	if AuswahlOption == "1":
		open("Database.kbdx", "c")