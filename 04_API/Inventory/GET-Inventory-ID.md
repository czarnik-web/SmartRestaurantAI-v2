# GET /inventory/

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať detail konkrétnej skladovej položky podľa jej jedinečného identifikátora.

---

# Business cieľ

Umožniť oprávneným používateľom a interným systémom zobraziť aktuálne informácie o konkrétnej skladovej položke.

Zabezpečiť presný prehľad o stave zásob bez zásahu do ostatných business domén.

---

# HTTP Metóda

GET

---

# URL

/api/v1/inventory/{id}

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                                         |
| --------- | ---- | -------- | --------------------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor skladovej položky |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo interný systém odošle požiadavku na získanie detailu skladovej položky.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Inventory Database vyhľadá skladovú položku podľa Inventory Item ID.
4. Systém overí rozsah údajov podľa oprávnení.
5. Systém vráti detail skladovej položky.

---

# Kto môže volať API

- Restaurant Assistant
- Inventory Agent
- Kitchen Agent
- Administrátor systému
- Oprávnený personál

---

# Response

Úspešná odpoveď obsahuje:

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

| Kód | Popis                                         |
| ---- | --------------------------------------------- |
| 200  | Skladová položka bola úspešne načítaná |
| 400  | Neplatný identifikátor skladovej položky   |
| 401  | Neautorizovaná požiadavka                   |
| 403  | Nedostatočné oprávnenia                    |
| 404  | Skladová položka neexistuje                 |
| 500  | Interná chyba systému                       |

---

# Business pravidlá

- Endpoint slúži iba na čítanie údajov.
- Inventory Agent môže zobraziť údaje potrebné na správu skladu.
- Kitchen Agent môže zobraziť údaje potrebné na overenie dostupnosti surovín.
- Restaurant Assistant môže zobraziť údaje potrebné na koordináciu procesu objednávky.
- Administrátor a oprávnený personál môžu zobraziť údaje podľa pridelených oprávnení.
- Inventory API pracuje iba s údajmi skladovej domény.
- Údaje o produktoch, objednávkach alebo platbách poskytujú samostatné moduly.

---

# Súvisiace dokumenty

- GET /inventory
- PATCH /inventory/{id}
- Inventory Database
- Inventory Workflow
- Products API
- Orders API
- AI Agent Communication

---

# Budúce rozšírenia

- História pohybov skladovej položky.
- Informácie o expirácii.
- Informácie o dodávateľovi.
- Viac skladov.
- AI predikcia spotreby.

---

# Stav dokumentu

🟢 Hotový
