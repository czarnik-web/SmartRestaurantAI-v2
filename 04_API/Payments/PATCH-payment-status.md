# PATCH /payments//status

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces aktualizácie stavu platby v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť bezpečnú zmenu stavu platby podľa výsledku spracovania platobnej požiadavky.

Zabezpečiť, aby stav platby bol aktualizovaný kontrolovaným spôsobom a aby jednotlivé moduly systému nemenili platobné údaje mimo definovaného procesu.

---

# Endpoint

PATCH /payments/{id}/status

---

# HTTP Metóda

PATCH

---

# URL

/api/v1/payments/{id}/status

---

# Popis

Endpoint aktualizuje stav existujúcej platby podľa výsledku platobného procesu.

Zmenu stavu koordinuje Restaurant Assistant na základe informácií získaných od Payment Agenta.

Payment Agent komunikuje s platobným poskytovateľom, spracuje výsledok a odošle informáciu Restaurant Assistantovi.

Payments API následne uloží nový stav platby.

---

# Kto môže volať API

- Restaurant Assistant
- Administrátor systému

---

# Vstupné údaje (Request)

Požiadavka obsahuje:

- Payment ID
- Nový stav platby
- Čas aktualizácie
- Dôvod zmeny (voliteľné)
- Referencia platobnej transakcie (voliteľné)

---

# Workflow

1. Payment Agent komunikuje s platobným poskytovateľom.
2. Platobný poskytovateľ vráti výsledok spracovania platby.
3. Payment Agent odošle výsledok Restaurant Assistantovi.
4. Restaurant Assistant overí výsledok a rozhodne o ďalšom kroku.
5. Restaurant Assistant odošle požiadavku na aktualizáciu stavu platby.
6. Payments API overí oprávnenie požiadavky.
7. Payments Database aktualizuje stav platby.
8. Systém zaznamená zmenu do auditu.
9. Restaurant Assistant pokračuje v ďalšom procese objednávky podľa výsledku platby.

---

# Zapojení AI agenti

## Restaurant Assistant

- Koordinuje zmenu stavu platby.
- Overuje výsledok platby.
- Riadi ďalší proces objednávky.

## Payment Agent

- Komunikuje s platobným poskytovateľom.
- Spracováva výsledok platby.
- Informuje Restaurant Assistant.

---

# Povolené stavy platby

## Pending

Platba bola vytvorená, ale ešte nebola spracovaná.

---

## Processing

Platba sa aktuálne spracováva u platobného poskytovateľa.

---

## Completed

Platba bola úspešne dokončená.

---

## Failed

Platba nebola úspešne dokončená.

---

## Cancelled

Platba bola zrušená systémom alebo používateľom.

---

# Povolené prechody stavov

Platba môže prejsť:

Pending → Processing

Processing → Completed

Processing → Failed

Pending → Cancelled

Processing → Cancelled

---

# Odpoveď systému (Response)

Úspešná odpoveď obsahuje:

- Payment ID
- Order ID
- Aktuálny stav platby
- Predchádzajúci stav platby
- Čas aktualizácie
- Výsledok operácie

---

# Chybové stavy

- Platba neexistuje.
- Neplatný stav platby.
- Neplatný prechod medzi stavmi.
- Používateľ nemá oprávnenie meniť stav.
- Platba už bola dokončená.
- Interná chyba systému.

---

# Audit

Systém zaznamenáva:

- pôvodný stav platby,
- nový stav platby,
- čas zmeny,
- kto vykonal zmenu,
- dôvod zmeny,
- výsledok operácie.

---

# Bezpečnosť

- Autorizácia požiadavky.
- Kontrola oprávnení.
- Validácia povolených stavov.
- Ochrana platobných údajov.
- Logovanie všetkých zmien.

---

# Business pravidlá

- Stav platby môže meniť iba autorizovaný proces.
- Payment Agent nemení stav platby priamo.
- Restaurant Assistant koordinuje zmenu stavu.
- Jedna objednávka má iba jednu platbu.
- Jedna platba predstavuje iba jeden platobný pokus.
- Po stave Completed nie je možné platbu zmeniť na nový platobný stav.
- Platba nemení stav objednávky priamo.
- Zmena objednávky prebieha cez Orders API.

---

# Súvisiace dokumenty

- POST /payments
- GET /payments/{id}
- GET /payments
- POST /orders
- PATCH /orders/{id}/status
- Payments Database
- Payment Workflow
- AI Agent Communication

---

# Budúce rozšírenia

- Refundácie.
- Čiastočné vrátenie platby.
- Automatické riešenie sporov.
- Viac platobných poskytovateľov.
- História všetkých platobných udalostí.

---

# Stav dokumentu

🟢 Hotový
