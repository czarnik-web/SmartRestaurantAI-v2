# GET /notifications/

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať detail konkrétneho upozornenia podľa jeho jedinečného identifikátora.

---

# Business cieľ

Umožniť oprávneným používateľom a interným systémom bezpečne zobraziť detail konkrétneho upozornenia.

Zabezpečiť, aby boli informácie o upozorneniach dostupné iba oprávneným používateľom a systémovým procesom.

---

# HTTP Metóda

GET

---

# URL

/api/v1/notifications/{id}

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                                  |
| --------- | ---- | -------- | -------------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor upozornenia |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Používateľ alebo interný systém odošle požiadavku na získanie detailu upozornenia.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Notifications Database vyhľadá upozornenie podľa Notification ID.
4. Systém overí, či má žiadateľ oprávnenie zobraziť dané upozornenie.
5. Systém vráti detail upozornenia.

---

# Kto môže volať API

- Restaurant Assistant
- Notification Agent
- Administrátor systému
- Zákazník (iba vlastné upozornenia)

---

# Response

Úspešná odpoveď obsahuje:

- Notification ID
- Identifikátor príjemcu
- Typ upozornenia
- Obsah správy
- Súvisiace Order ID (ak existuje)
- Stav upozornenia
- Kanál odoslania
- Čas vytvorenia
- Čas odoslania

---

# HTTP Status Codes

| Kód | Popis                                  |
| ---- | -------------------------------------- |
| 200  | Upozornenie bolo úspešne načítané |
| 400  | Neplatný identifikátor upozornenia   |
| 401  | Neautorizovaná požiadavka            |
| 403  | Nedostatočné oprávnenia             |
| 404  | Upozornenie neexistuje                 |
| 500  | Interná chyba systému                |

---

# Business pravidlá

- Zákazník môže zobraziť iba vlastné upozornenia.
- Restaurant Assistant môže zobraziť upozornenia potrebné na koordináciu procesu.
- Notification Agent môže zobraziť údaje potrebné na spracovanie a kontrolu upozornenia.
- Administrátor môže zobraziť údaje podľa pridelených oprávnení.
- Upozornenie nesmie obsahovať údaje o cudzej objednávke.
- Notifications API nemení stav objednávky, platby ani iných business objektov.
- Citlivé interné údaje systému nie sú dostupné zákazníkovi.

---

# Súvisiace dokumenty

- POST /notifications
- GET /notifications
- Notifications Workflow
- Orders API
- Payments API
- Kitchen API

---

# Budúce rozšírenia

- História pokusov o doručenie.
- Detailné informácie o výsledku doručenia.
- Podpora viacerých komunikačných kanálov.
- Preferencie upozornení zákazníka.

---

# Stav dokumentu

🟢 Hotový
