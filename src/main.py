from pojisteny import Pojisteny
from hledany import Hledany
from evidence_pojistenych import EvidencePojistenych
from uzivatelske_rozhrani import UzivatelskeRozhrani

rozhrani = UzivatelskeRozhrani()

volba = 0
while volba != "4":

    rozhrani.zobraz_menu()
    volba = input()

    match volba:
        case "1":
            rozhrani.vytvor_pojisteneho()

        case "2":
            rozhrani.vypis_pojistene()

        case "3":
            rozhrani.vytvor_dotaz()

    if volba in ["1", "2", "3"]:
        rozhrani.zobraz_enter()
