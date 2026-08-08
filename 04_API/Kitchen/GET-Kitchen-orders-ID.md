# GET /kitchen/orders/

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať detail konkrétnej objednávky určenej na spracovanie v kuchyni podľa jej jedinečného identifikátora.

---

# Business cieľ

Umožniť kuchyni, Kitchen Agentovi a Restaurant Assistantovi zobraziť všetky informácie potrebné na správnu prípravu konkrétnej objednávky.

Zabezpečiť, aby Kitchen API pracovalo iba s údajmi potrebnými pre proces prípravy objednávky.

---

# HTTP Metóda

GET

---

# URL

/api/v1/kitchen/orders/{id}

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                                  |
| --------- | ---- | -------- | -------------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor objednávky |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Response

Úspešná odpoveď obsahuje:

- Order ID
- Stav prípravy objednávky
- Produkty určené na prípravu
- Množstvo jednotlivých produktov
- Úpravy produktov požadované zákazníkom
- Poznámku k objednávke
- Typ objednávky
- Čas prijatia objednávky
- Čas poslednej aktualizácie

Endpoint poskytuje iba údaje potrebné na spracovanie objednávky v kuchyni.

---

# HTTP Status Codes

| Kód | Popis                                                      |
| ---- | ---------------------------------------------------------- |
| 200  | Objednávka bola úspešne načítaná                     |
| 400  | Neplatný identifikátor objednávky                       |
| 401  | Neautorizovaná požiadavka                                |
| 403  | Nedostatočné oprávnenia                                 |
| 404  | Objednávka neexistuje alebo nie je dostupná pre kuchyňu |
| 500  | Interná chyba systému                                    |

---

# Business pravidlá

- Kitchen API poskytuje iba údaje potrebné na prípravu objednávky.
- Kitchen Agent môže zobraziť objednávky určené na spracovanie v kuchyni.
- Restaurant Assistant môže zobraziť údaje potrebné na koordináciu procesu.
- Oprávnený personál kuchyne môže zobraziť objednávky určené na prípravu.
- Individuálne úpravy požadované zákazníkom musia byť zobrazené spolu s konkrétnym produktom.
- Kitchen API nemení údaje produktu v Products Database.
- Kitchen API nemení platobné údaje.
- Zmena hlavného stavu objednávky prebieha prostredníctvom Restaurant Assistant a Orders API.
- Objednávky, ktoré nie sú určené na spracovanie v kuchyni, nie sú cez tento endpoint dostupné.

---

# Súvisiace dokumenty

- Kitchen Workflow
- Orders API
- Products API
- Inventory API
- GET /kitchen/orders
- PATCH /kitchen/orders/{id}/status

---

# Budúce rozšírenia

- Sledovanie stavu jednotlivých položiek objednávky.
- Rozdelenie objednávok podľa kuchynských pracovísk.
- AI prioritizácia objednávok.
- Presnejší odhad času prípravy.

---

# Stav dokumentu

🟢 Hotový
