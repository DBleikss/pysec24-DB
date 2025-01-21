# Demonstrate use of the following Python data types
# Ņēmu iedvesmu no w3schools

# --- List ---
# Listi uzkrāj vertības secīgi, kuras var izmainīt. Tas atļauj duplikātus
# Izveidoju listu
nedela = ["pirmdiena", "otrdiena", "tresdiena", "ceturtdiena", "piektdiena", "sestdiena"]
print("Izveidoju listu")
print(nedela)

# Iegūstu un izprintēju darbadienas
darbadienas = nedela[0:5]
print("Iegūstu un izprintēju darbadienas")
print(darbadienas)

# Pievienoju svētdienu
nedela.append("svetdiena")
print("Pievienoju svētdienu un izprintēju listu")
print(nedela)


# --- Dictionary ---
# Dictionaries uzkrāj info izmantojot atslēgu pārus
# Izveidoju dictionary
students = {
        "vards": "Anna",
        "uzvards": "Panna",
        "pers_kods": "111111-22222"
    }
# Iegūstu studenta vārdu 
print("Studenta vārds:")
vards = students.get("vards")
print(vards)

# Nomainu Annas personas kodu
students["pers_kods"] = "222222-33333"
print("Studenta informācija:")
print(students)



# --- Set ---
# Iestatu Set-ā gadalaikus. Te galvenā atšķirība - ja kāds elements atkārtojas, to neizprintēs un to secība nav secīga
gadalaiki1 = {"ziema", "rudens", "rudens", "rudens"}
teksts1 = "Pirmā Set-a gadalaiki:"
print(teksts1, gadalaiki1)

# Izveidoju jaunu Set-u un pievienoju vasaru
gadalaiki2 = {"pavasaris"}
gadalaiki2.add("vasara")
teksts2 = "Otrā Set-a gadalaiki:"
print(teksts2, gadalaiki2)

# Tagad apvienoju abus Set-us
gadalaiki = gadalaiki1.union(gadalaiki2)
teksts = "Visi gadalaiki:"
print(teksts, gadalaiki)


# --- Tuple ---
# Te galvenā atšķirība, ka vērtības in Tuple var atkārtoties un to secība nemainās
ierices = ("telefons", "dators", "TV", "telefons", "dators")
teksts3 = ("Visas ierīces mājās:")
print(teksts3, ierices)

# Iegūstu no Tuple pirmo ierīci
teksts4 = ("Pirmā ierīce:")
print(teksts4, ierices[0])

# Saplīsa 2.dators :(
ierices = ierices[:-1]
print(teksts3, ierices)