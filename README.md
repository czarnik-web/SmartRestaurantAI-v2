# 🍽️ Smart Restaurant AI

## O projekte

Smart Restaurant AI je modulárna platforma využívajúca umelú inteligenciu na automatizáciu procesov v gastronómii.

Cieľom projektu je vytvoriť inteligentný systém, ktorý dokáže riadiť objednávky, platby, sklad, kuchyňu, komunikáciu so zákazníkmi a ďalšie business procesy prostredníctvom spolupracujúcich AI agentov.

Projekt je navrhnutý s dôrazom na škálovateľnosť, bezpečnosť a jednoduché rozširovanie o nové moduly.

---

# Vízia projektu

Vytvoriť AI platformu, ktorá bude schopná efektívne riadiť každodennú prevádzku reštaurácie a v budúcnosti sa rozšíri aj do ďalších oblastí podnikania.

Projekt nie je navrhnutý iba ako jedna aplikácia pre reštauráciu.

Smart Restaurant AI predstavuje základ budúcej AI platformy, kde bude možné vytvárať ďalších špecializovaných AI asistentov využívajúcich spoločné AI Core.

---

# Hlavné ciele projektu

- Automatizácia business procesov
- Zjednotenie komunikácie medzi AI agentmi
- Bezpečné spracovanie objednávok a platieb
- Inteligentné riadenie skladu
- Podpora personálu pomocou AI
- Kvalitná analytika a reporting
- Modulárna architektúra pripravená na ďalší rozvoj

---

# Architektúra projektu

Projekt je rozdelený do samostatných vrstiev.

```text
Business

↓

Workflow

↓

Databáza

↓

API

↓

AI Core

↓

Frontend / Mobilná aplikácia
```

Každá vrstva je navrhnutá nezávisle tak, aby bolo možné systém jednoducho rozširovať.

---

# Štruktúra projektu

```text
01_Vízia
02_Analýza
03_Databáza
04_API
05_Automatizácie
99_Nápady
```

---

# Dokumentácia

## 01_Vízia

- Vision
- Product Goals

---

## 02_Analýza

- Business Processes
- AI Agents
- Request Processing Architecture
- System Workflow
- Orders Workflow
- Kitchen Workflow
- Inventory Workflow
- Payments Workflow
- Notifications Workflow
- Reporting Workflow

---

## 03_Databáza

- Database Overview
- Orders Database
- Products Database
- Inventory Database

---

## 04_API

- API Overview
- POST /orders

---

## 05_Automatizácie

- Request Processing Architecture
- ADR-001
- ADR-002
- ADR-003 AI Core Architecture

---

## 99_Nápady

Priestor pre nové funkcionality, experimenty a návrhy budúcich rozšírení.

---

# AI Agenti

Projekt využíva architektúru spolupracujúcich AI agentov.

Aktuálne navrhnutí agenti:

- Restaurant Assistant
- Payment Agent
- Inventory Agent
- Kitchen Agent
- Notification Agent
- Reporting Agent

Každý agent rieši svoju špecializovanú oblasť a komunikuje prostredníctvom AI Core.

---

# Business Workflow

Hlavný životný cyklus objednávky:

```text
Zákazník

↓

Restaurant Assistant

↓

Orders Workflow

↓

Payments Workflow

↓

Inventory Workflow

↓

Kitchen Workflow

↓

Notifications Workflow

↓

Reporting Workflow

↓

Objednávka dokončená
```

---

# Aktuálny stav projektu

## Dokončené

- Vízia projektu
- Business analýza
- Návrh AI agentov
- Workflow objednávok
- Workflow kuchyne
- Workflow skladu
- Workflow platieb
- Workflow notifikácií
- Workflow reportingu
- Návrh databáz
- Základ API
- Architektúra AI Core

---

# Roadmap

## Fáza 1

✅ Analýza projektu

---

## Fáza 2

🟡 Návrh databáz

---

## Fáza 3

🟡 Návrh kompletného API

---

## Fáza 4

🔲 Backend

---

## Fáza 5

🔲 AI Core

---

## Fáza 6

🔲 Frontend

---

## Fáza 7

🔲 Testovanie

---

## Fáza 8

🔲 MVP

---

# Návrhové princípy

Projekt je navrhnutý podľa nasledujúcich princípov:

- Modularita
- Škálovateľnosť
- Jednoduchá rozšíriteľnosť
- AI ako podpora business procesov
- Bezpečnosť
- Oddelenie business logiky od implementácie
- Jasná dokumentácia
- Jednotná architektúra

---

# Licencia

Interný projekt – Smart Restaurant AI.

---
# Poznámka

Táto dokumentácia vzniká iteratívne.

Každé architektonické rozhodnutie je najskôr analyzované z business aj technického pohľadu a následne zapracované do dokumentácie. Cieľom je vytvoriť kvalitný základ pre implementáciu systému bez nutnosti zásadných zmien architektúry v neskorších fázach vývoja.
---
