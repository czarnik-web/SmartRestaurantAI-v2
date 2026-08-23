# 🍽️ Smart Restaurant AI

Smart Restaurant AI je modulárna platforma navrhnutá na automatizáciu procesov v gastronómii pomocou backendových služieb a spolupracujúcej AI vrstvy.

Projekt vzniká zároveň ako praktický vývojový projekt, na ktorom sa postupne implementuje kompletný systém od business analýzy a architektúry až po funkčný backend, AI vrstvu a používateľské rozhranie.

---

# 🎯 Vízia projektu

Cieľom je vytvoriť systém, ktorý dokáže pomáhať s každodennou prevádzkou reštaurácie:

- objednávky
- platby
- sklad
- kuchyňa
- komunikácia so zákazníkmi
- reporting
- automatizácia interných procesov

Dlhodobou víziou je vytvoriť spoločné **AI Core**, nad ktorým budú fungovať špecializovaní AI agenti.

Smart Restaurant AI preto nie je navrhnutý iba ako jedna aplikácia, ale ako modulárny základ, ktorý bude možné postupne rozširovať.

---

# 🏗️ Architektúra

Projekt oddeľuje jednotlivé vrstvy systému:

```text
Business požiadavky
        ↓
Business workflow
        ↓
Databáza
        ↓
REST API
        ↓
Service Layer
        ↓
Restaurant Assistant / AI vrstva
        ↓
Frontend / Mobilná aplikácia
```

Backend je implementovaný pomocou:

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest
- HTTPX
- Ollama
- Qwen3 4B

Architektúra backendu používa oddelenie:

```text
API Router
    ↓
Service Layer
    ↓
Database Model
    ↓
Database
```

AI časť používa samostatnú orchestration vrstvu:

```text
AI Chat
    ↓
AI model
    ↓
Restaurant Assistant
    ↓
Service Layer
    ↓
Database
```

Restaurant Assistant nepristupuje priamo k databáze. Pracuje prostredníctvom existujúcich backendových služieb.

---

# 📁 Štruktúra projektu

```text
SmartRestaurantAI-v2
│
├── 00_Admin
├── 01_Projekt
├── 02_Analýza
├── 03_Databáza
├── 04_API
├── 07_AI_Agenti
├── 11_Roly
├── 99_nápady
│
├── backend
│   ├── AI
│   │   ├── __init__.py
│   │   ├── restaurant_assistant.py
│   │   ├── ollama_client.py
│   │   └── openai_client.py
│   │
│   ├── routers
│   │   ├── products.py
│   │   ├── orders.py
│   │   ├── payments.py
│   │   ├── inventory.py
│   │   ├── kitchen.py
│   │   ├── notifications.py
│   │   ├── reporting.py
│   │   └── ai_chat.py
│   │
│   ├── services
│   │   ├── products_service.py
│   │   ├── orders_service.py
│   │   ├── payments_service.py
│   │   ├── inventory_service.py
│   │   ├── kitchen_service.py
│   │   ├── notifications_service.py
│   │   └── reporting_service.py
│   │
│   ├── tests
│   │   ├── conftest.py
│   │   ├── test_main.py
│   │   ├── test_products.py
│   │   ├── test_orders.py
│   │   ├── test_payments.py
│   │   ├── test_inventory.py
│   │   ├── test_kitchen.py
│   │   ├── test_notifications.py
│   │   ├── test_reporting.py
│   │   └── test_restaurant_assistant.py
│   │
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

# 📚 Dokumentácia

Projekt obsahuje samostatnú dokumentáciu pre business, databázu, API a AI architektúru.

## 00_Admin

Projektové a organizačné dokumenty:

- roadmap
- rozsah projektu
- architektonické poznámky
- rozhodnutia
- dokumentačný štandard

## 01_Projekt

Produktová a business vrstva:

- architektúra produktu
- business model
- cieľový zákazník
- moduly systému
- produktová stratégia
- priority vývoja

## 02_Analýza

Business a systémové workflow:

- System Workflow
- Request Processing Architecture
- Inventory Workflow
- Kitchen Workflow
- Payments Workflow
- Notifications Workflow
- Reporting Workflow

## 03_Databáza

Návrh databázových entít vrátane:

- Orders
- Order Items
- Products
- Inventory
- Payments
- Customers
- Users
- Notifications
- Reports
- Reservations

Nie všetky navrhnuté entity sú už súčasťou MVP implementácie.

## 04_API

REST API návrh systému.

Dokumentované sú moduly:

- Orders API
- Payments API
- Products API
- Inventory API
- Kitchen API
- Notifications API
- Reporting API

Backendová implementácia týchto hlavných modulov je už funkčná.

## 07_AI_Agenti

Návrhy AI agentov systému, napríklad:

- Restaurant Assistant
- Inventory Agent
- Kitchen Agent
- Payment Agent
- Notification Agent
- Reporting Agent
- Sales Agent
- Security Agent
- System Monitor Agent

V aktuálnej MVP implementácii je prvou funkčnou AI orchestration vrstvou **Restaurant Assistant**.

---

# 🤖 AI architektúra

Centrálnym koordinátorom systému je **Restaurant Assistant**.

Restaurant Assistant funguje ako interná orchestration vrstva nad existujúcimi backendovými službami.

Nemá vlastné samostatné CRUD API. Používateľ vstupuje do AI vrstvy cez:

```text
POST /ai/chat
```

Aktuálna implementácia:

```text
Používateľ / budúci Frontend
        ↓
