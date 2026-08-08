# Inventory Database

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje databázovú oblasť Inventory systému Smart Restaurant AI.

Inventory Database slúži na evidenciu skladových zásob, pohybov na sklade, surovín a dodávateľov.

Jej hlavným cieľom je zabezpečiť automatickú kontrolu zásob a podporiť efektívne riadenie skladu.

---

# Business cieľ

Poskytnúť presný prehľad o skladových zásobách a automatizovať proces sledovania spotreby surovín.

---

# Hlavné entity

## Inventory Item

Predstavuje skladovú položku.

### Základné údaje

- Inventory Item ID
- Item Name
- Item Type
- Current Quantity
- Minimum Quantity
- Unit
- Status

---

## Ingredient

Predstavuje surovinu používanú pri výrobe produktov.

### Základné údaje

- Ingredient ID
- Ingredient Name
- Unit
- Description

---

## Product Ingredient

Prepojenie medzi produktom a surovinami.

### Základné údaje

- Product Ingredient ID
- Product ID
- Ingredient ID
- Quantity Required

---

## Stock Movement

Predstavuje pohyb skladových zásob.

### Základné údaje

- Movement ID
- Inventory Item ID
- Movement Type
- Quantity
- Movement Date
- Created By

### Typy pohybov

- Purchase
- Sale
- Adjustment
- Waste
- Return

---

## Inventory Alert

Upozornenia na skladové zásoby.

### Základné údaje

- Alert ID
- Inventory Item ID
- Alert Type
- Alert Date
- Status

### Typy upozornení

- Low Stock
- Out Of Stock
- Expiration Warning

---

## Supplier

Dodávateľ skladových položiek.

### Základné údaje

- Supplier ID
- Supplier Name
- Contact Person
- Email
- Phone Number
- Status

---

# Vzťahy

Supplier

↓

Inventory Item

---

Ingredient

↓

Inventory Item

---

Product

↓

Product Ingredient

↓

Ingredient

---

Inventory Item

↓

Stock Movement

---

Inventory Item

↓

Inventory Alert

---

# Používatelia databázy

## Inventory Agent

Používa:

- kontrola zásob
- automatické upozornenia
- sledovanie pohybov

---

## Kitchen Agent

Používa:

- kontrola dostupnosti surovín
- odpočítanie spotreby

---

## Restaurant Assistant

Používa:

- overenie dostupnosti produktov

---

## Reporting Agent

Používa:

- skladové reporty
- analýzy spotreby

---

# Životný cyklus skladovej položky

Vytvorenie položky

↓

Pridanie na sklad

↓

Používanie pri predaji

↓

Automatická aktualizácia zásob

↓

Upozornenie na nízky stav

↓

Objednanie nových zásob

↓

Doplnenie skladu

---

# Audit

Každý pohyb skladu musí byť zaznamenaný.

Každá zmena množstva musí byť dohľadateľná.

---

# Bezpečnostné pravidlá

- Skladové pohyby nesmú byť odstránené.
- História pohybov musí byť zachovaná.
- Kritické zmeny musia byť logované.

---

# Budúce rozšírenia

- Automatické objednávky dodávateľom.
- AI predikcia spotreby.
- Expirácia surovín.
- Viac skladov.
- Centrálne skladové hospodárstvo.

---

# Poznámky

Inventory Database predstavuje jadro skladového hospodárstva systému Smart Restaurant AI.

Je priamo prepojená s Products Database a umožňuje automatické sledovanie spotreby surovín na základe predaných produktov.

---

# Stav dokumentu

🟡 Rozpracovaný
