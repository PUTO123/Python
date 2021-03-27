import random
print("Willkommen im 6 aus 45 - Lotto Generator")


def Gen():
    for i in range(0,7):
        print(random.randint(0,45))
Gen()

v = input("Willst du einen neuen Versuch? Ja/Nein: ")

while True:
    if v == "Ja":
        Gen()
        exit()
    elif v == "Nein":
        exit()
