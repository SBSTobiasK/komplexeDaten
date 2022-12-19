class Auto:
    #Atribute
    __tuerenanzahl = ""
    __farbe = ""
    __marke = ""

    def __init__(self):
        print("Hallo von Klasse Auto.")

#Methoden
# Setter
    def setTuerenanzahl(self, anzahl):
        self.__tuerenanzahl = anzahl
    def setFarbe(self, farbe):
        self.__farbe = farbe
    def setMarke(self, marke):
        self.__marke = marke
# Getter
    def getTuerenanzahl(self):
        return self.__tuerenanzahl
    def getFarbe(self):
        return self.__farbe
    def getMarke(self):
        return self.__marke
# weiterführende Methoden
    def gibGas(self):
        print("Brummm")