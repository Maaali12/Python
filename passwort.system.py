key = "12345"

def passwort_abfrage():
    passwort = input("Passwort bitte eingeben: ")
    while True:
        if passwort == key:
            print("Passwort korrekt.")
            break
        else:
            print("Falsches Passwort!")
            quit()

passwort_abfrage()