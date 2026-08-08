# Customers Database

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje databázovú oblasť Customers systému Smart Restaurant AI.

Customers Database slúži na evidenciu zákazníkov, ich histórie objednávok, preferencií a vernostných programov.

---

# Business cieľ

Poskytnúť jednotné miesto pre správu zákazníkov a umožniť personalizované služby.

---

# Hlavné entity

## Customer

Predstavuje registrovaného alebo identifikovaného zákazníka.

### Základné údaje

- Customer ID
- First Name
- Last Name
- Email
- Phone Number
- Registration Date
- Status

---

## Customer Preferences

Preferencie zákazníka.

### Základné údaje

- Preference ID
- Customer ID
- Favorite Products
- Allergies
- Dietary Restrictions
- Preferred Communication Channel

---

## Customer History

História aktivít zákazníka.

### Základné údaje

- History ID
- Customer ID
- Order Count
- Reservation Count
- Total Spending
- Last Activity Date

---

## Loyalty Account

Vernostný účet zákazníka.

### Základné údaje

- Loyalty ID
- Customer ID
- Points Balance
- Membership Level
- Last Update

---

# Vzťahy

Customer

↓

Customer Preferences

---

Customer

↓

Customer History

---

Customer

↓

Loyalty Account

---

Customer

↓

Orders

---

Customer

↓

Reservations

---

# Používatelia databázy

## Restaurant Assistant

Používa:

- identifikácia zákazníka
- vytváranie objednávok

---

## Reservation Agent

Používa:

- rezervácie
- história návštev

---

## Sales Agent

Používa:

- analýza správania zákazníkov
- návrhy akcií

---

## Notification Agent

Používa:

- komunikácia so zákazníkmi

---

## Reporting Agent

Používa:

- reporty a štatistiky

---

# Životný cyklus zákazníka

Nový zákazník

↓

Registrácia

↓

Objednávky a rezervácie

↓

Budovanie histórie

↓

Vernostný program

↓

Dlhodobý zákazník

---

# Audit

Každá významná zmena údajov zákazníka musí byť zaznamenaná.

---

# Bezpečnostné pravidlá

- Osobné údaje musia byť chránené.
- Prístup k údajom majú iba oprávnené služby.
- História zákazníka nesmie byť stratená.

---

# Budúce rozšírenia

- AI profil zákazníka
- Predikcia správania
- Automatické odporúčania
- Marketing segmentácia

---

# Poznámky

Customers Database predstavuje základ pre personalizáciu služieb a budovanie vzťahu so zákazníkom.
