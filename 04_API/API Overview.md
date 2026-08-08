# API Overview

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať štruktúru REST API platformy Smart Restaurant AI.

---

# Business cieľ

Poskytnúť jednotné rozhranie pre komunikáciu medzi frontendom, AI agentmi a backend službami.

---

# Architektúra API

REST API je rozdelené do samostatných modulov podľa business domén.

Každý modul je zodpovedný za svoju oblasť systému.

---

# API Moduly

## Orders API

Správa objednávok.

---

## Payments API

Správa platieb a refundácií.

---

## Inventory API

Kontrola skladu a rezervácia surovín.

---

## Kitchen API

Správa objednávok v kuchyni.

---

## Notifications API

Odosielanie oznámení zákazníkom.

---

## Reporting API

Prístup k reportom a histórii udalostí.

---

# Základné REST princípy

- GET – získanie údajov
- POST – vytvorenie nového záznamu
- PATCH – čiastočná aktualizácia
- DELETE – odstránenie záznamu

---

# Formát komunikácie

Request:

JSON

↓

REST API

↓

Response:

JSON

---

# Autentifikácia

Bude riešená v samostatnom dokumente.

---

# Stav dokumentu

🟢 Hotový
