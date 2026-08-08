nie sme ďalší systém, sme vrstva, ktorá prepája existujúce systémy“ podľa mňa zásadne ovplyvní celý projekt.

# Pravidlo AI architekta

Nikdy neanalyzuj iba funkcie.

Analyzuj celý proces.

Každý proces rozdeľ na čo najmenšie kroky.

Práve medzi jednotlivými krokmi vznikajú chyby, zdržania a príležitosti na automatizáciu.

# Pravidlo AI architekta

Každý proces navrhujem v troch scenároch:

1. Ideálny priebeh.
2. Výnimky (napr. chýbajúci produkt, zamietnutá platba).
3. Chybové stavy (výpadok internetu, databázy alebo API).

Až keď sú navrhnuté všetky tri scenáre, považujem proces za pripravený na implementáciu.

# Architektonické rozhodnutia

## Rozhodnutie 001

Otázka:

Kedy sa vytvorí objednávka?

Možnosť A

Objednávka vznikne až po úspešnej platbe.

Výhody

- menej neplatných objednávok

Nevýhody

- riziko konfliktov pri posledných skladových položkách

---

Možnosť B

Objednávka vznikne okamžite.

Status = Pending.

Výhody

- možnosť rezervovať sklad
- lepšie zvládnutie súbežných objednávok

Nevýhody

- vznikajú nezaplatené objednávky

---

Naše rozhodnutie

Online objednávky:

Pending → Payment → Confirmed

Objednávky v reštaurácii:

Confirmed okamžite, platba môže prebehnúť neskôr.


# Rozhodnutie

Každý API endpoint vracia údaje iba zo svojej business domény.

Ak sú pre spracovanie požiadavky potrebné informácie z iných modulov (napríklad Payments, Reporting alebo Notifications), získavajú sa prostredníctvom samostatných API endpointov.

Tým sa zabezpečí jasné oddelenie business domén, jednoduchšia údržba systému, lepšia škálovateľnosť a konzistentná architektúra celej platformy.


ADR – Úprava objednávky zákazníkom
Rozhodnutie

Zákazník môže pri vytváraní objednávky požiadať o odstránenie ľubovoľnej suroviny z produktu.

Táto úprava sa vykonáva iba pre konkrétnu objednávku a nikdy nemení definíciu produktu v databáze. 


ADR – Úprava objednávky zákazníkom
Rozhodnutie

Zákazník môže pri vytváraní objednávky požiadať o odstránenie ľubovoľnej suroviny z produktu.

Táto úprava sa vykonáva iba pre konkrétnu objednávku a nikdy nemení definíciu produktu v databáze.
