# GET /notifications

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať zoznam upozornení podľa oprávnení používateľa alebo systémového modulu.

---

# Business cieľ

Umožniť bezpečný prístup k zoznamu upozornení zákazníkom, administrátorom a interným systémovým procesom.

Zabezpečiť, aby každý používateľ alebo modul získal iba upozornenia, ku ktorým má oprávnenie.

---

# HTTP Metóda

GET

---

# URL

/api/v1/notifications

---

# Query Parameters

| Parameter | Typ     | Povinný | Popis                                      |
| --------- | ------- | -------- | ------------------------------------------ |
| type      | String  | Nie      | Filtrovanie podľa typu upozornenia        |
| status    | String  | Nie      | Filtrovanie podľa stavu upozornenia       |
| order_id  | UUID    | Nie      | Filtrovanie podľa súvisiacej objednávky |
| from_date | Date    | Nie      | Začiatok časového obdobia               |
| to_date   | Date    | Nie      | Koniec časového obdobia                  |
| page      | Integer | Nie      | Číslo stránky výsledkov                |
| limit     | Integer | Nie      | Počet výsledkov na stránku              |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo interný systém odošle požiadavku na získanie zoznamu upozornení.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Systém určí rozsah upozornení dostupných pre žiadateľa.
4. Notifications Database vyhľadá upozornenia podľa zadaných filtrov.
5. Systém vráti zoznam povolených upozornení.

---

# Kto môže volať API

- Restaurant Assistant
- Notification Agent
- Administrátor systému
- Zákazník (iba vlastné upozornenia)

---

# Response

Úspešná odpoveď obsahuje zoznam upozornení.

Každé upozornenie môže obsahovať:

- Notification ID
- Typ upozornenia
- Stav upozornenia
- Súvisiace Order ID (ak existuje)
- Kanál odoslania
- Čas vytvorenia
- Čas odoslania

Rozsah zobrazených údajov závisí od oprávnení používateľa alebo systémového modulu.

---

# HTTP Status Codes

| Kód | Popis                                        |
| ---- | -------------------------------------------- |
| 200  | Zoznam upozornení bol úspešne načítaný |
| 400  | Neplatné parametre požiadavky              |
| 401  | Neautorizovaná požiadavka                  |
| 403  | Nedostatočné oprávnenia                   |
| 500  | Interná chyba systému                      |

---

# Business pravidlá

- Používateľ vidí iba upozornenia, ku ktorým má oprávnenie.
- Zákazník môže zobraziť iba vlastné upozornenia.
- Restaurant Assistant môže zobraziť upozornenia potrebné na koordináciu procesu.
- Notification Agent môže zobraziť údaje potrebné na správu a kontrolu upozornení.
- Administrátor môže zobraziť údaje podľa pridelených oprávnení.
- Zákazník nesmie získať upozornenia iného zákazníka.
- Notifications API nemení stav objednávky, platby ani iných business objektov.
- Citlivé interné údaje systému nie sú dostupné zákazníkovi.

---

# Súvisiace dokumenty

- POST /notifications
- GET /notifications/{id}
- Notifications Workflow
- Orders API
- Payments API
- Kitchen API

---

# Budúce rozšírenia

- Pokročilé filtrovanie upozornení.
- História pokusov o doručenie.
- Preferencie upozornení zákazníka.
- Podpora ďalších komunikačných kanálov.
- Archivácia starších upozornení.

---

# Stav dokumentu

🟢 Hotový
