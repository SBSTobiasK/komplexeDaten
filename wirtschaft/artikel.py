class Artikel:
    __artikelnummer = ""
    __preis = ""
    __bezeichnung = ""
    __menge = ""
    __mwstsatz = ""

    def __init__(self, anr, preis, bez, menge, mwst):
        self.__artikelnummer = anr
        self.__preis = preis
        self.__bezeichnung = bez
        self. __menge = menge
        self. __mwstsatz = mwst
    def setArttikelnummer(self, anr):
        self.__artikelnummer = anr

    def getArtikelnummer(self):
        return self.__artikelnummer

    def setPreis(self, preis):
        self.__preis = preis

    def getPreis(self):
        return self.__preis

    def setBezeichnung(self, bez):
        self.__bezeichnung = bez

    def getBezeichnung(self):
        return self.__bezeichnung

    def setMenge(self, menge):
        self.__menge = menge

    def getMenge(self):
        return self.__menge

    def setMwstsatz(self, mwst):
        self.__mwstsatz = mwst

    def getMwstsatz(self):
        return self.__mwstsatz