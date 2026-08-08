# GET /products/

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať detail konkrétneho produktu podľa jeho jedinečného identifikátora.

---

# Business cieľ

Umožniť zákazníkom, personálu a interným systémom zobraziť detail produktu podľa pridelených oprávnení.

Zabezpečiť, aby každý používateľ alebo AI agent získal iba údaje potrebné na svoju činnosť.

---

# HTTP Metóda

GET

---

# URL

/api/v1/products/{id}

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                               |
| --------- | ---- | -------- | ----------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor produktu |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo AI agent odošle požiadavku na získanie detailu produktu.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Products Database vyhľadá produkt podľa Product ID.
4. Systém určí rozsah údajov podľa oprávnení.
5. Restaurant Assistant spracuje odpoveď, ak je súčasťou procesu objednávky.
6. Systém vráti detail produktu.

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

Úspešná odpoveď môže obsahovať:

- Product ID
- Názov produktu
- Popis produktu
- Kategóriu
- Predajnú cenu
- Menu
- Alergény
- Dostupnosť produktu
- Stav produktu
- Dátum vytvorenia
- Dátum poslednej úpravy

Rozsah zobrazených údajov závisí od oprávnenia používateľa alebo AI agenta.

---

# HTTP Status Codes

| Kód | Popis                             |
| ---- | --------------------------------- |
| 200  | Produkt úspešne načítaný     |
| 400  | Neplatný identifikátor produktu |
| 401  | Neautorizovaná požiadavka       |
| 403  | Nedostatočné oprávnenia        |
| 404  | Produkt neexistuje                |
| 500  | Interná chyba systému           |

---

# Business pravidlá

- Produkt môže vytvárať a upravovať iba administrátor systému.
- AI agenti nemôžu meniť údaje produktu.
- Restaurant Assistant môže produkt iba zobraziť a použiť pri vytváraní objednávky.
- Kitchen Agent môže zobraziť údaje potrebné na prípravu jedla.
- Inventory Agent môže zobraziť údaje potrebné na správu skladu.
- Marketing Agent môže zobraziť údaje potrebné na marketingové aktivity.
- Zákazník môže zobraziť iba verejné informácie o produkte.
- Interné údaje systému nie sú zákazníkovi dostupné.

---

# Súvisiace dokumenty

- POST /products
- GET /products
- PATCH /products/{id}
- PATCH /products/{id}/status
- Products Database
- Orders API
- Inventory API
- AI Agent Communication

---

# Budúce rozšírenia

- Nutričné hodnoty produktu.
- Fotografie produktov.
- Hodnotenie produktov zákazníkmi.
- Odporúčané produkty pomocou AI.
- Personalizované odporúčania podľa histórie objednávok.

---

# Stav dokumentu

🟢 Hotový
