from evidence_pojistenych import EvidencePojistenych
from pojisteny import Pojisteny
from hledany import Hledany

"""Třída pro komunikaci s uživatelem"""
class UzivatelskeRozhrani:

    def __init__(self):
        self.evidence = EvidencePojistenych()

    """Zobrazí manu s možnostmi pro uživatele"""
    def zobraz_menu(self):
        print("--------------------------------")
        print("Evidence pojištěných")
        print("-------------------------------- \n")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

    """Vytvoří požadavek na záznam nového pojištěnce"""
    def vytvor_pojisteneho(self):

        jmeno = self.zjisti_jmeno()
        prijmeni = (self.zjisti_prijmeni())
        vek = self.zjisti_vek()
        telefon = self.zjisti_telefon()

        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.evidence.pridej_pojisteneho(pojisteny)
        print("\nData byla uložena.")

    """Zjistí a zvaliduje jméno"""
    def zjisti_jmeno(self):
        validita = False
        while not validita:
            jmeno = input("Zadejte jméno: ")
            if not jmeno: print("\nNezadal jste jméno. Zadejte jméno:")
            else: return jmeno

    """Zjistí a zvaliduje příjmení"""
    def zjisti_prijmeni(self):
        validita = False
        while not validita:
            jmeno = input("Zadejte příjmení: ")
            if not jmeno: print("\nNezadal jste příjmení. Zadejte příjmení:")
            else: return jmeno

    """Zjistí a zvaliduje věk"""
    def zjisti_vek(self):
        validita = True
        vek = -1
        while not validita or vek < 0:
            validita = True
            vek = input("Zadejte věk: ")
            try:
                vek = int(vek)
            except ValueError:
                validita = False
            if not validita or vek < 0:
                print ("\nVěk musí být celé, kladné číslo:")
            else: return vek

    """Zjistí a zvaliduje telefon"""
    def zjisti_telefon(self):
        validita = False
        while not validita:
            jmeno = input("Zadejte telefon: ")
            if not jmeno: print("\nNezadal jste telefon. Zadejte telefon:")
            else: return jmeno

    """Vytvoří požadavek na nalezení pojištěnce"""
    def vytvor_dotaz(self):
        jmeno = self.zjisti_jmeno()
        prijmeni = self.zjisti_prijmeni()
        hledany = Hledany(jmeno, prijmeni)
        if not self.evidence.najdi_pojisteneho(hledany):
            print ("\nPojištěný nenalezen")
        else:

            for pojisteny in self.evidence.najdi_pojisteneho(hledany):
                print(pojisteny)

    """Vytvoří požadavek na výpis všech pojištěnců"""
    def vypis_pojistene(self):
        for pojisteny in self.evidence.vrat_pojistene():
            print(pojisteny)

    """Zobrazí Pokračujte klávesou enter"""
    def zobraz_enter(self):
        input("Pokračujte klávesou enter.")
