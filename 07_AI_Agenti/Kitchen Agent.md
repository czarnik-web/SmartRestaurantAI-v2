# Kitchen Agent

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje Kitchen Agenta systému Smart Restaurant AI.

Kitchen Agent riadi proces prípravy objednávok v kuchyni, sleduje ich stav a informuje ostatných agentov o priebehu prípravy.

---

# Identifikácia agenta

**ID:** AG-006

**Názov agenta:** Kitchen Agent

**Typ agenta:** Business Agent

**Verzia:** v1.0

**Priorita:** Kritická

**Stav:** 🟡 Rozpracovaný

---

# Business informácie

## Účel agenta

Riadiť proces prípravy jedál a zabezpečiť efektívnu komunikáciu medzi kuchyňou a systémom.

## Problém, ktorý rieši

Odstraňuje chaos pri objednávkach, skracuje čakaciu dobu a umožňuje presné sledovanie stavu každej objednávky.

## Hodnota pre zákazníka

- Presnejší čas prípravy.
- Menej chýb pri objednávkach.
- Rýchlejšia obsluha.
- Lepšia organizácia práce kuchyne.

---

# Kompetencie

## Agent môže

- prijímať objednávky
- zoradiť objednávky podľa priority
- sledovať stav prípravy
- označiť objednávku ako hotovú
- odhadnúť čas prípravy
- komunikovať s Inventory Agentom

## Agent nesmie

- meniť obsah objednávky
- meniť ceny produktov
- rušiť objednávky
- upravovať skladové zásoby

---

# Rozhodovacie právomoci

## Samostatné rozhodnutia

- určiť poradie prípravy
- aktualizovať stav objednávky
- oznámiť dokončenie objednávky

## Rozhodnutia vyžadujúce schválenie manažéra

- zastavenie výroby
- vyradenie objednávky
- zmena pracovného postupu

---

# Workflow

1. Prijme objednávku.
2. Skontroluje dostupnosť surovín.
3. Zaradí objednávku do poradia.
4. Odhadne čas prípravy.
5. Sleduje priebeh prípravy.
6. Označí objednávku ako hotovú.
7. Informuje Restaurant Assistanta.

---

# Rozhodovacia logika

Ak sú všetky suroviny dostupné

↓

Začni prípravu

↓

Odhadni čas

↓

Po dokončení označ objednávku ako hotovú

↓

Informuj Restaurant Assistanta

---

# Komunikácia

## Prijíma údaje od

- Restaurant Assistant
- Inventory Agent

## Odosiela údaje

- Restaurant Assistant
- Inventory Agent
- Reporting Agent

---

# Databáza

## Číta tabuľky

- Orders
- Products
- Recipes
- Inventory

## Zapisuje tabuľky

- Kitchen_Log
- Order_Status

---

# API a externé služby

Žiadne.

---

# Logovanie

Agent zaznamenáva

- začiatok prípravy
- ukončenie prípravy
- meškania
- chyby

---

# Bezpečnostné pravidlá

- Každá zmena stavu objednávky musí byť zaznamenaná.
- História objednávok musí zostať zachovaná.

---

# KPI

- Priemerný čas prípravy.
- Počet vybavených objednávok.
- Meškajúce objednávky.
- Vyťaženosť kuchyne.

---

# ROI

**Úspora času:** Lepšie riadenie kuchyne.

**Úspora nákladov:** Menej chýb pri príprave.

**Zníženie chybovosti:** Automatická evidencia stavu objednávok.

**Odhad návratnosti investície:** Zvýšenie efektivity kuchyne.

---

# Chybové scenáre

- Nedostatok surovín → upozorni Inventory Agenta.
- Výpadok systému → zachovaj posledný stav objednávky.
- Oneskorenie prípravy → informuj Restaurant Assistanta.

---

# Budúce rozšírenia

- AI optimalizácia poradia objednávok.
- Predikcia času prípravy podľa histórie.
- Integrácia s kuchynskými displejmi.

---

# Poznámky

Kitchen Agent zabezpečuje riadenie celej kuchyne a spolupracuje najmä s Restaurant Assistantom a Inventory Agentom.

---

# Stav dokumentu

🟡 Rozpracovaný
