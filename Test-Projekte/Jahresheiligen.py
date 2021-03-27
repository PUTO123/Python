import random
print("Willkommen beim Jahresheiligen Generator")
v = ["Aaron, Bruder Mose", "Heilige Therese", "David, König Israels", "", "", "", "", "", ""]
def selectRandom(v):
  return random.choice(v)

print("The name selected is: ", selectRandom(v))

