class Mensch:
    def SageHallo(self):
        print("Hallo, mein Name ist " + self.name + " und ich bin " + self.alter + " Jahre alt.")
    def SetzeNamen(self, name):
        self.name = name
    def SetzeAlter(self, alter):
        self.alter = alter

x = Mensch()
x.SetzeNamen(input("Wie heißt du?:"))
x.SetzeAlter(input("Wie Alt bist du?:"))
x.SageHallo()