# GET /kitchen/orders

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať zoznam objednávok určených na spracovanie v kuchyni podľa oprávnení a zadaných filtrov.

---

# Business cieľ

Umožniť Kitchen Agentovi, Restaurant Assistantovi a oprávnenému personálu kuchyne zobraziť aktuálne objednávky potrebné na prípravu.

Zabezpečiť prehľad o stave kuchynských objednávok bez prístupu k údajom, ktoré nie sú potrebné pre proces prípravy.

---

# HTTP Metóda

GET

---

# URL

/api/v1/kitchen/orders

---

# Query Parameters

| Parameter | Typ     | Povinný | Popis                                          |
| --------- | ------- | -------- | ---------------------------------------------- |
| status    | String  | Nie      | Filtrovanie podľa stavu prípravy objednávky |
| from_date | Date    | Nie      | Začiatok časového obdobia                   |
| to_date   | Date    | Nie      | Koniec časového obdobia                      |
| page      | Integer | Nie      | Číslo stránky výsledkov                    |
| limit     | Integer | Nie      | Počet výsledkov na stránku                  |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo interný systém odošle požiadavku na získanie zoznamu kuchynských objednávok.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Systém určí rozsah objednávok dostupných pre kuchyňu.
4. Systém vyhľadá objednávky podľa zadaných filtrov.
5. Systém vráti zoznam objednávok určených na prípravu.

---

# Kto môže volať API

- Kitchen Agent
- Restaurant Assistant
- Oprávnený personál kuchyne
- Administrátor systému

---

# Response

Úspešná odpoveď obsahuje zoznam objednávok určených na spracovanie v kuchyni.

Každá objednávka môže obsahovať:

- Order ID
- Stav prípravy objednávky
- Produkty určené na prípravu
- Množstvo jednotlivých produktov
- Úpravy produktov požadované zákazníkom
- Poznámku k objednávke
- Typ objednávky
- Čas prijatia objednávky
- Čas poslednej aktualizácie

---

# HTTP Status Codes

| Kód | Popis                                        |
| ---- | -------------------------------------------- |
| 200  | Zoznam objednávok bol úspešne načítaný |
| 400  | Neplatné parametre požiadavky              |
| 401  | Neautorizovaná požiadavka                  |
| 403  | Nedostatočné oprávnenia                   |
| 500  | Interná chyba systému                      |

---

# Business pravidlá

- Endpoint vracia iba objednávky určené na spracovanie v kuchyni.
- Kitchen Agent môže zobraziť objednávky potrebné na riadenie prípravy.
- Restaurant Assistant môže zobraziť objednávky potrebné na koordináciu prevádzky.
- Oprávnený personál kuchyne môže zobraziť objednávky určené na prípravu.
- Individuálne úpravy zákazníka musia byť viditeľné pri konkrétnych produktoch.
- Kitchen API neposkytuje platobné údaje.
- Kitchen API nemení údaje produktu v Products Database.
- Zmena hlavného stavu objednávky prebieha prostredníctvom Restaurant Assistant a Orders API.

---

# Súvisiace dokumenty

- GET /kitchen/orders/{id}
- PATCH /kitchen/orders/{id}/status
- Kitchen Workflow
- Orders API
- Products API
- Inventory API

---

# Budúce rozšírenia

- Filtrovanie podľa kuchynského pracoviska.
- Prioritizácia objednávok.
- Sledovanie stavu jednotlivých položiek.
- AI optimalizácia poradia prípravy.

---

# Stav dokumentu

🟢 Hotový
