import sys

Bestand = {"Bananen": 1, "Äpfel": 2, "Salz": 99, "Ananas": 28, } #Liste mit vorhandenen gegenständen
paswort = input("Passwort bitte eingeben:")

def error_ausgabe():
    print("Fehler: Falsche eingabe!")
    print("Achte bitte auf deine Rechtschreibung!")
    
while True:
    if paswort == "1234":
        print("Passwort korrekt.")
    else:
        print("Paswort Falsch!")
        quit()

while True:
    print("Bitte Produkt eingeben:")  #Ausgabe
    index = input()  #Eingabe
    print("Es sind noch:", Bestand[index], "Stück", "vorhanden.")  #Ausgabe
