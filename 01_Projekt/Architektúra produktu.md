# Architektúra produktu – Smart Restaurant AI

## Verzia

v1.0

---

# Hlavné moduly systému

## 🌐 Web / Mobilná aplikácia

- Online objednávky
- Rezervácie
- Vernostný program
- Profil zákazníka
- História objednávok

---

## 🤖 AI Core

Riadi komunikáciu medzi všetkými modulmi systému.

Obsahuje AI agentov zodpovedných za jednotlivé oblasti.

---

## 📦 Správa objednávok

- prijatie objednávky
- kontrola skladu
- odoslanie do kuchyne
- sledovanie stavu objednávky
- odhad času dokončenia

---

## 💳 Platby

- online platby
- potvrdenie platby
- fakturácia
- pokladňa

---

## 📦 Sklad

- evidencia zásob
- odpočítanie surovín
- objednávanie tovaru
- kontrola expirácie

---

## 📅 Rezervácie

- rezervácia stolov
- kontrola kapacity
- potvrdenia
- pripomienky

---

## 📊 Reporty

- denné reporty
- týždenné reporty
- mesačné reporty
- analýza predaja
- analýza skladu

---

## ⚙ Administrácia

- správa používateľov
- správa jedálneho lístka
- ceny
- nastavenia systému

---

# Komunikácia modulov

Web

↓

AI Core

↓

Jednotlivé AI Agenty

↓

Databáza

↓

Externé služby

↓

Zákazník / Zamestnanci
