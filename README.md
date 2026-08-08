# 🍽️ Smart Restaurant AI

Smart Restaurant AI je modulárna platforma navrhnutá na automatizáciu procesov v gastronómii pomocou backendových služieb a spolupracujúcich AI agentov.

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
AI Core / AI Agenti
        ↓
Frontend / Mobilná aplikácia
```

Backend je postupne implementovaný pomocou:

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

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
│   ├── routers
│   ├── services
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
- Products
- Inventory
- Payments
- Customers
- Users
- Notifications
- Reports
- Reservations

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

---

# 🤖 AI architektúra

Centrálnym koordinátorom systému je **Restaurant Assistant**.

Jeho úlohou je koordinovať požiadavky medzi jednotlivými časťami systému a špecializovanými agentmi.

Plánovaná architektúra:

```text
Zákazník / Personál
        ↓
Restaurant Assistant
        ↓
AI Core
        ↓
Špecializovaní agenti
        ↓
API / Services
        ↓
Databáza
```

AI vrstva zatiaľ nie je implementovaná a nachádza sa vo fáze návrhu.

---

# 💻 Aktuálna implementácia backendu

Backend už obsahuje prvý funkčný modul:

## Products API

Implementované endpointy:

```text
GET   /products
GET   /products/{id}
POST  /products
PATCH /products/{id}
```

Products modul používa:

```text
FastAPI Router
      ↓
Products Service
      ↓
SQLAlchemy
      ↓
SQLite
```

Implementované sú tiež:

- databázové spojenie
- SQLAlchemy model Product
- Pydantic request/response schemas
- dependency pre databázovú session
- HTTP 404 pre neexistujúci produkt
- Swagger / OpenAPI dokumentácia
- oddelená router a service vrstva

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
pip install -r requirements.txt
```

Spusti FastAPI server:

```bash
uvicorn main:app --reload
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

| Oblasť                   | Stav                        |
| ------------------------- | --------------------------- |
| Business analýza         | ✅ Dokončená              |
| Produktová architektúra | ✅ Základ dokončený      |
| Databázový návrh       | ✅ Základ dokončený      |
| API návrh                | ✅ v1.0 dokončené         |
| Backend základ           | ✅ Funkčný                |
| Products modul            | 🟢 Implementovaný základ  |
| Orders modul              | ⬜ Čaká na implementáciu |
| Payments modul            | ⬜ Čaká na implementáciu |
| Inventory modul           | ⬜ Čaká na implementáciu |
| Kitchen modul             | ⬜ Čaká na implementáciu |
| Notifications modul       | ⬜ Čaká na implementáciu |
| Reporting modul           | ⬜ Čaká na implementáciu |
| AI Core                   | ⬜ Plánované              |
| Frontend                  | ⬜ Plánované              |
| Testovanie                | ⬜ Plánované              |
| MVP                       | ⬜ Vo vývoji               |

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
Backend
   🟡
AI Core
   ⬜
Frontend
   ⬜
Testovanie
   ⬜
MVP
   ⬜
```

Aktuálna vývojová fáza:

**Backend implementation**

---

# 🧠 Návrhové princípy

Projekt je navrhovaný s dôrazom na:

- modularitu
- oddelenie zodpovedností
- škálovateľnosť
- jednoduché rozširovanie
- jasné API rozhrania
- oddelenie business logiky od API vrstvy
- bezpečné spracovanie dát
- konzistentnú dokumentáciu
- postupnú implementáciu funkčného MVP

---

# 📌 Stav repozitára

Projekt je aktívne vyvíjaný.

Dokumentácia predstavuje návrh cieľového systému, zatiaľ čo implementácia backendu prebieha postupne po jednotlivých moduloch.

Cieľom verzie **v1.0** je vytvoriť funkčné MVP Smart Restaurant AI bez zbytočného rozširovania rozsahu projektu.
