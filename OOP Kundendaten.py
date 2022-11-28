class Kunde:
    vorname = ""
    nachname = ""
    e_mail = ""

    def ausgabe(self):
        print("Vorname:", self.vorname, "Nachname:", self.nachname, "E-Mail:", self.e_mail)

    def ueberschreiben(self, neu):
        # z.B. ob @ enthalten ist usw ...
        self.e_mail = neu


kunde_1 = Kunde()
kunde_1.vorname = "Hans"
kunde_1.nachname = "Meier"
kunde_1.e_mail = "k1@gmail.com"

kunde_2 = Kunde()
kunde_2.vorname = "Hans"
kunde_2.nachname = "Meier"
kunde_2.e_mail = "k1@gmail.com"

print(kunde_2.vorname)

kunde_2.e_mail = "k2@gmx.de"
print(kunde_2.e_mail)

kunde_1.ausgabe()

kunde_1.ueberschreiben("neu@gmx.de")

kunde_1.ausgabe()
kunde_2.ausgabe()