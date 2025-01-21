# Explore Python Threading module
# Create a meaningful example demonstrating use of the mentioned module
# Paņēmu kodu no 8.uzd un to pārmainīju. 
# Galvenā doma, ko cenšos izveidot - uztaisīt monitoringu, kas paralēli, veicot threading, skatās gan syslog failu gan auth.log failu
import threading
import time

def funkc(log_cels, vards): # vards ir vārds, kas jāmeklē (šoreiz norādīju error)
    with open(log_cels, "r") as fails:   # Atver failu tikai in read-only veidā
        for rinda in fails:              # For loop, kas failā iet pa rindām
            if vards in rinda:             # Ja ir error vārds rindā, to rindu izprintē zinojumi.txt failā
#                print(rinda)
                with open("zinojumi.txt", "a") as out_file:  # Atver zinojumi.txt
                    out_file.write(rinda)   # Rindu izprintē zinojumi.txt failā


def monitorings():
    while True:
        # Uztaisu abus threadus, kas izmantos "funkc" funkciju un norādu argumentus
        syslog = threading.Thread(target=funkc, args=("/var/log/syslog", "error"))
        authlog = threading.Thread(target=funkc, args=("/var/log/auth.log", "error"))

        # Sāk threadus
        syslog.start()
        authlog.start()

        # Gaida, kad abi threadi pabeigs darbību
        syslog.join()
        authlog.join()

        # Gaida 1 minūti un atkal atkārto monitoringa funkciju
        time.sleep(60)

monitorings() # Funkcija, kas sāk monitoringu
