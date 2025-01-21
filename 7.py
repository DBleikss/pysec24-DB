# Explore the use of modules and demonstrate with example
import random

print("Vai tev ir ko darīt?")
ievade = input("Ievadi 0, ja tev nav ko darīt, bet 1, ja tev ir: ")
saraksts = ["mācīties", "gulēt", "priecāties", "strādāt", "paēst", "padzerties", "uzmest kūleni", "padziedi", "paklausīties mūziku"]

if ievade == "0":
    print("Nu tad ej", random.choice(saraksts))
elif ievade == "1":
    print("Nu tad dari to.")
else:
    print("Aj, aj, aj. Neievadīji prasīto..")