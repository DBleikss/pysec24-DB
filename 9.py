# Create a program which can recursively traverse directories and print the file listing in a hierarchical way
# For any given filename list out all the stats related to the file such as size, creation time, etc..

import os
import time

def faila_info(faila_atr_vieta):  # Funkcija, kas nolasa un izprintē faila info

    faila_statuss = os.stat(faila_atr_vieta) # Iegūst visus faila statusus kā objektu

    izmers = faila_statuss.st_size # No visiem faila statusiem izvelku izmeru
    print("Izmers:", izmers, "bytes")

    laiks = time.ctime(faila_statuss.st_ctime)  # No visiem faila statusiem izvelku laiku
    print("Izveides laiks:", laiks)


def galvena_funkc(mapes_atr_vieta, hierarhija=""): # Funkcija kas pārbauda mapes. Hierarhija piefiksē, cik dziļi atrodas mapē
    print(hierarhija, os.path.basename(mapes_atr_vieta)) # Izprintē mapi, kurā atrodas (Norādīju, funkcijā, lai atver A mapi un tur sāk darbu)

    mapju_un_failu_saraksts = sorted(os.listdir(mapes_atr_vieta)) # Prezentācijā "Listing files and their information", bet iestatu, lai to dara alfabētiski ar sorted()
    for mape_vai_fails in mapju_un_failu_saraksts:  # Cikls, kas pārbauda vai mapē ir faili
        pilnais_cels = os.path.join(mapes_atr_vieta, mape_vai_fails) # Izveido pilnu ceļu mapei vai failam
        if os.path.isfile(pilnais_cels):  # Pārbauda vai tas ir fails
            print(hierarhija, "----", mape_vai_fails) # Ja mapē ir fails, to izprintē
            faila_info(pilnais_cels)  # Izmanto faila_info() funkciju un nolasa, izprintē info par failu

    for mape_vai_fails in mapju_un_failu_saraksts:  # Cikls, kas pārbauda vai mapē ir mapes
        pilnais_cels = os.path.join(mapes_atr_vieta, mape_vai_fails) # Izveido pilnu ceļu mapei vai failam
        if os.path.isdir(pilnais_cels):  # Pārbauda vai tā ir mape
            galvena_funkc(pilnais_cels, hierarhija + "----")      # Ja mapē ir mape, to izprintē. Palielina hierarhiju


galvena_funkc("/home/dav/Desktop/A")