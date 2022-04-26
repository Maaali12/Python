class Roboter:
    def __init__(self, name, alter, wohnort):
        self.name = name
        self.alter = alter
        self.wohnort = wohnort 
    def SageHallo(self):
        print("Hallo, mein Name ist " + self.name + " und ich bin " + self.alter + " Jahre alt.")
        print("Ich Wohne in " + self.wohnort + ".")

x = Roboter(input("Wie heißt du?: ") , input("Wie alt bist du?: ") , input("In Welcher Stadt Wohnst du? "))
x.SageHallo()