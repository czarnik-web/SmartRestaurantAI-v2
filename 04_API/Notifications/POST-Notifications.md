# POST /notifications

## Verzia dokumentu

v1.0

---

# Účel endpointu

Vytvoriť a odoslať upozornenie zákazníkovi alebo oprávnenému používateľovi systému Smart Restaurant AI.

---

# Business cieľ

Zabezpečiť automatické informovanie zákazníka o dôležitých udalostiach súvisiacich s jeho objednávkou.

Umožniť interným systémovým procesom bezpečne vytvárať upozornenia bez priameho zásahu do ostatných business domén.

---

# HTTP Metóda

POST

---

# URL

/api/v1/notifications

---

# Request Body

Požiadavka obsahuje:

- Customer ID alebo identifikátor príjemcu
- Typ upozornenia
- Obsah správy
- Súvisiace Order ID (voliteľné)
- Kanál odoslania

---

# Workflow

1. V systéme nastane udalosť, o ktorej má byť zákazník alebo oprávnený používateľ informovaný.
2. Príslušný AI agent alebo systémový modul odošle informáciu Restaurant Assistantovi.
3. Restaurant Assistant vyhodnotí potrebu odoslania upozornenia.
4. Restaurant Assistant odošle požiadavku na vytvorenie upozornenia.
5. Notifications API vytvorí upozornenie.
6. Notification Agent zabezpečí jeho odoslanie cez určený komunikačný kanál.
7. Výsledok odoslania sa zaznamená v systéme.

---

# Kto môže volať API

- Restaurant Assistant
- Administrátor systému
- Autorizovaný systémový proces

---

# Response

Úspešná odpoveď obsahuje:

- Notification ID
- Identifikátor príjemcu
- Typ upozornenia
- Stav upozornenia
- Kanál odoslania
- Čas vytvorenia
- Čas odoslania

---

# HTTP Status Codes

| Kód | Popis                                             |
| ---- | ------------------------------------------------- |
| 201  | Upozornenie bolo úspešne vytvorené             |
| 400  | Neplatné alebo neúplné vstupné údaje         |
| 401  | Neautorizovaná požiadavka                       |
| 403  | Nedostatočné oprávnenia                        |
| 404  | Príjemca alebo súvisiaca objednávka neexistuje |
| 500  | Interná chyba systému                           |

---

# Business pravidlá

- Upozornenie môže vytvoriť iba autorizovaný proces.
- Restaurant Assistant koordinuje vytvorenie upozornenia.
- Notification Agent zabezpečuje odoslanie upozornenia.
- Notification Agent nemení stav objednávky ani platby.
- Upozornenie môže obsahovať iba údaje potrebné na informovanie príjemcu.
- Zákazník nesmie prostredníctvom upozornenia získať údaje o cudzej objednávke.
- Výsledok odoslania upozornenia musí byť zaznamenaný v systéme.

---

# Súvisiace dokumenty

- GET /notifications/{id}
- GET /notifications
- Notifications Workflow
- Orders API
- Payments API
- Kitchen API
- AI Agent Communication

---

# Budúce rozšírenia

- Možnosť nastavenia preferovaných upozornení zákazníkom.
- Možnosť vypnutia voliteľných upozornení.
- Plánované upozornenia.
- Personalizované upozornenia.
- Rozšírenie komunikačných kanálov.

---

# Stav dokumentu

🟢 Hotový
