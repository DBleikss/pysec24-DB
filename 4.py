# Demonstrate use of all types of loops in Python

# --- While Loop ---
# Kamēr noteiktais ir True, tikmēr notiks While loop
i = 1
print("Mācāmies skaitīt:")
while i <= 3:
  print(i)
  i += 1
else:
  print("Vairs nezinu, kas ir aiz 3 :(") 


# --- For Loop ---
# For loop tiek izmantots priekš List, Tuple, Dictionary, Set un String
# Paņēmu no 3.uzd
nedela = ["pirmdiena", "otrdiena", "tresdiena", "ceturtdiena", "piektdiena", "sestdiena", "svetdiena"]
print("Dienas nedēļā:")
for i in nedela:
  print(i)
else:
  print("Aii, atkal pirmdiena!") 


# --- Range Loop  ---
print("Mācāmies desmitus:")
for i in range(10, 100, 10):
  print(i)
else:
  print("Pietiks desmitu.") 