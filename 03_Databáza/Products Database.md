# Products Database

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje databázovú oblasť Products systému Smart Restaurant AI.

Products Database slúži na evidenciu všetkých produktov, ktoré reštaurácia ponúka zákazníkom, vrátane cien, kategórií, dostupnosti a histórie zmien.

---

# Business cieľ

Poskytnúť centralizovanú správu produktov a zabezpečiť ich prepojenie s objednávkami, skladom a reportovaním.

---

# Hlavné entity

## Product

Predstavuje jeden produkt alebo jedlo v ponuke.

### Základné údaje

- Product ID
- Product Name
- Description
- Category ID
- Price
- Status
- Creation Date

---

## Product Category

Predstavuje kategóriu produktu.

### Základné údaje

- Category ID
- Category Name
- Description

### Príklady

- Pizza
- Burgre
- Nápoje
- Dezerty
- Prílohy

---

## Product Availability

Definuje dostupnosť produktu.

### Základné údaje

- Availability ID
- Product ID
- Availability Status
- Last Update

### Možné stavy

- Available
- Limited
- Out Of Stock
- Hidden

---

## Product Price History

História zmien cien produktu.

### Základné údaje

- Price History ID
- Product ID
- Old Price
- New Price
- Change Date
- Changed By

---

# Vzťahy

Product Category

↓

Product

---

Product

↓

Product Availability

---

Product

↓

Product Price History

---

Product

↓

Order Item

---

Product

↓

Inventory Item

---

# Používatelia databázy

## Restaurant Assistant

Používa:

- zobrazenie menu
- vytváranie objednávok

---

## Inventory Agent

Používa:

- kontrola dostupnosti produktov
- prepojenie na sklad

---

## Kitchen Agent

Používa:

- príprava objednávok
- kontrola produktov

---

## Sales Agent

Používa:

- analýza predaja
- štatistiky produktov

---

## Reporting Agent

Používa:

- reporty
- KPI ukazovatele

---

# Životný cyklus produktu

Vytvorenie produktu

↓

Priradenie kategórie

↓

Nastavenie ceny

↓

Predaj zákazníkom

↓

Úpravy produktu

↓

Archivácia alebo deaktivácia

---

# Audit

Každá zmena produktu musí byť zaznamenaná.

Každá zmena ceny musí byť uložená do Product Price History.

---

# Bezpečnostné pravidlá

- Produkt nesmie byť odstránený bez oprávnenia.
- História cien musí byť zachovaná.
- Kritické zmeny musia byť logované.

---

# Budúce rozšírenia

- Viacjazyčné menu.
- AI odporúčanie produktov.
- Dynamické ceny.
- Sezónne produkty.
- Produktové balíčky.

---

# Poznámky

Products Database predstavuje centrálny katalóg produktov systému Smart Restaurant AI a prepája objednávky, skladové hospodárstvo a analytiku.

---

# Stav dokumentu

🟡 Rozpracovaný
