# Šis tiek izpildīts Linux virtuālajā mašīnā

def funkc(log_cels, USB):
    with open(log_cels, "r") as fails:  # Atver failu tikai in read-only veidā
        for rinda in fails:     # For loop, kas failā iet pa rindām
            if USB in rinda:    # Ja ir USB vārds rindā, to rindu izprintē
                print(rinda)

funkc("/var/log/syslog", "USB") # Izpilda funkciju