# GET /payments

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces získania zoznamu platieb podľa oprávnení používateľa alebo systémového modulu v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť bezpečný prístup k zoznamu platieb podľa potrieb jednotlivých používateľov a systémových komponentov.

Zabezpečiť, aby každý používateľ alebo modul získal iba údaje potrebné pre svoju činnosť.

---

# Endpoint

GET /payments

---

# HTTP Metóda

GET

---

# URL

/api/v1/payments

---

# Popis

Endpoint vráti zoznam platieb podľa oprávnení používateľa a zadaných filtrov.

Prístup k platobným údajom je riadený systémom autorizácie.

Payments modul poskytuje iba informácie o platbách a nemení stav objednávok ani neovplyvňuje proces objednávky.

---

# Kto môže volať API

- Restaurant Assistant
- Payment Agent
- Administrátor systému
- Zákazník (iba vlastné platby)

---

# Query Parameters

| Parameter   | Typ     | Povinný | Popis                           |
| ----------- | ------- | -------- | ------------------------------- |
| status      | String  | Nie      | Filtrovanie podľa stavu platby |
| order_id    | UUID    | Nie      | Filtrovanie podľa objednávky  |
| customer_id | UUID    | Nie      | Filtrovanie podľa zákazníka  |
| from_date   | Date    | Nie      | Začiatok časového obdobia    |
| to_date     | Date    | Nie      | Koniec časového obdobia       |
| page        | Integer | Nie      | Číslo stránky výsledkov     |
| limit       | Integer | Nie      | Počet výsledkov               |

---

# Vstupné údaje (Request)

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo systém odošle požiadavku na získanie zoznamu platieb.
2. Systém overí identitu a oprávnenie požiadavky.
3. Systém určí rozsah platieb, ktoré môže žiadateľ zobraziť.
4. Payments Database vyhľadá povolené platby podľa filtrov.
5. Systém vráti zoznam dostupných platieb.
6. Systém zaznamená požiadavku do auditu.

---

# Prístupové pravidlá

## Zákazník

Môže zobraziť:

- vlastné platby,
- stav vlastných platieb,
- základné informácie o transakciách.

Nemôže zobraziť:

- platby iných zákazníkov,
- interné platobné údaje systému.

---

## Restaurant Assistant

Môže zobraziť:

- platby súvisiace s objednávkami potrebnými na koordináciu prevádzky.

---

## Payment Agent

Môže zobraziť:

- platby potrebné na spracovanie a kontrolu platobného procesu.

---

## Administrátor systému

Môže zobraziť údaje podľa pridelených oprávnení.

---

# Odpoveď systému (Response)

Úspešná odpoveď obsahuje zoznam platieb.

Každá platba obsahuje:

- Payment ID
- Order ID
- Stav platby
- Celkovú sumu
- Mena
- Spôsob platby
- Čas vytvorenia platby
- Čas poslednej aktualizácie

---

# Možné stavy platby

- Pending
- Processing
- Completed
- Failed
- Cancelled

---

# Chybové stavy

- Používateľ nie je autentifikovaný.
- Používateľ nemá oprávnenie zobraziť platby.
- Neplatné filtračné parametre.
- Interná chyba systému.

---

# Audit

Systém zaznamenáva:

- kto požiadal o zoznam platieb,
- čas požiadavky,
- použité filtre,
- rozsah poskytnutých údajov,
- výsledok požiadavky.

---

# Bezpečnosť

- Autorizácia požiadavky.
- Kontrola oprávnení podľa role.
- Ochrana platobných údajov.
- Zamedzenie prístupu k cudzím platbám.
- Logovanie prístupov k platbám.

---

# Business pravidlá

- Používateľ vidí iba platby, ku ktorým má oprávnenie.
- Zákazník nikdy nemôže získať platby iného zákazníka.
- Payments modul poskytuje iba informácie o platbách.
- Payments modul nemení stav objednávky.
- Jedna objednávka má iba jednu platbu.
- Jedna platba predstavuje iba jeden platobný pokus.
- Citlivé platobné údaje nie sú dostupné cez API.

---

# Súvisiace dokumenty

- POST /payments
- GET /payments/{id}
- PATCH /payments/{id}/status
- Payments Database
- Payment Workflow
- Orders API
- AI Agent Communication

---

# Budúce rozšírenia

- Pokročilé filtrovanie platieb.
- Finančné reportovanie.
- Export platobných údajov.
- Analýza platobného správania.
- Prepojenie s fakturačným systémom.

---

# Stav dokumentu

🟢 Hotový
