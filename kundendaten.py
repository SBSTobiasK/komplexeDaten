def email_aendern(kunde, neue_email):
    kunde[2] = neue_email

kunde1 = ["Hans", "Meier", "hm@gmx.de"]
kunde2 = ["Mustafa", "Imram", "mi@gmx.de"]

kunden = [["Hans", "Meier", "hm@gmx.de"], ["Mustafa", "Imram", "mi@gmx.de"]]

print(kunde1)
print(kunde2)

email_aendern(kunde2, "mi@hotmail.com")

print(kunde2)
