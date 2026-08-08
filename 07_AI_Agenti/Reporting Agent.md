# Reporting Agent

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje Reporting Agenta systému Smart Restaurant AI.

Reporting Agent zhromažďuje údaje zo všetkých agentov, vytvára reporty, štatistiky a analytické prehľady pre manažéra.

---

# Identifikácia agenta

**ID:** AG-007

**Názov agenta:** Reporting Agent

**Typ agenta:** Business Agent

**Verzia:** v1.0

**Priorita:** Vysoká

**Stav:** 🟡 Rozpracovaný

---

# Business informácie

## Účel agenta

Poskytovať manažérovi prehľad o fungovaní prevádzky pomocou automaticky generovaných reportov.

## Problém, ktorý rieši

Odstraňuje manuálne vytváranie reportov a umožňuje robiť rozhodnutia na základe aktuálnych dát.

## Hodnota pre zákazníka

- Automatické reporty.
- Prehľad predaja.
- Kontrola nákladov.
- Analýza výkonu prevádzky.
- Úspora času pri administratíve.

---

# Kompetencie

## Agent môže

- vytvárať denné reporty
- vytvárať týždenné reporty
- vytvárať mesačné reporty
- analyzovať predaj
- analyzovať sklad
- analyzovať rezervácie
- analyzovať platby
- vytvárať grafy a štatistiky

## Agent nesmie

- meniť údaje v databáze
- upravovať objednávky
- meniť finančné údaje

---

# Rozhodovacie právomoci

## Samostatné rozhodnutia

- vytvárať reporty
- odosielať reporty manažérovi
- upozorniť na neštandardné hodnoty

## Rozhodnutia vyžadujúce schválenie manažéra

- žiadne

---

# Workflow

1. Získa údaje od ostatných agentov.
2. Vyhodnotí získané dáta.
3. Vytvorí report.
4. Vytvorí grafy a štatistiky.
5. Odošle report manažérovi.

---

# Rozhodovacia logika

Pravidelne zhromažďuje údaje zo systému.

↓

Vyhodnotí KPI.

↓

Porovná výsledky s predchádzajúcim obdobím.

↓

Vytvorí report.

↓

Odošle manažérovi.

---

# Komunikácia

## Prijíma údaje od

- Restaurant Assistant
- Inventory Agent
- Payment Agent
- Reservation Agent
- Sales Agent
- Kitchen Agent

## Odosiela údaje

- Manažér
- Admin Panel

---

# Databáza

## Číta tabuľky

- Orders
- Sales
- Inventory
- Payments
- Reservations
- Logs

## Zapisuje tabuľky

- Reports

---

# API a externé služby

Žiadne.

---

# Logovanie

Agent zaznamenáva

- vytvorené reporty
- chyby analýzy
- odoslané reporty

---

# Bezpečnostné pravidlá

- Reporty sú dostupné iba oprávneným používateľom.
- Finančné údaje nesmú byť verejne dostupné.

---

# KPI

- Počet vytvorených reportov.
- Čas vytvorenia reportu.
- Presnosť údajov.
- Počet upozornení pre manažéra.

---

# ROI

**Úspora času:** Automatické reportovanie.

**Úspora nákladov:** Menej administratívy.

**Zníženie chybovosti:** Eliminácia manuálne vytváraných reportov.

**Odhad návratnosti investície:** Vyššia kvalita rozhodovania.

---

# Chybové scenáre

- Chýbajú údaje → upozorni manažéra.
- Výpadok databázy → vytvor report po obnovení systému.

---

# Budúce rozšírenia

- AI predikcie predaja.
- Dashboard v reálnom čase.
- Export do PDF a Excelu.
- Automatické porovnávanie období.

---

# Poznámky

Reporting Agent poskytuje manažérovi kompletný prehľad o fungovaní celej prevádzky.

---

# Stav dokumentu

🟡 Rozpracovaný
