# GET /orders

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces získania zoznamu objednávok podľa oprávnení používateľa a potrieb jednotlivých systémových modulov.

---

# Business cieľ

Umožniť bezpečný prístup k zoznamu objednávok zákazníkom, personálu a interným systémom podľa ich oprávnení.

Zabezpečiť, aby každý používateľ alebo modul získal iba údaje potrebné pre svoju činnosť.

---

# Endpoint

GET /orders

---

# HTTP Metóda

GET

---

# URL

/api/v1/orders

---

# Popis

Endpoint vráti zoznam objednávok podľa oprávnení používateľa, role systému a zadaných filtrov.

Prístup k objednávkam je riadený systémom autorizácie.

Restaurant Assistant môže získavať aktívne objednávky potrebné na koordináciu prevádzky.

---

# Kto môže volať API

- Web aplikácia
- Mobilná aplikácia
- Restaurant Assistant
- Administrátor systému
- Interné systémové moduly podľa oprávnení

---

# Query Parameters

| Parameter   | Typ     | Povinný | Popis                                |
| ----------- | ------- | -------- | ------------------------------------ |
| status      | String  | Nie      | Filtrovanie podľa stavu objednávky |
| customer_id | UUID    | Nie      | Filtrovanie podľa zákazníka       |
| from_date   | Date    | Nie      | Začiatok časového obdobia         |
| to_date     | Date    | Nie      | Koniec časového obdobia            |
| page        | Integer | Nie      | Číslo stránky                     |
| limit       | Integer | Nie      | Počet výsledkov                    |

---

# Vstupné údaje (Request)

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo systém odošle požiadavku na získanie objednávok.
2. Systém overí identitu a oprávnenia používateľa.
3. Systém určí rozsah objednávok, ktoré môže používateľ alebo modul zobraziť.
4. Orders Database vyhľadá povolené objednávky.
5. Systém vráti výsledky podľa nastavených filtrov.
6. Reporting Agent môže zaznamenať využitie údajov podľa potreby systému.

---

# Prístupové pravidlá

## Zákazník

Môže zobraziť:

- vlastné objednávky,
- stav svojich objednávok,
- základné informácie o objednávkach.

Nemôže zobraziť:

- objednávky iných zákazníkov,
- interné údaje reštaurácie.

---

## Restaurant Assistant

Môže zobraziť:

- aktívne objednávky potrebné na koordináciu prevádzky,
- stav spracovania objednávok.

---

## Administrátor systému

Môže zobraziť údaje podľa pridelených oprávnení.

---

# Odpoveď systému (Response)

Úspešná odpoveď obsahuje zoznam objednávok:

- Order ID
- Stav objednávky
- Typ objednávky
- Celková cena
- Čas vytvorenia objednávky
- Posledná aktualizácia

---

# Chybové stavy

- Používateľ nie je autentifikovaný.
- Používateľ nemá oprávnenie zobraziť objednávky.
- Neplatné filtračné parametre.
- Interná chyba systému.

---

# Audit

Systém zaznamenáva:

- kto požiadal o zoznam objednávok,
- čas požiadavky,
- rozsah poskytnutých údajov.

---

# Bezpečnosť

- Autorizácia používateľa.
- Kontrola oprávnení podľa role.
- Obmedzenie prístupu k citlivým údajom.
- Ochrana pred získaním údajov iných zákazníkov.
- Logovanie prístupov k objednávkam.

---

# Business pravidlá

- Používateľ vidí iba objednávky, ku ktorým má oprávnenie.
- Zákazník nikdy nemôže získať objednávky iného zákazníka.
- Restaurant Assistant má prístup iba k údajom potrebným na koordináciu prevádzky.
- Endpoint pracuje iba s Orders doménou.
- Informácie o platbách, sklade, kuchyni alebo reportingu poskytujú samostatné moduly.
- Objednávky sa v systéme fyzicky neodstraňujú.

---

# Súvisiace dokumenty

- Orders Workflow
- Orders Database
- POST /orders
- GET /orders/{id}
- PATCH /orders/{id}/status
- Restaurant Assistant Architecture
- AI Agent Communication

---

# Budúce rozšírenia

- Pokročilé filtrovanie objednávok.
- Vyhľadávanie podľa zákazníka alebo produktu.
- AI odporúčanie priorít spracovania.
- Automatické triedenie objednávok podľa naliehavosti.

---

# Stav dokumentu

🟢 Hotový
