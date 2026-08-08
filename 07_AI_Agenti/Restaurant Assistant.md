# Restaurant Assistant

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje hlavného AI agenta systému Smart Restaurant AI.

Restaurant Assistant zabezpečuje komunikáciu so zákazníkmi, prijíma objednávky a rezervácie, koordinuje ostatných AI agentov a dohliada na plynulý priebeh objednávok.

---

# Identifikácia agenta

**ID:** AG-001

**Názov agenta:** Restaurant Assistant

**Typ agenta:** Communication Agent

**Verzia:** v1.0

**Priorita:** Kritická

**Stav:** 🟡 Rozpracovaný

---

# Business informácie

## Účel agenta

Zjednodušiť komunikáciu so zákazníkmi a automatizovať proces objednávok a rezervácií.

## Problém, ktorý rieši

Znižuje čas obsluhy zákazníkov, eliminuje manuálne spracovanie objednávok a zabezpečuje plynulú komunikáciu medzi zákazníkom a prevádzkou.

## Hodnota pre zákazníka

- Rýchle vybavenie objednávok.
- Okamžitá odpoveď.
- Presné informácie o objednávke.
- Menej chýb pri komunikácii.

---

# Kompetencie

## Agent môže

- prijímať online objednávky
- prijímať rezervácie
- komunikovať cez web, e-mail a SMS
- odovzdávať úlohy ostatným agentom
- informovať zákazníka o stave objednávky
- odpovedať na často kladené otázky

## Agent nesmie

- meniť ceny produktov
- rušiť objednávky bez potvrdenia zákazníka
- poskytovať osobné údaje iných zákazníkov
- vykonávať rozhodnutia vyhradené manažérovi

---

# Rozhodovacie právomoci

## Samostatné rozhodnutia

- potvrdenie prijatia objednávky
- potvrdenie rezervácie
- odoslanie odhadovaného času objednávky
- komunikácia so zákazníkom

## Rozhodnutia vyžadujúce schválenie manažéra

- kompenzácia zákazníka nad stanovený limit
- zmena otváracích hodín
- výnimočné riešenia reklamácií

---

# Workflow

1. Prijme požiadavku zákazníka.
2. Overí dostupnosť produktov alebo termínu rezervácie.
3. Požiada príslušných agentov o potrebné informácie.
4. Informuje zákazníka o výsledku.
5. Sleduje priebeh objednávky až do jej dokončenia.

---

# Rozhodovacia logika

Ak zákazník vytvorí objednávku:

→ over dostupnosť produktov

→ ak sú dostupné, pokračuj

→ ak nie sú dostupné, navrhni alternatívu

→ odošli objednávku do kuchyne

→ informuj zákazníka

---

# Komunikácia

## Prijíma údaje od

- zákazníka
- Inventory Agenta
- Payment Agenta
- Reservation Agenta

## Odosiela údaje

- Kitchen Agentovi
- Inventory Agentovi
- Payment Agentovi
- zákazníkovi

---

# Databáza

## Číta tabuľky

- Customers
- Products
- Orders
- Reservations

## Zapisuje tabuľky

- Orders
- Reservations
- Customer Communication Log

---

# API a externé služby

- SMS API
- Email API
- ChatGPT API
- Platobná brána

---

# Logovanie

Agent zaznamenáva:

- prijaté objednávky
- rezervácie
- komunikáciu so zákazníkom
- chyby systému

---

# Bezpečnostné pravidlá

- Overovať identitu zákazníka pri citlivých operáciách.
- Neposkytovať osobné údaje tretím stranám.
- Dodržiavať GDPR.

---

# KPI

- Priemerný čas odpovede.
- Úspešne spracované objednávky.
- Úspešne spracované rezervácie.
- Spokojnosť zákazníkov.

---

# ROI

**Úspora času:** Automatizácia komunikácie so zákazníkmi.

**Úspora nákladov:** Menej administratívnej práce.

**Zníženie chybovosti:** Eliminácia manuálneho prepisovania objednávok.

**Odhad návratnosti investície:** Bude stanovený podľa veľkosti prevádzky.

---

# Chybové scenáre

- Nedostupný produkt → ponúkne alternatívu.
- Výpadok platobnej brány → ponúkne inú možnosť platby.
- Výpadok systému → uloží údaje a po obnovení ich spracuje.

---

# Budúce rozšírenia

- Hlasový asistent.
- Podpora viacerých jazykov.
- Personalizované odporúčania jedál.
- Integrácia s mobilnou aplikáciou.

---

# Poznámky

Restaurant Assistant je hlavný komunikačný agent systému Smart Restaurant AI a koordinuje komunikáciu medzi zákazníkom a ostatnými AI agentmi.

---

# Stav dokumentu

🟡 Rozpracovaný
