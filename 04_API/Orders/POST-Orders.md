# POST /payments

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces vytvorenia novej platobnej požiadavky pre existujúcu objednávku v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť bezpečné vytvorenie a spracovanie platby zákazníka prostredníctvom samostatného Payments modulu bez zasahovania do logiky objednávok.

Zabezpečiť jasné oddelenie zodpovedností medzi:

- Orders modulom,
- Payments modulom,
- Restaurant Assistantom,
- Payment Agentom.

---

# Endpoint

POST /payments

---

# HTTP Metóda

POST

---

# URL

/api/v1/payments

---

# Popis

Endpoint vytvorí novú platobnú požiadavku pre existujúcu objednávku.

Proces vytvorenia platby je riadený cez Restaurant Assistant, ktorý koordinuje komunikáciu medzi Orders modulom a Payment Agentom.

Payment Agent zabezpečuje vytvorenie platby a komunikáciu s platobným poskytovateľom.

Payments modul iba spracováva platobnú časť procesu a nemení stav objednávky priamo.

---

# Kto môže volať API

- Restaurant Assistant
- Payment Agent
- Administrátor systému

---

# Vstupné údaje (Request)

Platobná požiadavka obsahuje:

- Order ID
- Customer ID
- Celková suma platby
- Mena
- Spôsob platby

---

# Workflow

1. Orders modul vytvorí novú objednávku v stave Payment Pending.
2. Restaurant Assistant prijme informáciu o potrebe vytvorenia platby.
3. Restaurant Assistant odošle požiadavku Payment Agentovi.
4. Payment Agent vytvorí platobnú požiadavku.
5. Payments API overí existenciu objednávky.
6. Payments Database vytvorí záznam o platbe v stave Pending.
7. Payment Agent odošle požiadavku platobnému poskytovateľovi.
8. Systém čaká na výsledok spracovania platby.
9. Výsledný stav platby sa aktualizuje cez PATCH /payments/{id}/status.
10. Payment Agent odošle výsledok platby Restaurant Assistantovi.
11. Restaurant Assistant podľa výsledku pokračuje v ďalšom procese objednávky.

---

# Zapojení AI agenti

## Restaurant Assistant

- Koordinuje proces vytvorenia platby.
- Komunikuje medzi Orders a Payments modulom.
- Prijíma výsledok platby.
- Riadi ďalší postup objednávky.

## Payment Agent

- Vytvára platobné požiadavky.
- Komunikuje s platobným poskytovateľom.
- Spracováva výsledky platieb.
- Informuje Restaurant Assistant o výsledku.

---

# Použité databázy

Pri vytvorení platby sa priamo používa:

- Payments Database

Súvisiace moduly:

- Orders Database
- Customers Database

---

# Odpoveď systému (Response)

Úspešná odpoveď obsahuje:

- Payment ID
- Order ID
- Stav platby
- Celkovú sumu
- Mena
- Spôsob platby
- Čas vytvorenia platby

---

# Možné stavy platby

- Pending
- Processing
- Completed
- Failed
- Cancelled

---

# Chybové stavy

- Objednávka neexistuje.
- Platba pre objednávku už existuje.
- Platobný pokus už bol vykonaný.
- Neplatná suma platby.
- Nepodporovaný spôsob platby.
- Chyba komunikácie s platobným poskytovateľom.
- Interná chyba systému.

---

# Audit

Systém zaznamenáva:

- vytvorenie platby,
- prepojenie platby s objednávkou,
- identifikáciu platobného poskytovateľa,
- zmenu stavu platby,
- výsledok spracovania platby.

---

# Bezpečnosť

- Autorizácia požiadavky.
- Kontrola oprávnenia vytvoriť platbu.
- Validácia vstupných údajov.
- Ochrana platobných údajov.
- Šifrovanie citlivých údajov.
- Logovanie všetkých udalostí.

---

# Business pravidlá

- Jedna objednávka môže mať iba jednu platbu.
- Každá platba predstavuje iba jeden platobný pokus.
- Pri neúspešnej platbe nie je možné vytvoriť nový platobný pokus pre existujúcu objednávku.
- Pri opakovanom nákupe musí zákazník vytvoriť novú objednávku.
- Payment modul nevytvára ani neupravuje objednávky.
- Payment modul nemení stav objednávky priamo.
- Výsledok platby komunikuje Payment Agent Restaurant Assistantovi.
- Zmena stavu objednávky prebieha cez Orders API.
- Platobné údaje sú oddelené od ostatných modulov.

---

# Súvisiace dokumenty

- Orders API
- POST /orders
- PATCH /orders/{id}/status
- Payments Database
- Payment Workflow
- AI Agent Communication
- Restaurant Assistant Architecture

---

# Budúce rozšírenia

- Viacero platobných poskytovateľov.
- Refundácie.
- Fakturačný systém.
- Rozšírené finančné reporty.
- Automatická detekcia podozrivých transakcií.

---

# Stav dokumentu

🟢 Hotový
