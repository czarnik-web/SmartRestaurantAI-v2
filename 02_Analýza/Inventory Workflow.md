# Inventory Workflow

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces kontroly a správy skladových zásob počas spracovania objednávok.

---

# Business cieľ

Zabezpečiť, aby bolo možné pripraviť každú potvrdenú objednávku z dostupných skladových zásob.

---

# Začiatok procesu

Proces začína po úspešnom prijatí objednávky a potvrdení platby.

Po potvrdení platby Restaurant Assistant požiada Inventory Agenta o kontrolu dostupnosti surovín.

---

# Workflow

## 1. Prijatie požiadavky

Restaurant Assistant odošle požiadavku Inventory Agentovi.

---

## 2. Kontrola zásob

Po úspešnom prijatí platby Restaurant Assistant odošle požiadavku Inventory Agentovi.

Inventory Agent overí dostupnosť všetkých potrebných surovín.

---

## 3. Vyhodnotenie

Ak sú všetky suroviny dostupné:

↓

Inventory Agent rezervuje potrebné množstvo surovín pre objednávku.

↓

Restaurant Assistant pokračuje v spracovaní objednávky.

Ak niektoré suroviny nie sú dostupné:

↓

Objednávka nebude potvrdená.

↓

Restaurant Assistant informuje zákazníka o nedostupnosti objednávky alebo jej časti.---

## 4. Aktualizácia skladu

Po dokončení objednávky Inventory Agent odpočíta spotrebované množstvo zo skladu.

---

## 5. Kontrola minimálnych zásob

Po aktualizácii skladu Inventory Agent overí minimálne skladové limity.

Ak niektorá položka klesne pod minimálnu hodnotu:

↓

Vytvorí upozornenie pre personál.

---

# AI Agenti

- Restaurant Assistant
- Inventory Agent
- Notification Agent
- Reporting Agent

---

# Databázy

- Inventory Database
- Products Database
- Orders Database

---

# Možné výsledky

- Suroviny dostupné
- Nedostatok surovín
- Rezervované
- Spotrebované
- Upozornenie na nízky stav zásob

---

# Koniec procesu

Proces končí aktualizáciou skladových zásob a prípadným vytvorením upozornenia.

---

# Budúce rozšírenia

- Automatické vytváranie objednávok dodávateľom.
- AI predikcia spotreby.
- AI plánovanie nákupu.
- Viac skladov.
- Expirácia surovín.
- FIFO/LIFO skladové hospodárstvo.

---

# Stav dokumentu

🟡 Rozpracovaný
