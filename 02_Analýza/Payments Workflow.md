# Payments Workflow

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces spracovania platieb od vytvorenia objednávky až po potvrdenie úspešnej platby.

---

# Business cieľ

Zabezpečiť bezpečné, spoľahlivé a overiteľné spracovanie platieb pred začatím prípravy objednávky.

---

# Začiatok procesu

Proces začína od vytvorenia objednávky zákazníkom.

---

# Workflow

## 1. Vytvorenie objednávky

Zákazník vytvorí objednávku.

↓

Restaurant Assistant prijme požiadavku.

↓

Objednávka získa stav:

Pending Payment

---

## 2. Inicializácia platby

Restaurant Assistant odošle požiadavku Payment Agentovi.

↓

Payment Agent vytvorí platobnú reláciu.

---

## 3. Platba zákazníkom

Zákazník vykoná platbu prostredníctvom podporovanej platobnej metódy.

---

## 4. Overenie platby

Zákazník dokončí platbu prostredníctvom platobnej brány.

↓

Platobná brána odošle potvrdenie Restaurant Assistantovi.

↓

Restaurant Assistant po prijatí potvrdenia overí stav platby.

Ak bola platba úspešná:

↓

Objednávka získa stav:

Paid

↓

Restaurant Assistant pokračuje v Inventory Workflow.

Ak platba zlyhá:

↓

Objednávka zostáva v stave:

Pending Payment

alebo

Failed

↓

Restaurant Assistant informuje zákazníka o neúspešnej platbe.

---

## 5. Kontrola skladu

Restaurant Assistant odošle požiadavku Inventory Agentovi na kontrolu dostupnosti surovín.

↓

Inventory Agent overí dostupnosť všetkých potrebných surovín.

Ak sú suroviny dostupné:

↓

Inventory Agent rezervuje potrebné množstvo surovín.

↓

Restaurant Assistant pokračuje v Kitchen Workflow.

Ak niektoré suroviny nie sú dostupné:

↓

Restaurant Assistant informuje zákazníka o nedostupnosti.

↓

Zákazník si môže vybrať jednu z možností:

- zmeniť objednávku,
- nahradiť nedostupnú položku,
- zrušiť objednávku.

Ak zákazník súhlasí so zmenou:

↓

Restaurant Assistant aktualizuje objednávku.

↓

Inventory Agent vykoná novú kontrolu dostupnosti.

Ak zákazník objednávku zruší:

↓

Restaurant Assistant iniciuje proces refundácie platby.

---

## 6. Ukončenie procesu

Proces úspešne končí odovzdaním objednávky do Kitchen Workflow.

Ak platba alebo kontrola skladu zlyhá, proces končí informovaním zákazníka o dôvode neúspešného spracovania objednávky.

---

# AI Agenti

- Restaurant Assistant
- Payment Agent
- Inventory Agent
- Notification Agent
- Reporting Agent

---

# Databázy

- Orders Database
- Payments Database

---

# Stavy platby

Pending

↓

Paid

alebo

Failed

alebo

Cancelled

---

# Koniec procesu

Proces končí úspešným potvrdením platby alebo jej neúspešným ukončením.

---

# Budúce rozšírenia

- Podpora viacerých platobných brán.
- Opakovaný pokus o platbu.
- Automatické refundácie.
- Firemné fakturácie.
- Vernostné body.
- Darčekové poukážky.

---

# Stav dokumentu

🟡 Rozpracovaný
