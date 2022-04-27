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
    while True:
        if paswort == key:
            print("Passwort korrekt.")
            break
    else:
        print("Paswort Falsch!")
        quit()



auswahl_möglichkeit()
wahl = input("Wähle auswahlmöglichkeit aus.")

while True:
    if wahl == "1":
        passwort_abfrage()
    else:
        if wahl == "2":
        passwort_abfrage()
    else:
        fehler_ausgabe()
