import random
from RandomWordGenerator import RandomWord
rw = RandomWord(max_word_size=5)


print("Willkommen im Passwort - Generator")
print("Dein Passwort ist: ")

class Generator:
      def Z1(self):
            print(random.randint(0,999))
      def B2(self):
            print(rw.generate())
      def Z3(self):
            print(random.randint(0,50))
      def B4(self):
            print(rw.generate())


GV = Generator()
Generator.Z1(1)
Generator.B2(1)
Generator.Z3(1)
Generator.B4(1)

input()