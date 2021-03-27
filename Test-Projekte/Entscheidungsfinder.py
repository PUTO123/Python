import random

print("Willkommen im Entscheidungsfinder")

o1 = input("Option1: ")
o2 = input("Option2: ")
olist = [o1, o2]

result = random.choice(olist)

print(result)

input()