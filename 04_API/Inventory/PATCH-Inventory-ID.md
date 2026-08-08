# PATCH /inventory/

## Verzia dokumentu

v1.0

---

# Účel endpointu

Aktualizovať údaje existujúcej skladovej položky v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť bezpečnú aktualizáciu údajov skladovej položky oprávneným používateľom a systémovým procesom.

Zabezpečiť, aby bol stav zásob v Inventory Database aktuálny a dostupný pre ostatné časti systému.

---

# HTTP Metóda

PATCH

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

Požiadavka môže obsahovať údaje, ktoré majú byť aktualizované:

- Aktuálne množstvo
- Minimálne množstvo
- Dostupnosť
- Stav položky

Nie je potrebné posielať všetky údaje skladovej položky.

---

# Response

Úspešná odpoveď obsahuje:

- Inventory Item ID
- Aktuálne množstvo
- Minimálne množstvo
- Dostupnosť
- Stav položky
- Dátum poslednej aktualizácie

---

# HTTP Status Codes

| Kód | Popis                                            |
| ---- | ------------------------------------------------ |
| 200  | Skladová položka bola úspešne aktualizovaná |
| 400  | Neplatné vstupné údaje                        |
| 401  | Neautorizovaná požiadavka                      |
| 403  | Nedostatočné oprávnenia                       |
| 404  | Skladová položka neexistuje                    |
| 500  | Interná chyba systému                          |

---

# Business pravidlá

- Skladovú položku môže aktualizovať iba oprávnený používateľ alebo autorizovaný systémový proces.
- Inventory Agent môže aktualizovať stav zásob podľa reálnej spotreby surovín.
- Zmena množstva musí byť zaznamenaná v systéme.
- Aktuálne množstvo skladovej položky nemôže byť záporné.
- Pri dosiahnutí minimálneho množstva môže Inventory Agent upozorniť Restaurant Assistanta na potrebu doplnenia zásob.
- Nedostupnosť potrebnej suroviny môže ovplyvniť dostupnosť produktu.
- Inventory API nemení definíciu produktu v Products Database.
- Inventory API nemení stav objednávky v Orders Database.
- Každá aktualizácia skladovej položky musí byť zaznamenaná v audite.

---

# Súvisiace dokumenty

- GET /inventory/{id}
- GET /inventory
- Inventory Database
- Inventory Workflow
- Products API
- Orders API
- AI Agent Communication

---

# Budúce rozšírenia

- Automatické objednávanie zásob.
- História skladových pohybov.
- Sledovanie expirácie surovín.
- Správa dodávateľov.
- Podpora viacerých skladov.
- AI predikcia spotreby zásob.

---

# Stav dokumentu

🟢 Hotový
