class Bestellung:
    menge = ""
    stk_preis = ""
    versandkosten = ""
    bestellnummer = ""
    bezeichnung = ""

    def setMenge(self, menge):
        self.menge = menge

    def getMenge(self):
        return self.menge

    def setPreis(self, stk_preis):
        self.stk_preis = stk_preis

    def getPreis(self):
        return self.stk_preis

    def setVersandkosten(self, Versandkosten):

bestellung_1 = Bestellung()
bestellung_1.setMenge(1)
print(bestellung_1.getMenge())