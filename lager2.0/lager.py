import sqlite3

key = ""


def db_start():
    verbindung = sqlite3.connect("lager2.0/lager.db")
    zeiger = verbindung.cursor()

    sql_anweisung = """
    CREATE TABLE lager (
    produkt VARCHAR(20), 
    anzahl DATE
    );"""

    zeiger.execute(sql_anweisung)
    verbindung.commit()

def fehler():
    print("--Achtung--")
    print("Falsche eingabe!")
    print("Achte bitte auf deine zeichen setzung und Rechtschreibung!")


def auswahl():
    print("[1.] Lager bestand abfragen.")
    print("[2.] Lager bestand bearbeiten.")
    print("[3.] Lager System beenden.")
    wahl = input("Bitte asuwahlmöglichkeit auswählen: ")
    while True:
        if wahl == "1":
            print("123123")
        elif wahl == "2":
            print("Testasd")
            break
        elif wahl == "3":
            print("Lager System beendet sich nun.")
            quit()
        else:
            fehler()
            break

def passwort_set():
    print("Passwort konfigurieren: ")
    print("[1.] Passwort setzen/bearbeiten.")
    print("[2.] Kein Passwort verwenden.")
    inputv = input("Bitte wählen: ")
    while True:
        if inputv == "1":
            pass
        elif inputv == "2":
            print("")
        else:
            fehler()
            break













db_start()