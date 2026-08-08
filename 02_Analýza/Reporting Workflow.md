# Reporting Workflow

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces zaznamenávania dôležitých udalostí počas spracovania objednávok.

---

# Business cieľ

Zabezpečiť úplnú históriu udalostí pre každú objednávku.

---

# Začiatok procesu

Proces začína pri každej udalosti, ktorá mení stav objednávky alebo predstavuje významnú operáciu v systéme.

---

# Workflow

## 1. Vznik udalosti

Restaurant Assistant zaznamená novú udalosť.

↓

Restaurant Assistant odošle požiadavku Reporting Agentovi.

---

## 2. Spracovanie udalosti

Reporting Agent spracuje prijaté údaje.

↓

Reporting Agent pripraví záznam.

---

## 3. Uloženie záznamu

Reporting Agent uloží udalosť do databázy.

↓

História objednávky sa aktualizuje.

---

## 4. Potvrdenie uloženia

Ak bolo uloženie úspešné:

↓

Proces pokračuje.

Ak uloženie zlyhá:

↓

Reporting Agent zaznamená chybu.

↓

Restaurant Assistant môže iniciovať opakovaný pokus o uloženie.

---

# AI Agenti

- Restaurant Assistant
- Reporting Agent

---

# Databázy

- Orders Database
- Reporting Database

---

# Zaznamenávané udalosti

- Objednávka vytvorená
- Platba vytvorená
- Platba úspešná
- Platba neúspešná
- Kontrola skladu
- Rezervácia surovín
- Začiatok prípravy
- Objednávka pripravená
- Objednávka dokončená
- Refundácia
- Zrušenie objednávky

---

# Koniec procesu

Proces končí úspešným uložením udalosti.

---

# Budúce rozšírenia

- AI analýza histórie objednávok
- Dashboard pre manažéra
- Štatistiky kuchyne
- Štatistiky predaja
- Export reportov
- Audit log

---

# Stav dokumentu

🟡 Rozpracovaný
