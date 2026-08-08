# PATCH /products/

## Verzia dokumentu

v1.0

---

# Účel endpointu

Upraviť existujúci produkt v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť administrátorovi bezpečne aktualizovať údaje existujúceho produktu.

Zabezpečiť, aby zmeny produktov boli kontrolované a aby AI agenti nemohli samostatne meniť oficiálne údaje produktov.

---

# HTTP Metóda

PATCH

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

Požiadavka môže obsahovať údaje, ktoré chce administrátor aktualizovať:

- Názov produktu
- Popis produktu
- Kategóriu
- Predajnú cenu
- Menu
- Alergény
- Zloženie produktu
- Dostupnosť

Nie je potrebné posielať všetky údaje produktu.

---

# Response

Úspešná odpoveď obsahuje:

- Product ID
- Aktualizované údaje produktu
- Dátum poslednej úpravy

---

# HTTP Status Codes

| Kód | Popis                                                |
| ---- | ---------------------------------------------------- |
| 200  | Produkt bol úspešne aktualizovaný                 |
| 400  | Neplatné vstupné údaje                            |
| 401  | Neautorizovaná požiadavka                          |
| 403  | Nedostatočné oprávnenia                           |
| 404  | Produkt neexistuje                                   |
| 409  | Aktualizácia je v konflikte s existujúcimi údajmi |
| 500  | Interná chyba systému                              |

---

# Business pravidlá

- Produkt môže upravovať iba administrátor systému.
- AI agenti nemôžu samostatne meniť údaje produktu.
- Administrátor môže upraviť iba existujúci produkt.
- Product ID sa počas aktualizácie nemení.
- Cena produktu môže byť zmenená iba administrátorom.
- Zloženie produktu môže byť zmenené iba administrátorom.
- Individuálne úpravy produktu zákazníkom nemenia produkt uložený v Products Database.
- Každá významná zmena produktu musí byť zaznamenaná v audite.
- Zmena stavu produktu sa rieši prostredníctvom samostatného endpointu PATCH /products/{id}/status.

---

# Súvisiace dokumenty

- POST /products
- GET /products/{id}
- GET /products
- PATCH /products/{id}/status
- Products Database
- Orders API
- Inventory API

---

# Budúce rozšírenia

- História zmien produktu.
- Plánované zmeny cien.
- Hromadná úprava produktov.
- Automatické návrhy zmien pomocou AI s povinným schválením administrátorom.

---

# Stav dokumentu

🟢 Hotový