POST /ai/chat
        ↓
Lokálny AI model
Qwen3 4B cez Ollama
        ↓
Action detection
        ↓
Restaurant Assistant
        ↓
Products / Orders / Payments
Inventory / Kitchen
Notifications / Reporting
        ↓
Service Layer
        ↓
Databáza
```

AI model slúži na pochopenie požiadavky používateľa a výber povolenej akcie.

Restaurant Assistant následne vykoná požadovanú operáciu cez existujúce backendové služby.

Aktuálne podporované AI akcie:

```text
restaurant_status
product_count
order_overview
unknown
```

AI dokáže pracovať aj s parametrami.

Príklad:

```text
Používateľ:
"Ukáž mi objednávku číslo 2"

        ↓

AI rozhodnutie:

{
    "action": "order_overview",
    "order_id": 2
}

        ↓

Restaurant Assistant
        ↓
Orders Service + Payments Service
        ↓
odpoveď z reálnych dát systému
```

Príklady podporovaných požiadaviek:

```text
"Ako sa dnes darí našej reštaurácii?"

"Koľko jedál máme momentálne v systéme?"

"Ukáž mi objednávku číslo 2"
```

AI model je aktuálne prevádzkovaný lokálne pomocou **Ollama + Qwen3 4B**, takže základná AI funkcionalita môže fungovať bez plateného externého API.

Projekt obsahuje aj pripraveného OpenAI klienta pre možný budúci prechod alebo podporu viacerých AI providerov.

---

# 💻 Aktuálna implementácia backendu

Backend obsahuje funkčné moduly:

## Products API

```text
GET   /products
GET   /products/{id}
POST  /products
PATCH /products/{id}
```

## Orders API

```text
GET   /orders
GET   /orders/{id}
POST  /orders
PATCH /orders/{id}
```

Objednávka podporuje položky objednávky cez `OrderItem`.

Cena položky je získavaná z produktu na backende a výsledná suma objednávky sa počíta automaticky.

## Payments API

```text
GET   /payments
GET   /payments/{id}
POST  /payments
PATCH /payments/{id}
```

Platba používa sumu objednávky z backendu.

Pre jednu objednávku môže v aktuálnom MVP existovať iba jedna platba.

Zmena stavu platby sa synchronizuje aj do objednávky.

## Inventory API

```text
GET   /inventory
GET   /inventory/{id}
POST  /inventory
PATCH /inventory/{id}
```

Inventory podporuje evidenciu:

- aktuálneho množstva
- minimálneho množstva
- jednotky
- typu položky
- stavu položky

## Kitchen API

```text
GET   /kitchen/orders
GET   /kitchen/orders/{id}
PATCH /kitchen/orders/{id}/status
```

Aktuálne podporované stavy objednávky v MVP:

```text
New
Preparing
Ready
```

Stav `Ready` je v MVP používaný ako dokončená objednávka pre reporting.

## Notifications API

```text
GET  /notifications
GET  /notifications/{id}
POST /notifications
```

Aktuálna implementácia eviduje notifikácie v systéme.

Externé odosielanie SMS, e-mailov alebo push notifikácií je plánované ako ďalšie rozšírenie.

## Reporting API

```text
GET /reports/daily
GET /reports/sales
GET /reports/refunds
```

Reporting aktuálne poskytuje napríklad:

- počet objednávok
- tržby
- low-stock položky
- počet dokončených objednávok
- počet predaných položiek
- Top produkty
- počet refundácií
- refundovanú sumu

## AI Chat API

```text
POST /ai/chat
```

AI Chat používa Restaurant Assistanta ako internú orchestration vrstvu.

AI model rozpozná požiadavku používateľa a vyberie povolenú akciu.

Implementované sú tiež:

- databázové spojenie
- centrálna databázová dependency `get_db`
- SQLAlchemy modely
- Pydantic request/response schemas
- validačné pravidlá
- HTTP 404 pre neexistujúce entity
- HTTP 409 pre business konflikty
- oddelená router a service vrstva
- rollback pri neplatnom vytváraní objednávky
- Swagger / OpenAPI dokumentácia
- automatizované backendové testy
- samostatná in-memory SQLite databáza pre testovanie
- AI routing testy bez nutnosti reálne volať Ollamu

---

# 🧪 Automatické testovanie

Backend používa **Pytest**.

Testy používajú samostatnú SQLite databázu v pamäti, takže neovplyvňujú lokálnu vývojovú databázu.

Aktuálne:

```text
25 passed
```

Testované sú hlavné scenáre:

- Products
- Orders
- Payments
- Inventory
- Kitchen
- Notifications
- Reporting
- Restaurant Assistant
- AI routing
- validačné chyby
- 404 scenáre
- 409 konflikty
- synchronizácia platby a objednávky
- ochrana pri neplatnom AI JSON výstupe

Spustenie testov:

```bash
python -m pytest
```

---

# ▶️ Lokálne spustenie backendu

Prejdi do backend priečinka:

```bash
cd backend
```

Vytvor virtuálne prostredie:

```bash
python -m venv venv
```

Aktivácia vo Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Nainštaluj dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Ollama

Pre lokálnu AI vrstvu je potrebné mať nainštalovanú Ollamu.

Používaný model:

```text
qwen3:4b
```

Stiahnutie modelu:

```bash
ollama pull qwen3:4b
```

Test modelu:

```bash
ollama run qwen3:4b "Odpovedz iba slovom FUNGUJE"
```

Ollama poskytuje lokálne API na:

```text
http://localhost:11434
```

---

## FastAPI

Spusti FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Backend bude dostupný na:

```text
http://127.0.0.1:8000
```

Swagger dokumentácia:

```text
http://127.0.0.1:8000/docs
```

---

# 🚧 Stav projektu

| Oblasť                   | Stav                   |
| ------------------------- | ---------------------- |
| Business analýza         | ✅ Dokončená         |
| Produktová architektúra | ✅ Základ dokončený |
| Databázový návrh       | ✅ Základ dokončený |
| API návrh                | ✅ v1.0 dokončené    |
| Backend základ           | ✅ Funkčný           |
| Products modul            | ✅ Implementovaný     |
| Orders modul              | ✅ Implementovaný     |
| Payments modul            | ✅ Implementovaný     |
| Inventory modul           | ✅ Implementovaný     |
| Kitchen modul             | ✅ Implementovaný     |
| Notifications modul       | ✅ Implementovaný     |
| Reporting modul           | ✅ Implementovaný     |
| Backend hardening         | ✅ Základ dokončený |
| Automatické testovanie   | ✅ 25 testov           |
| Restaurant Assistant      | 🟢 Funkčný základ   |
| AI Chat                   | 🟢 Funkčný           |
| AI routing                | 🟢 Akcie + parametre   |
| Ollama integrácia        | 🟢 Funkčná           |
| AI Core                   | 🟡 Vo vývoji          |
| Frontend                  | ⬜ Plánované         |
| MVP                       | 🟡 Vo vývoji          |

---

# 🗺️ Roadmap

Projekt sa vyvíja postupne.

```text
Analýza
   ✅
