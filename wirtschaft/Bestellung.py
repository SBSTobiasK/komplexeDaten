class Bestellung:
    __menge = ""
    __stk_preis = ""
    __versandkosten = ""
    __bestellnummer = ""
    __bezeichnung = ""

    def setMenge(self, menge):
        self.__menge = menge

    def getMenge(self):
        return self.__menge

    def setPreis(self, stk_preis):
        self.__stk_preis = stk_preis

    def getPreis(self):
        return self.__stk_preis

    def setVersandkosten(self, versandkosten):
        self.__versandkosten = versandkosten

    def getVersandkosten(self):
        return self.__versandkosten

    def setBestellnummer(self, bestellnummer):
        self.__bestellnummer = bestellnummer

    def getBestellnummer(self):
        return self.__bestellnummer

    def setBezeichnung(self, bezeichnung):
        self.__bezeichnung = bezeichnung

    def getBezeichnung(self):
        return self.__bezeichnung

    #Konstruktor
    def __init__(self):
        print("Objekt wurde erzeugt.")
