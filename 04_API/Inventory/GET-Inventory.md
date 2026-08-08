# GET /inventory

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať zoznam skladových položiek podľa oprávnení používateľa a zadaných filtrov.

---

# Business cieľ

Umožniť oprávneným používateľom a interným systémom bezpečne zobraziť aktuálny stav skladových zásob.

Zabezpečiť prehľad o dostupnosti položiek bez zásahu do ostatných business domén.

---

# HTTP Metóda

GET

---

# URL

/api/v1/inventory

---

# Query Parameters

| Parameter | Typ     | Povinný | Popis                                       |
| --------- | ------- | -------- | ------------------------------------------- |
| status    | String  | Nie      | Filtrovanie podľa stavu skladovej položky |
| available | Boolean | Nie      | Filtrovanie podľa dostupnosti              |
| search    | String  | Nie      | Vyhľadávanie podľa názvu položky       |
| page      | Integer | Nie      | Číslo stránky výsledkov                 |
| limit     | Integer | Nie      | Počet výsledkov na stránku               |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo interný systém odošle požiadavku na získanie zoznamu skladových položiek.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Systém určí rozsah údajov podľa oprávnení.
4. Inventory Database vyhľadá skladové položky podľa zadaných filtrov.
5. Systém vráti zoznam skladových položiek.

---

# Kto môže volať API

- Restaurant Assistant
- Inventory Agent
- Kitchen Agent
- Administrátor systému
- Oprávnený personál

---

# Response

Úspešná odpoveď obsahuje zoznam skladových položiek.

Každá položka môže obsahovať:

- Inventory Item ID
- Názov položky
- Typ položky
- Aktuálne množstvo
- Minimálne množstvo
- Mernú jednotku
- Dostupnosť
- Stav položky
- Dátum poslednej aktualizácie

Rozsah zobrazených údajov závisí od oprávnení používateľa alebo interného systému.

---

# HTTP Status Codes

| Kód | Popis                                                  |
| ---- | ------------------------------------------------------ |
| 200  | Zoznam skladových položiek bol úspešne načítaný |
| 400  | Neplatné parametre požiadavky                        |
| 401  | Neautorizovaná požiadavka                            |
| 403  | Nedostatočné oprávnenia                             |
| 500  | Interná chyba systému                                |

---

# Business pravidlá

- Používateľ alebo interný systém vidí iba údaje, ku ktorým má oprávnenie.
- Inventory Agent môže zobraziť údaje potrebné na správu skladu.
- Kitchen Agent môže zobraziť údaje potrebné na overenie dostupnosti surovín.
- Restaurant Assistant môže zobraziť údaje potrebné na koordináciu prevádzky.
- Administrátor a oprávnený personál môžu zobraziť údaje podľa pridelených oprávnení.
- Inventory API pracuje iba s údajmi skladovej domény.
- Údaje o produktoch, objednávkach alebo platbách poskytujú samostatné moduly.

---

# Súvisiace dokumenty

- GET /inventory/{id}
- PATCH /inventory/{id}
- Inventory Database
- Inventory Workflow
- Products API
- Orders API
- AI Agent Communication

---

# Budúce rozšírenia

- Pokročilé filtrovanie skladových položiek.
- História skladových pohybov.
- Filtrovanie podľa expirácie.
- Filtrovanie podľa dodávateľa.
- Viac skladov.
- AI predikcia spotreby.

---

# Stav dokumentu

🟢 Hotový
