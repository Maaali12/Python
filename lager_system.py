from operator import index
import sys

Bestand = {"Bananen": 1, "Äpfel": 2, "Salz": 99, "Ananas": 28,  } 

key = "1205"

def fehler_ausgabe():
    print("Fehler: Falsche eingabe!")
    print("Achte bitte auf deine Rechtschreibung!")

def auswahl_möglichkeit():
    print("[1.] Lager bestand abfragen.")
    print("[2.] Lager bestand bearbeiten.")

def passowrt_abfrage():
    passwort = input("Bitte Passwort zum Fortfahren eingeben: ")
    while True:
        if passwort == key:
            print("Passwort korrekt.")
            break
        else:
            print("Paswort Falsch!")
            quit()

def lager_bestand():
    while True:
        print("Bitte Produkt eingeben: ")
        index = input()
        print("Es sind noch:", Bestand[index], "Stück vorhanden.")

def lager_bearbeiten():
    print("Dieser befehl ist noch in Arbeit!")
    auswahl_möglichkeit()
    auswahl_möglichkeit2()

def auswahl_möglichkeit2():
    wahl = input("Wähle auswahlmöglichkeit aus: ")
    while True:
        if wahl == "1":
            print("Lager bestand wird abgefragt")
            passowrt_abfrage()
            lager_bestand()
            break
        elif wahl == "2":
            passowrt_abfrage()
            lager_bearbeiten()
            break 
        else:
            fehler_ausgabe()
            return



auswahl_möglichkeit()
auswahl_möglichkeit2()