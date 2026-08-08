# Request Processing Architecture

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje spôsob spracovania všetkých požiadaviek v systéme Smart Restaurant AI.

Opisuje tok požiadaviek od ich prijatia až po odoslanie odpovede používateľovi.

---

# Business cieľ

Vytvoriť jednotný spôsob spracovania všetkých požiadaviek systému.

Každá požiadavka bude spracovaná rovnakým princípom bez ohľadu na to, či ide o objednávku, rezerváciu alebo platbu.

---

# Architektúra spracovania požiadavky

Používateľ

↓

Web / Mobilná aplikácia

↓

API

↓

AI Core

↓

Restaurant Assistant

↓

Príslušný AI Agent

↓

Databáza

↓

Restaurant Assistant

↓

API

↓

Používateľ

---

# Zodpovednosť jednotlivých vrstiev

## Používateľ

Vytvorí požiadavku.

Príklady:

- vytvorenie objednávky
- rezervácia stola
- online platba
- registrácia

---

## API

Prijíma požiadavky.

Vykonáva:

- autentifikáciu
- autorizáciu
- validáciu vstupných údajov

API nevykonáva business logiku.

---

## AI Core

Riadi spracovanie požiadavky.

Rozhoduje:

- ktorý agent bude použitý
- aké služby bude potrebné vykonať
- v akom poradí budú vykonané

---

## Restaurant Assistant

Koordinuje jednotlivých agentov.

Zabezpečuje komunikáciu medzi AI Core a ostatnými agentmi.

---

## AI Agenti

Každý agent vykonáva jednu konkrétnu úlohu.

Príklady:

- Inventory Agent
- Kitchen Agent
- Payment Agent
- Notification Agent
- Reporting Agent

---

## Databáza

Ukladá alebo načítava údaje.

Databáza nikdy nerozhoduje.

---

# Príklad spracovania objednávky

1. Zákazník odošle objednávku.
2. API prijme požiadavku.
3. AI Core rozhodne, že ide o proces vytvorenia objednávky.
4. Restaurant Assistant spustí workflow objednávky.
5. Inventory Agent overí dostupnosť.
6. Orders Database vytvorí objednávku.
7. Kitchen Agent prijme objednávku.
8. Payment Agent spracuje platbu.
9. Notification Agent odošle potvrdenie.
10. Reporting Agent zapíše údaje do reportov.
11. Restaurant Assistant pripraví odpoveď.
12. API odošle odpoveď zákazníkovi.

---

# Hlavné princípy

- Každá požiadavka prechádza AI Core.
- AI agenti medzi sebou nekomunikujú priamo bez koordinácie.
- Restaurant Assistant riadi workflow.
- API obsahuje iba komunikačnú vrstvu.
- Databáza neobsahuje business logiku.

---

# Výhody architektúry

- jednoduché rozširovanie systému
- jednoduché pridávanie nových agentov
- jednotné workflow
- jednoduchšie testovanie
- vyššia bezpečnosť
- lepšia údržba systému

---

# Budúce rozšírenia

- viac AI Core modulov
- paralelné spracovanie požiadaviek
- podpora externých AI agentov
- distribuovaná architektúra

---

# Stav dokumentu

🟡 Rozpracovaný# Request Processing Architecture
