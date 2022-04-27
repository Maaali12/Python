paswort = input("Passwort bitte eingeben: ")
key = "12345"

while True:
    if paswort == key:
        print("Passwort korrekt.")
        break
    else:
        print("Paswort Falsch!")
        quit()
