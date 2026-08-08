# Orders Database

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje databázovú oblasť Orders systému Smart Restaurant AI.

Objednávky predstavujú hlavný business proces celej platformy a prepájajú zákazníkov, produkty, platby a kuchyňu.

---

# Business cieľ

Umožniť evidenciu a sledovanie každej objednávky počas celého životného cyklu.

---

# Hlavné entity

## Order

Predstavuje jednu objednávku zákazníka.

### Základné údaje

- Order ID
- Customer ID
- Order Number
- Order Date
- Order Type
- Order Status
- Total Amount
- Payment Status

---

## Order Item

Predstavuje konkrétnu položku objednávky.

### Základné údaje

- Order Item ID
- Order ID
- Product ID
- Quantity
- Unit Price
- Total Price

---

## Order Status

Definuje aktuálny stav objednávky.

### Možné stavy

- New
- Confirmed
- Preparing
- Ready
- Delivered
- Completed
- Cancelled

---

## Order History

História všetkých zmien objednávky.

### Základné údaje

- History ID
- Order ID
- Previous Status
- New Status
- Timestamp
- Changed By

---

# Vzťahy

Customer

↓

Order

↓

Order Item

↓

Product

---

Order

↓

Payment

---

Order

↓

Kitchen Process

---

Order

↓

Order History

---

# Používatelia databázy

## Restaurant Assistant

Používa:

- vytvorenie objednávky
- zobrazenie stavu objednávky

---

## Kitchen Agent

Používa:

- zobrazenie nových objednávok
- aktualizácia stavu prípravy

---

## Payment Agent

Používa:

- overenie platby
- aktualizácia stavu platby

---

## Reporting Agent

Používa:

- štatistiky objednávok
- reporty

---

# Životný cyklus objednávky

Nová objednávka

↓

Potvrdená

↓

Pripravuje sa

↓

Hotová

↓

Doručená / Prevzatá

↓

Ukončená

---

# Audit

Každá zmena objednávky musí byť uložená do Order History.

---

# Bezpečnostné pravidlá

- Objednávka nesmie byť odstránená.
- Každá zmena musí byť dohľadateľná.
- Históriu môže upravovať iba systém.

---

# Budúce rozšírenia

- Promo kódy
- Kombinované objednávky
- Skupinové objednávky
- Online sledovanie objednávky
- AI predikcia času doručenia

---

# Poznámky

Orders Database predstavuje centrálnu databázovú oblasť systému Smart Restaurant AI a prepája väčšinu business procesov.
