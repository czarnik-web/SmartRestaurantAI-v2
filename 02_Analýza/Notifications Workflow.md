# Notifications Workflow

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces odosielania oznámení zákazníkom počas spracovania objednávky.

---

# Business cieľ

Zabezpečiť včasné, presné a spoľahlivé informovanie zákazníka o stave objednávky.

---

# Začiatok procesu

Proces začína po udalosti, ktorá vyžaduje informovanie zákazníka.

---

# Workflow

## 1. Vznik udalosti

Restaurant Assistant zaznamená zmenu stavu objednávky.

↓

Restaurant Assistant odošle požiadavku Notification Agentovi.

---

## 2. Spracovanie oznámenia

Notification Agent pripraví oznámenie.

↓

Notification Agent vyberie vhodný komunikačný kanál.

---

## 3. Odoslanie oznámenia

Notification Agent odošle oznámenie zákazníkovi.

---

## 4. Potvrdenie odoslania

Ak odoslanie oznámenia zlyhá:

↓

Notification Agent vykoná opakovaný pokus o odoslanie.

↓

Ak sa oznámenie nepodarí odoslať ani po opakovaných pokusoch:

↓

Reporting Agent zaznamená neúspešné doručenie.

↓

Hlavný workflow objednávky pokračuje bez prerušenia.

---

# AI Agenti

- Restaurant Assistant
- Notification Agent
- Reporting Agent

---

# Databázy

- Orders Database
- Notifications Database

---

# Typy oznámení

- Objednávka prijatá
- Platba úspešná
- Platba neúspešná
- Objednávka sa pripravuje
- Objednávka pripravená
- Objednávka dokončená
- Objednávka zrušená

---

# Koniec procesu

Proces končí úspešným alebo neúspešným odoslaním oznámenia.

---

# Budúce rozšírenia

- Push notifikácie
- SMS správy
- E-mailové oznámenia
- WhatsApp
- Viber
- Preferovaný komunikačný kanál zákazníka
- AI optimalizácia obsahu správ

---

# Stav dokumentu

🟡 Rozpracovaný
