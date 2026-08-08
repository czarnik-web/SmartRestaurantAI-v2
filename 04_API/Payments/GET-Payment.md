# GET /payments/

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces získania detailných informácií o konkrétnej platbe podľa jej identifikátora v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť bezpečný prístup k informáciám o konkrétnej platbe používateľom a systémovým modulom podľa ich oprávnení.

Zabezpečiť oddelenie platobných údajov od ostatných častí systému.

---

# Endpoint

GET /payments/{id}

---

# HTTP Metóda

GET

---

# URL

/api/v1/payments/{id}

---

# Popis

Endpoint vráti detail jednej konkrétnej platby podľa Payment ID.

Prístup k platobným údajom je riadený podľa oprávnení používateľa alebo systémového modulu.

Payments modul poskytuje informácie o platbe, ale nemení stav objednávky ani neovplyvňuje proces objednávky.

---

# Kto môže volať API

- Restaurant Assistant
- Payment Agent
- Administrátor systému
- Zákazník (iba vlastná platba)

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                             |
| --------- | ---- | -------- | --------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor platby |

---

# Workflow

1. Používateľ alebo systém odošle požiadavku na získanie detailu platby.
2. Systém overí identitu a oprávnenie požiadavky.
3. Payments Database vyhľadá platbu podľa Payment ID.
4. Systém overí, či má žiadateľ povolený prístup k údajom.
5. Systém vráti detail platby.

---

# Prístupové pravidlá

## Zákazník

Môže zobraziť:

- vlastnú platbu,
- stav platby,
- základné informácie o transakcii.

Nemôže zobraziť:

- platby iných zákazníkov,
- interné systémové údaje.

---

## Restaurant Assistant

Môže zobraziť:

- platby súvisiace s objednávkami potrebnými na koordináciu procesu.

---

## Payment Agent

Môže zobraziť:

- údaje potrebné na spracovanie a kontrolu platby.

---

## Administrátor systému

Môže zobraziť údaje podľa pridelených oprávnení.

---

# Odpoveď systému (Response)

Úspešná odpoveď obsahuje:

- Payment ID
- Order ID
- Customer ID
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

- Platba neexistuje.
- Neplatný identifikátor platby.
- Používateľ nemá oprávnenie zobraziť platbu.
- Interná chyba systému.

---

# Audit

Systém zaznamenáva:

- kto požiadal o zobrazenie platby,
- čas požiadavky,
- identifikátor platby,
- výsledok požiadavky.

---

# Bezpečnosť

- Autorizácia požiadavky.
- Kontrola oprávnení.
- Ochrana platobných údajov.
- Zamedzenie prístupu k cudzím platbám.
- Logovanie prístupov.

---

# Business pravidlá

- Jedna platba je vždy viazaná na jednu objednávku.
- Payment ID je jednoznačne prepojené s Order ID.
- Payment modul poskytuje iba informácie o platbe.
- Payment modul nemení stav objednávky.
- Zákazník môže vidieť iba vlastné platby.
- Citlivé platobné údaje nie sú dostupné cez API.

---

# Súvisiace dokumenty

- POST /payments
- GET /payments
- PATCH /payments/{id}/status
- Payments Database
- Payment Workflow
- Orders API
- AI Agent Communication

---

# Budúce rozšírenia

- Detailná história platobných udalostí.
- Prepojenie s fakturačným systémom.
- Rozšírené finančné reportovanie.
- Automatická kontrola podozrivých transakcií.

---

# Stav dokumentu

🟢 Hotový
