"""Třída pro práci s daty"""
class EvidencePojistenych:

    def __init__(self):
        self.pojisteni = []

    """zpracuje požadavek na přidání nového pojištěnce"""
    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    """zpracuje požadavek na vypsání všech pojištění"""
    def vrat_pojistene(self):
         return self.pojisteni

    """zpracuje požadavek na vyhledání jednoho pojištěnce"""
    def najdi_pojisteneho(self, hledany):
        self.vypis_pojisteneho = []
        nalezen = False
        for pojisteny in (self.pojisteni):
            if pojisteny.jmeno == hledany.jmeno and pojisteny.prijmeni == hledany.prijmeni:
                self.vypis_pojisteneho.append(pojisteny)
                nalezen = True
        if not nalezen:
            return nalezen
        else:
            return self.vypis_pojisteneho
