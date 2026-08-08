# Reservation Agent

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje Reservation Agenta systému Smart Restaurant AI.

Reservation Agent zabezpečuje správu rezervácií, kontroluje dostupnosť stolov, komunikuje so zákazníkmi a optimalizuje obsadenosť reštaurácie.

---

# Identifikácia agenta

**ID:** AG-004

**Názov agenta:** Reservation Agent

**Typ agenta:** Business Agent

**Verzia:** v1.0

**Priorita:** Vysoká

**Stav:** 🟡 Rozpracovaný

---

# Business informácie

## Účel agenta

Automatizovať správu rezervácií a zabezpečiť efektívne využitie kapacity reštaurácie.

## Problém, ktorý rieši

Odstraňuje manuálne zapisovanie rezervácií, predchádza dvojitým rezerváciám a znižuje čas potrebný na komunikáciu so zákazníkmi.

## Hodnota pre zákazníka

- Okamžité potvrdenie rezervácie.
- Prehľad voľných termínov.
- Automatické pripomienky rezervácie.
- Jednoduchá zmena alebo zrušenie rezervácie.

---

# Kompetencie

## Agent môže

- prijímať rezervácie
- meniť rezervácie po potvrdení zákazníka
- zrušiť rezerváciu po potvrdení zákazníka
- kontrolovať dostupnosť stolov
- odosielať potvrdenia rezervácií
- odosielať pripomienky rezervácií
- navrhovať alternatívne termíny

## Agent nesmie

- zrušiť rezerváciu bez potvrdenia zákazníka
- meniť otváracie hodiny
- meniť kapacitu reštaurácie
- poskytovať údaje o iných zákazníkoch

---

# Rozhodovacie právomoci

## Samostatné rozhodnutia

- potvrdiť rezerváciu
- navrhnúť iný termín
- odoslať potvrdenie zákazníkovi
- odoslať pripomienku rezervácie

## Rozhodnutia vyžadujúce schválenie manažéra

- rezervácia mimo otváracích hodín
- rezervácia veľkej skupiny nad stanovený limit
- rezervácia uzavretej spoločnosti
- blokovanie väčšej časti kapacity reštaurácie

---

# Workflow

1. Prijme požiadavku na rezerváciu.
2. Skontroluje dostupnosť stolov.
3. Vyhodnotí kapacitu reštaurácie.
4. Potvrdí rezerváciu alebo navrhne alternatívu.
5. Zapíše rezerváciu do databázy.
6. Odošle potvrdenie zákazníkovi.
7. Pred termínom rezervácie odošle pripomienku.

---

# Rozhodovacia logika

Ak je stôl voľný

↓

Potvrď rezerváciu

↓

Zapíš rezerváciu

↓

Odošli potvrdenie

Ak stôl nie je voľný

↓

Navrhni najbližší voľný termín

↓

Čakaj na potvrdenie zákazníka

---

# Komunikácia

## Prijíma údaje od

- Restaurant Assistant
- zákazník
- manažér

## Odosiela údaje

- Restaurant Assistant
- zákazník
- Reporting Agent

---

# Databáza

## Číta tabuľky

- Reservations
- Tables
- Customers

## Zapisuje tabuľky

- Reservations
- Reservation_Log

---

# API a externé služby

- Email API
- SMS API
- Kalendár

---

# Logovanie

Agent zaznamenáva

- nové rezervácie
- zmeny rezervácií
- zrušené rezervácie
- neúspešné rezervácie

---

# Bezpečnostné pravidlá

- Overovať identitu zákazníka pri zmene rezervácie.
- Nezverejňovať rezervácie iných zákazníkov.
- Uchovávať históriu zmien rezervácií.

---

# KPI

- Počet rezervácií.
- Počet zrušených rezervácií.
- Obsadenosť stolov.
- Úspešnosť rezervácií.

---

# ROI

**Úspora času:** Automatizácia rezervácií.

**Úspora nákladov:** Menej telefonickej komunikácie.

**Zníženie chybovosti:** Eliminácia dvojitých rezervácií.

**Odhad návratnosti investície:** Podľa počtu rezervácií.

---

# Chybové scenáre

- Plná kapacita → navrhni alternatívny termín.
- Výpadok databázy → zaznamenaj požiadavku a po obnovení ju spracuj.
- Duplicitná rezervácia → upozorni zákazníka a ponúkni iné riešenie.

---

# Budúce rozšírenia

- Výber konkrétneho stola.
- Online správa rezervácie zákazníkom.
- Automatický čakací zoznam.
- Predikcia nevyužitých rezervácií.
- Integrácia s mobilnou aplikáciou.

---

# Poznámky

Reservation Agent zabezpečuje kompletnú správu rezervácií a spolupracuje s Restaurant Assistantom pri komunikácii so zákazníkmi.

---

# Stav dokumentu

🟡 Rozpracovaný
