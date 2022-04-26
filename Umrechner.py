print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")

auswahl = input("Bitte rechner auswählen:")

if auswahl == "1":
    celsius = float(input("Temperatur in Celsius angeben:"))
    if celsius >= -273.15:
        kelvin = celsius + 273.15
        print(celsius, "° = ", kelvin, "K")
    else:
        print("Fehler: Falsche angabe!")
else: auswahl == "2"
    celsius = float

