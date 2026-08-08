# Sales Agent

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje Sales Agenta systému Smart Restaurant AI.

Sales Agent analyzuje predaj, stav skladu a správanie zákazníkov. Navrhuje zľavy, akcie a predajné stratégie s cieľom maximalizovať zisk a minimalizovať straty spôsobené nepredaným tovarom.

---

# Identifikácia agenta

**ID:** AG-005

**Názov agenta:** Sales Agent

**Typ agenta:** Business Agent

**Verzia:** v1.0

**Priorita:** Vysoká

**Stav:** 🟡 Rozpracovaný

---

# Business informácie

## Účel agenta

Optimalizovať predaj produktov pomocou inteligentných zliav a obchodných odporúčaní.

## Problém, ktorý rieši

Minimalizuje straty zo surovín s blížiacim sa dátumom spotreby, pomáha udržiavať optimálny stav skladu a zvyšuje celkový zisk prevádzky.

## Hodnota pre zákazníka

- Inteligentné zľavy.
- Menší odpad.
- Vyšší zisk.
- Lepšie využitie skladových zásob.
- Automatické obchodné odporúčania.

---

# Kompetencie

## Agent môže

- analyzovať predaje
- analyzovať stav skladu
- navrhovať zľavy
- odporúčať sezónne produkty
- zvýrazniť produkty s blížiacou sa exspiráciou
- pripravovať reporty pre manažéra

## Agent nesmie

- meniť základné ceny produktov
- znižovať maržu pod nastavený limit
- vytvárať akcie bez evidencie
- meniť obchodné pravidlá systému

---

# Rozhodovacie právomoci

## Samostatné rozhodnutia

- navrhovať zľavy podľa pravidiel
- zvýrazniť produkty na predaj
- odporučiť sezónne produkty
- vytvoriť obchodný report

## Rozhodnutia vyžadujúce schválenie manažéra

- mimoriadne zľavy
- zmena obchodnej stratégie
- dlhodobé akcie
- výpredaje celej kategórie

---

# Workflow

1. Načíta údaje o predaji.
2. Skontroluje stav skladu.
3. Skontroluje dátumy spotreby.
4. Vyhodnotí marže.
5. Navrhne zľavy podľa pravidiel.
6. Informuje manažéra.
7. Sleduje výsledky predaja.

---

# Rozhodovacia logika

Agent vyhodnocuje:

- stav skladu
- predaj za posledných 7 dní
- dátum spotreby
- počasie
- maržu produktu
- deň v týždni
- počet rezervácií

Na základe týchto údajov navrhne vhodnú obchodnú stratégiu.

---

# Komunikácia

## Prijíma údaje od

- Inventory Agent
- Restaurant Assistant
- Reporting Agent
- Manažér

## Odosiela údaje

- Manažér
- Restaurant Assistant
- Marketing Agent

---

# Databáza

## Číta tabuľky

- Products
- Sales
- Inventory
- Reservations

## Zapisuje tabuľky

- Promotions
- Sales_Recommendations
- Sales_Log

---

# API a externé služby

- Weather API

---

# Logovanie

Agent zaznamenáva

- vytvorené zľavy
- odporúčania
- obchodné analýzy
- upozornenia pre manažéra

---

# Bezpečnostné pravidlá

- Dodržiava minimálnu povolenú maržu.
- Každá zľava musí byť zaznamenaná.
- Obchodné pravidlá môže meniť iba manažér.

---

# KPI

- Obrat predaja.
- Počet predaných produktov v akcii.
- Zníženie odpadu.
- Zvýšenie zisku.

---

# ROI

**Úspora času:** Automatická analýza predaja.

**Úspora nákladov:** Menšie straty zo skladu.

**Zníženie chybovosti:** Objektívne rozhodovanie podľa dát.

**Odhad návratnosti investície:** Zvýšenie efektivity predaja.

---

# Chybové scenáre

- Chýbajú údaje o predaji → upozorni manažéra.
- Chýbajú skladové údaje → pozastav analýzu.
- Výpadok Weather API → pokračuj bez počasia.

---

# Budúce rozšírenia

- Predikcia predaja pomocou AI.
- Dynamické určovanie cien.
- Automatické tvorenie akciových balíkov.
- Personalizované ponuky pre zákazníkov.
- Analýza konkurencie.

---

# Poznámky

Sales Agent spolupracuje najmä s Inventory Agentom a Restaurant Assistantom. Jeho cieľom je maximalizovať zisk pri zachovaní obchodných pravidiel prevádzky.

---

# Stav dokumentu

🟡 Rozpracovaný
