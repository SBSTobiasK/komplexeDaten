from wirtschaft import Bestellung
from wirtschaft import Kunde

bestellung_1 = Bestellung()
bestellung_1.setMenge(1)
bestellung_1.setPreis(11.12)
bestellung_1.setVersandkosten(7.79)
bestellung_1.setBestellnummer(1234567890)
bestellung_1.setBezeichnung("Testartikel")

print(bestellung_1.getMenge())
print(bestellung_1.getPreis())
print(bestellung_1.getVersandkosten())
print(bestellung_1.getBestellnummer())
print(bestellung_1.getBezeichnung())

#print(bestellung_1.versandkosten)

kunde_1 = Kunde()
kunde_1.setVorname("test")
kunde_1.addBestellung(bestellung_1)

bestellung_2 = Bestellung()
bestellung_2.setBezeichnung("Best2")

kunde_1.addBestellung(bestellung_2)

print(kunde_1.getVorname())

bst = kunde_1.getBestellungen()

print(bst[0].getBezeichnung())