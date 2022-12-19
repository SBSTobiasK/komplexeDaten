from wirtschaft import Bestellung
from wirtschaft import Kunde
from wirtschaft import Artikel
from wirtschaft import Auto
from wirtschaft import Cabrio

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

kunde_1.stornoAlle()

bst = kunde_1.getBestellungen()

print(bst)

artikel_a = Artikel()
artikel_a.setBezeichnung("TESTARTIKELBEZEICHNUNG1")
print(artikel_a.getBezeichnung())

artikel_b = Artikel()
artikel_b.setBezeichnung("TESTARTIKELBEZEICHNUNG2")

bestellung_1.setArtikel(artikel_a)
bestellung_1.setArtikel(artikel_b)

art = bestellung_1.getArtikel()
print(art[0].getBezeichnung())
print(art[1].getBezeichnung())

auto1 = Auto()
auto1.setMarke("Fiat")
auto1.setFarbe("rot")
auto1.setTuerenanzahl("5")
print(auto1.getMarke())
print(auto1.getFarbe())
print(auto1.getTuerenanzahl())
auto1.gibGas()

auto2 = Auto()

cabrio1 = Cabrio()

cabrio1.setMarke("Lotus")
print(cabrio1.getMarke())
cabrio1.oeffneVerdeck()

auto1.gibGas()
cabrio1.gibGas()

