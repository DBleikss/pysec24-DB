# Demonstrate use of Exception
print("Uzminēšu tavu vecumu.")
while True:
    try:
        datu_ievade = input("Ievadi savu vecumu:")
        vecums = int(datu_ievade)
        print("Tavs vecums ir", vecums, "gads/gadi!")
        break
    
    except: 
        print("Ievadi skaitli nevis burtus vai simbolus >:( ")