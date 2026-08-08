# GET /products

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať zoznam produktov dostupných v systéme Smart Restaurant AI podľa oprávnení používateľa a zadaných filtrov.

---

# Business cieľ

Umožniť bezpečný prístup k zoznamu produktov pre zákazníkov, personál a AI agentov.

Zabezpečiť, aby každý používateľ alebo AI agent získal iba produkty a informácie, ku ktorým má oprávnenie.

---

# HTTP Metóda

GET

---

# URL

/api/v1/products

---

# Query Parameters

| Parameter | Typ     | Povinný | Popis                                 |
| --------- | ------- | -------- | ------------------------------------- |
| category  | String  | Nie      | Filtrovanie podľa kategórie         |
| available | Boolean | Nie      | Zobraziť iba dostupné produkty      |
| search    | String  | Nie      | Vyhľadávanie podľa názvu produktu |
| page      | Integer | Nie      | Číslo stránky výsledkov           |
| limit     | Integer | Nie      | Počet produktov na stránku          |
| sort      | String  | Nie      | Triedenie výsledkov                  |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo AI agent odošle požiadavku na získanie zoznamu produktov.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Products Database vyhľadá produkty podľa zadaných filtrov.
4. Systém odstráni produkty, ku ktorým používateľ nemá oprávnenie.
5. Systém vráti zoznam produktov.

---

# Kto môže volať API

- Restaurant Assistant
- Kitchen Agent
- Inventory Agent
- Marketing Agent
- Web aplikácia
- Mobilná aplikácia
- Administrátor systému
- Zákazník

---

# Response

Úspešná odpoveď obsahuje zoznam produktov.

Každý produkt môže obsahovať:

- Product ID
- Názov produktu
- Popis produktu
- Kategóriu
- Predajnú cenu
- Dostupnosť produktu
- Stav produktu

Rozsah zobrazených údajov závisí od oprávnenia používateľa alebo AI agenta.

---

# HTTP Status Codes

| Kód | Popis                                  |
| ---- | -------------------------------------- |
| 200  | Zoznam produktov úspešne načítaný |
| 400  | Neplatné parametre požiadavky        |
| 401  | Neautorizovaná požiadavka            |
| 403  | Nedostatočné oprávnenia             |
| 500  | Interná chyba systému                |

---

# Business pravidlá

- Zákazník môže zobraziť iba aktívne produkty.
- Restaurant Assistant môže zobraziť iba produkty dostupné pre objednávky.
- Kitchen Agent môže zobraziť produkty potrebné na prípravu jedál.
- Inventory Agent môže zobraziť produkty potrebné pre správu skladu.
- Marketing Agent môže zobraziť produkty podľa pridelených oprávnení.
- Administrátor môže zobraziť všetky produkty vrátane neaktívnych.
- Rozsah zobrazených údajov závisí od oprávnenia používateľa alebo AI agenta.

---

# Súvisiace dokumenty

- POST /products
- GET /products/{id}
- PATCH /products/{id}
- PATCH /products/{id}/status
- Products Database
- Orders API
- Inventory API
- AI Agent Communication

---

# Budúce rozšírenia

- Pokročilé filtrovanie produktov.
- Fulltextové vyhľadávanie.
- AI odporúčanie produktov.
- Personalizované odporúčania podľa histórie objednávok.
- Zobrazenie hodnotení produktov.

---

# Stav dokumentu

🟢 Hotový
