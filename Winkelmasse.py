from math import pi

rad = float(input("Winkel in Bogenmass eingeben: "))
deg = rad*180.0/pi
grad = int(deg)
bogenmin = int((deg - grad)*60)
bogenmin = ((deg - grad)*60 - bogenmin)*60
print(rad, " rad = ", grad, "°", bogenmin, "'", bogenmin, "\"", sep = "")