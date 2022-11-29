class Kunde:
    __vorname = ""
    __nachname = ""
    __e_mail = ""
    __telnr = ""
    __strasse = ""
    __hausnr = ""
    __plz = ""
    __ort = ""
    __bestellungen = []

    def addBestellung(self, bestellung):
        self.__bestellungen.append(bestellung)

    def stornoAlle(self):
        self.__bestellungen = []

    def getBestellungen(self):
        return self.__bestellungen



    def setVorname(self, vorname):
        self.__vorname = vorname

    def getVorname(self):
        return self.__vorname

    def setNachname(self, nachname):
        self.__nachname = nachname

    def getNachname(self):
        return self.__nachname

    def setE_mail(self, e_mail):
        self.__e_mail = e_mail

    def getE_mail(self):
        return self.__e_mail

    def setTelnr(self, telnr):
        self.__telnr = telnr

    def getTelnr(self):
        return self.__telnr

    def setStrasse(self, strasse):
        self.__strasse = strasse

    def getStrasse(self):
        return self.__strasse

    def setHausnr(self, hausnr):
        self.__hausnr = hausnr

    def getHausnr(self):
        return self.__hausnr

    def setPlz(self, plz):
        self.__plz = plz

    def getPlz(self):
        return self.__plz

    def setOrt(self, ort):
        self.__ort = ort

    def getOrt(self):
        return self.__ort

