# PATCH /products//status

## Verzia dokumentu

v1.0

---

# Účel endpointu

Zmeniť stav existujúceho produktu v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť administrátorovi bezpečne aktivovať alebo deaktivovať produkt bez jeho odstránenia zo systému.

Zabezpečiť, aby neaktívne produkty neboli dostupné zákazníkom na objednanie, ale zostali zachované v systéme.

---

# HTTP Metóda

PATCH

---

# URL

/api/v1/products/{id}/status

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                               |
| --------- | ---- | -------- | ----------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor produktu |

---

# Request Body

Požiadavka obsahuje:

- Nový stav produktu

Povolené stavy:

- Active
- Inactive

---

# Response

Úspešná odpoveď obsahuje:

- Product ID
- Predchádzajúci stav produktu
- Aktuálny stav produktu
- Dátum poslednej aktualizácie

---

# HTTP Status Codes

| Kód | Popis                                      |
| ---- | ------------------------------------------ |
| 200  | Stav produktu bol úspešne aktualizovaný |
| 400  | Neplatný stav produktu                    |
| 401  | Neautorizovaná požiadavka                |
| 403  | Nedostatočné oprávnenia                 |
| 404  | Produkt neexistuje                         |
| 500  | Interná chyba systému                    |

---

# Business pravidlá

- Stav produktu môže meniť iba administrátor systému.
- AI agenti nemôžu samostatne meniť stav produktu.
- Produkt môže byť v stave Active alebo Inactive.
- Aktívny produkt môže byť dostupný zákazníkom na objednanie.
- Neaktívny produkt nie je dostupný zákazníkom na objednanie.
- Neaktívny produkt zostáva zachovaný v Products Database.
- Deaktivácia produktu neodstraňuje jeho historické väzby na existujúce objednávky.
- Restaurant Assistant nemôže vytvoriť novú objednávku s neaktívnym produktom.
- Každá zmena stavu produktu musí byť zaznamenaná v audite.
- Dočasná nedostupnosť produktu z dôvodu nedostatku surovín sa rieši prostredníctvom dostupnosti produktu a nemení jeho stav na Inactive.

---

# Súvisiace dokumenty

- POST /products
- GET /products/{id}
- GET /products
- PATCH /products/{id}
- Products Database
- Orders API
- Inventory API

---

# Budúce rozšírenia

- Plánovaná automatická aktivácia a deaktivácia produktov.
- Dočasné sezónne produkty.
- Archivácia produktov.
- História zmien stavu produktu.

---

# Stav dokumentu

🟢 Hotový
