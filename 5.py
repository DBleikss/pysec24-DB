# Demonstrate a use of Class in Python with a few methods
# Tips for ideas:
# A Person (Teacher)
class Person:
    def __init__(self, vards, uzvards, pasniedz):
        self.vards = vards
        self.uzvards = uzvards
        self.pasniedz = pasniedz

    def pilns(self):
        print("Skolotājs/a " + self.vards + " " + self.uzvards + " māca " + self.pasniedz)

Teacher = Person("Anna", "Panna", "Matemātika")
Teacher.pilns()


# Vehicle (Car, Bike)
class Vehicle:
    def __init__(self, firma, nosaukums):
        self.firma = firma
        self.nosaukums = nosaukums

    def bez_gada(self):
        print("Firma:", self.firma, "Nosaukums:", self.nosaukums)

class Car(Vehicle):
    def __init__(self, firma, nosaukums, izlaisanas_gads):
        super().__init__(firma, nosaukums)
        self.izlaisanas_gads = izlaisanas_gads

    def viss_info(self):
        print("Firma:", self.firma, "Nosaukums:", self.nosaukums, "Izlaišanas gads:", self.izlaisanas_gads)
            
class Bike(Vehicle):
    def __init__(self, firma, nosaukums, cena):
        super().__init__(firma, nosaukums)
        self.cena = cena

    def viss_info(self):
        print("Firma:", self.firma, "Nosaukums:", self.nosaukums, "Cena:", self.cena)

Masina1 = Car("Audi", "A4", 2000)
Masina1.bez_gada()
Masina1.viss_info()

Velosipeds1 = Bike("Tout Terrain", "TANAMI ", 500)
Velosipeds1.viss_info()


# Calculator (Simple, Scientific)
# Simple 
import math
class Calculator:
    def __init__(self, arg1, arg2):
        self.a = arg1
        self.b = arg2

class Simple(Calculator):
    def saskaitisana(self):
        return self.a + self.b
        
    def atnemsana(self):
        return self.a - self.b
        
    def reizinasana(self):
        return self.a * self.b
        
    def dalisana(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Ar 0 nevar dalīt! Aj, aj, aj. Nē, nu varēt jau var, bet nebūs rezultāts."

# Scientific
class Scientific(Calculator):
    def kvadrats(self):
        return self.a ** self.b
    
    def kvadratsakne(self):
        if self.b >= 0:
            return math.sqrt(self.b)
        else:
            return "No negatīva numura nevar izvilkt kvadrātsakni! >:("
    
    def sinuss(self):
        return math.sin(math.radians(self.b))
    
    def cosinuss(self):
        return math.cos(math.radians(self.b))
    
    def tangens(self):
        return math.tan(math.radians(self.b))
        
Atbilde1 = Simple(5, 2)
print(Atbilde1.saskaitisana())
print(Atbilde1.atnemsana())
print(Atbilde1.reizinasana())
print(Atbilde1.dalisana())

print("Gudrā kalkulatora atbildes:")
Atbilde2 = Scientific(2, 3)
print("Pakāpju atbilde:", Atbilde2.kvadrats())

Atbilde3 = Scientific(2, 3)
print("Kvadrātsaknes atbilde:", Atbilde3.kvadratsakne())

Atbilde4 = Scientific(0, 30)
print("Sīnusa atbilde:", Atbilde4.sinuss())
print("Kosinusa atbilde:", Atbilde4.cosinuss())
print("Tangensa atbilde:", Atbilde4.tangens())