Databázový návrh
   ✅
API návrh
   ✅
Backend základ
   ✅
Backend hardening + testovanie
   ✅
Restaurant Assistant
   🟡
AI Core
   🟡
Frontend
   ⬜
MVP
   🟡
```

Aktuálna vývojová fáza:

**Restaurant Assistant / AI Core implementation**

Aktuálnym cieľom je postupne rozširovať AI vrstvu o ďalšie bezpečne povolené nástroje a akcie nad existujúcimi backendovými službami.

---

# 🧠 Návrhové princípy

Projekt je navrhovaný s dôrazom na:

- modularitu
- oddelenie zodpovedností
- škálovateľnosť
- jednoduché rozširovanie
- jasné API rozhrania
- oddelenie business logiky od API vrstvy
- oddelenie AI vrstvy od priameho prístupu k databáze
- bezpečné spracovanie dát
- bezpečné AI akcie
- konzistentnú dokumentáciu
- automatické testovanie
- postupnú implementáciu funkčného MVP

---

# 📌 Stav repozitára

Projekt je aktívne vyvíjaný.

Business analýza, databázový návrh, API návrh a základ hlavných backendových modulov sú implementované.

Backend je pokrytý automatizovanými testami a obsahuje prvú funkčnú AI orchestration vrstvu cez **Restaurant Assistant**.

Lokálny AI model **Qwen3 4B cez Ollama** dokáže analyzovať používateľskú požiadavku, vybrať povolenú akciu a odovzdať ju Restaurant Assistantovi, ktorý pracuje s existujúcimi backendovými službami.

Projekt sa aktuálne nachádza vo fáze rozširovania **Restaurant Assistant / AI Core** vrstvy.

Cieľom verzie **v1.0** je vytvoriť funkčné MVP Smart Restaurant AI bez zbytočného rozširovania rozsahu projektu.
