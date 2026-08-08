# PATCH /kitchen/orders//status

## Verzia dokumentu

v1.0

---

# Účel endpointu

Aktualizovať stav prípravy konkrétnej objednávky v kuchyni.

---

# Business cieľ

Umožniť bezpečnú a kontrolovanú aktualizáciu stavu objednávky počas procesu prípravy v kuchyni.

Zabezpečiť, aby zmena stavu prípravy bola koordinovaná prostredníctvom Restaurant Assistant a bola v súlade s definovaným Kitchen Workflow.

---

# HTTP Metóda

PATCH

---

# URL

/api/v1/kitchen/orders/{id}/status

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                                  |
| --------- | ---- | -------- | -------------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor objednávky |

---

# Request Body

Požiadavka obsahuje:

- Nový stav prípravy objednávky
- Dôvod zmeny (voliteľné)
- Čas aktualizácie

Povolené stavy:

- Waiting
- Preparing
- Ready
- Paused
- Cancelled

---

# Workflow

1. Kuchár alebo Kitchen Agent zaznamená zmenu v procese prípravy objednávky.
2. Kitchen Agent odošle informáciu Restaurant Assistantovi.
3. Restaurant Assistant overí, či je požadovaná zmena stavu povolená podľa Kitchen Workflow.
4. Restaurant Assistant odošle požiadavku na aktualizáciu stavu.
5. Kitchen API aktualizuje stav prípravy objednávky.
6. Ak zmena ovplyvňuje hlavný stav objednávky, Restaurant Assistant zabezpečí jeho aktualizáciu cez Orders API.
7. Notification Agent môže informovať zákazníka o zmene stavu.
8. Reporting Agent zaznamená zmenu do histórie systému.

---

# Kto môže volať API

- Restaurant Assistant
- Administrátor systému

---

# Response

Úspešná odpoveď obsahuje:

- Order ID
- Predchádzajúci stav prípravy
- Nový stav prípravy
- Čas aktualizácie

---

# HTTP Status Codes

| Kód | Popis                                                      |
| ---- | ---------------------------------------------------------- |
| 200  | Stav prípravy bol úspešne aktualizovaný                |
| 400  | Neplatný stav alebo neplatný prechod medzi stavmi        |
| 401  | Neautorizovaná požiadavka                                |
| 403  | Nedostatočné oprávnenia                                 |
| 404  | Objednávka neexistuje alebo nie je dostupná pre kuchyňu |
| 500  | Interná chyba systému                                    |

---

# Business pravidlá

- Kitchen Agent nemení stav prípravy priamo v databáze.
- Kitchen Agent odovzdáva informáciu o zmene Restaurant Assistantovi.
- Restaurant Assistant koordinuje aktualizáciu stavu prípravy.
- Zmena stavu musí byť v súlade s Kitchen Workflow.
- Kitchen API nemení platobné údaje.
- Kitchen API nemení údaje produktu v Products Database.
- Hlavný stav objednávky sa mení iba prostredníctvom Orders API.
- Každá zmena stavu prípravy musí byť zaznamenaná v audite.
- Individuálne úpravy produktov požadované zákazníkom zostávajú počas prípravy zachované.

---

# Súvisiace dokumenty

- GET /kitchen/orders/{id}
- GET /kitchen/orders
- Kitchen Workflow
- Orders API
- Products API
- Inventory API
- Notifications Workflow
- Reporting Workflow

---

# Budúce rozšírenia

- Sledovanie stavu jednotlivých položiek objednávky.
- Automatické prideľovanie objednávok kuchárom.
- AI prioritizácia objednávok.
- Presnejší odhad času dokončenia.
- Podpora viacerých kuchynských pracovísk.

---

# Stav dokumentu

🟢 Hotový
