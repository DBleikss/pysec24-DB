# Write a program that executes a long task and has implementation to catch “CRTL+C” and exit gracefully 
# (without throwing exception).
# Nesapratu, kas skaitās, kā "long task", bet izdomāju uztaisīt bezgalīgu while loop, kas katru sekundi izprintē paziņojumu
import time

def ilgais_uzd():
    try:    # Saprotu, ka te galvenais uzdevums parādīt, ka, izmantojot "try:" un "except:", tas iziet gracefully
        while True:
            print("Tikko palaidi garām 1 sekundi no savas dzīves..")
            time.sleep(1)
    except:
        print(" Labs darbs!")

ilgais_uzd()
