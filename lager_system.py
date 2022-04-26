#Lager System von Max
Bestand = {"Bananen": 1, "Äpfel": 2, "Salz": 99, "Ananas": 28,  } #Liste mit vorhandenen gegenständen
paswort = input("Passwort bitte eingeben:")

while True:
    if paswort == "1234":
        print("Passwort korrekt.")
        break
else:
    print("Paswort Falsch!")

while True:
    print("Bitte Produkt eingeben:")  #Ausgabe
    index = input()  #Eingabe
    print("Es sind noch:", Bestand[index], "Stück", "vorhanden.")  #Ausgabe