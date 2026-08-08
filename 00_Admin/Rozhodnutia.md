# Rozhodnutie #001

## Téma

Filozofia produktu

## Rozhodnutie

Smart Restaurant AI nebude vytvorený s cieľom nahrádzať ľudí.

Jeho úlohou bude prepájať existujúce systémy, automatizovať rutinné úlohy a pomáhať majiteľovi robiť lepšie rozhodnutia.

## Dôvod

Našou hodnotou nie je nahradiť personál.

Našou hodnotou je ušetriť čas, znížiť počet chýb a zvýšiť efektivitu prevádzky.

## Stav

✅ Schválené

# Rozhodnutie #002

## Téma

Prvý cieľový zákazník

## Rozhodnutie

Prvými zákazníkmi Smart Restaurant AI budú reštaurácie a gastro prevádzky, ktoré stále vykonávajú veľkú časť administratívy ručne (papier, Excel alebo neprepojené systémy).

## Dôvod

Najväčšiu hodnotu dokážeme priniesť tam, kde dnes majiteľ alebo zamestnanci strácajú čas opakovanými manuálnymi úlohami.

Produkt nebude zameraný podľa veľkosti prevádzky, ale podľa úrovne digitalizácie.

## Stav

✅ Schválené

# ADR-003 – AI Core Architecture

## Verzia dokumentu

v1.0

---

# Stav

✅ Schválené

---

# Dátum

3.7.2026

---

# Kontext

Počas návrhu architektúry Smart Restaurant AI vznikla otázka, ktorá vrstva systému bude predstavovať hlavný riadiaci prvok platformy.

Zvažovali sa dve možnosti:

- Restaurant Assistant ako hlavný koordinátor systému.
- AI Core ako univerzálny riadiaci prvok celej platformy.

---

# Rozhodnutie

Za hlavný riadiaci prvok celej platformy bol zvolený **AI Core**.

Restaurant Assistant nebude predstavovať hlavný mozog systému.

Restaurant Assistant bude doménový koordinátor určený pre gastro segment a bude riadiť iba procesy súvisiace s reštauráciami.

AI Core bude riadiť všetkých doménových asistentov.

---

# Architektúra

Používateľ

↓

API

↓

AI Core

↓

Restaurant Assistant

↓

Špecializovaní AI agenti

↓

Databáza

---

# Budúce rozšírenia

AI Core bude podporovať ďalších doménových asistentov.

Príklady:

- Restaurant Assistant
- Hotel Assistant
- Clinic Assistant
- Warehouse Assistant
- Retail Assistant
- Service Assistant

Každý nový asistent bude využívať rovnaké AI Core.

---

# Výhody rozhodnutia

- Jednotná architektúra platformy.
- Jednoduché rozšírenie do ďalších odvetví.
- Oddelenie business logiky od platformovej logiky.
- Vyššia modularita.
- Jednoduchšia údržba.
- Opätovné využitie AI Core.

---

# Nevýhody

- AI Core bude predstavovať kritickú časť systému.
- Vyžaduje kvalitné riadenie komunikácie medzi asistentmi.

---

# Dôvod rozhodnutia

Cieľom projektu nie je vytvoriť iba systém pre reštaurácie.

Architektúra musí umožniť budúce rozšírenie do ďalších oblastí bez zásadných zmien platformy.

Restaurant Assistant predstavuje iba jeden z doménových modulov využívajúcich spoločné AI Core.

---

# Dopad na projekt

Od tohto rozhodnutia bude každá nová funkcionalita navrhovaná s predpokladom, že AI Core predstavuje centrálny riadiaci prvok celej platformy.

Všetci doménoví asistenti budú využívať spoločnú platformovú architektúru.

Klient nikdy nepotvrdzuje úspešnosť platby.

Restaurant Assistant považuje platbu za úspešnú výhradne po potvrdení platobnou bránou.
