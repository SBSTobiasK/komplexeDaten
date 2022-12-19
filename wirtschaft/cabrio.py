from wirtschaft import Auto
#Klasse Cabrio Vererbung von Auto
class Cabrio(Auto):
#Attribut
    __verdeckfarbe =""

    def __init__(self):
        super().__init__()
        print("Hallo von Klasse Cabrio")

    def setVerdeckfarbe(self, farbe):
        self.__verdeckfarbe = farbe

    def getVerdeckfarbe(self):
        return self.__verdeckfarbe

    def oeffneVerdeck(self):
        print("Verdeck öffnen")

    def gibGas(self):
        print("Brummm vom Cabrio")