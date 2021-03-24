print("\033[31m")

v1 = "umbrella"
v2 = "sun"
v3 = "car"

points = 0
print("Willkommen im Vokabeltrainer")
print("Versuch soviele Punkte  wie möglich zu bekommen")

f1 = input("Wie lautet Regenschirm auf Englisch?:" )
if f1 == v1:
    print("Super Richtig")
    points = points + 1
    print("Du hast einen Punkt bekommen", points)

else:
    print("Falsch")

f2 = input("Wie lautet Sonne auf Englisch?:")
if f2 == v2:
    print("Super Richtig")
    points = points + 1
    print("Du hast einen Punkt bekommen", points)

else:
    print("Falsch")

f3 = input("Wie lautet Auto auf Englisch?: ")
if f3 == v3:
    print("Super Richtig")
    points = points + 1
    print("Du hast einen Punkt bekommen", points)

print("Danke fürs mitmachen. Deine Punktenzahl:", points) 
