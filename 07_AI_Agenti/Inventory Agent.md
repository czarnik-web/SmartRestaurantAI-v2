# Inventory Agent

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje Inventory Agenta systému Smart Restaurant AI.

Inventory Agent zabezpečuje správu skladových zásob, kontroluje dostupnosť surovín, sleduje dátumy spotreby a pripravuje návrhy objednávok pre dodávateľov.

---

# Identifikácia agenta

**ID:** AG-002

**Názov agenta:** Inventory Agent

**Typ agenta:** Business Agent

**Verzia:** v1.0

**Priorita:** Kritická

**Stav:** 🟡 Rozpracovaný

---

# Business informácie

## Účel agenta

Automatizovať správu skladu a zabezpečiť, aby prevádzke nikdy nechýbali potrebné suroviny.

## Problém, ktorý rieši

Odstraňuje manuálnu kontrolu skladu, znižuje riziko chýb, minimalizuje plytvanie potravinami a šetrí čas personálu.

## Hodnota pre zákazníka

- Automatická kontrola skladu.
- Menej odpadu z exspirovaných surovín.
- Včasné objednávanie tovaru.
- Menej situácií, keď nie je možné pripraviť objednané jedlo.

---

# Kompetencie

## Agent môže

- kontrolovať stav skladu
- odpočítavať suroviny po dokončení objednávky
- sledovať dátumy spotreby
- upozorňovať na nízky stav zásob
- pripravovať návrhy objednávok dodávateľom
- vytvárať reporty o stave skladu
- komunikovať s ostatnými AI agentmi

## Agent nesmie

- meniť receptúry jedál
- meniť ceny produktov
- upravovať sklad bez zaznamenania zmeny
- objednať tovar nad schválený finančný limit bez súhlasu manažéra

---

# Rozhodovacie právomoci

## Samostatné rozhodnutia

- upozorniť na nízky stav skladu
- upozorniť na blížiacu sa exspiráciu
- pripraviť návrh objednávky
- rezervovať suroviny pre potvrdenú objednávku

## Rozhodnutia vyžadujúce schválenie manažéra

- automatické objednávky nad finančný limit
- zmena minimálnych skladových zásob
- zmena dodávateľa
- vyradenie väčšieho množstva surovín

---

# Workflow

1. Prijme informáciu o novej objednávke.
2. Načíta receptúru objednaných produktov.
3. Skontroluje dostupnosť všetkých surovín.
4. Rezervuje potrebné množstvo.
5. Po dokončení objednávky odpočíta spotrebované suroviny zo skladu.
6. Skontroluje minimálne skladové zásoby.
7. Skontroluje dátumy spotreby.
8. Ak je potrebné, pripraví návrh objednávky dodávateľovi.
9. Zapíše všetky zmeny do databázy.

---

# Rozhodovacia logika

Ak je surovina dostupná

↓

Rezervuj potrebné množstvo

↓

Po dokončení objednávky odpočítaj zo skladu

↓

Ak stav skladu klesne pod minimum

↓

Priprav návrh objednávky

↓

Ak suma objednávky presiahne limit

↓

Požiadaj manažéra o schválenie

---

# Komunikácia

## Prijíma údaje od

- Restaurant Assistant
- Kitchen Agent
- Manažér
- Dodávateľ

## Odosiela údaje

- Restaurant Assistant
- Sales Agent
- Reporting Agent
- Manažér

---

# Databáza

## Číta tabuľky

- Ingredients
- Products
- Product_Ingredients
- Suppliers

## Zapisuje tabuľky

- Inventory
- Inventory_Log
- Purchase_Orders

---

# API a externé služby

- API dodávateľov
- Email API

---

# Logovanie

Agent zaznamenáva:

- zmeny skladových zásob
- rezervácie surovín
- objednávky dodávateľom
- upozornenia na exspiráciu
- chyby pri synchronizácii skladu

---

# Bezpečnostné pravidlá

- Každá zmena skladu musí byť zaznamenaná.
- Nie je možné vymazať históriu skladu.
- Každá objednávka dodávateľovi musí byť dohľadateľná.

---

# KPI

- Počet chýbajúcich surovín.
- Počet exspirovaných položiek.
- Presnosť skladových zásob.
- Počet automaticky pripravených objednávok.

---

# ROI

**Úspora času:** Automatická kontrola skladu.

**Úspora nákladov:** Menší odpad a efektívnejšie objednávanie.

**Zníženie chybovosti:** Eliminácia manuálnych chýb pri evidencii skladu.

**Odhad návratnosti investície:** Podľa veľkosti prevádzky.

---

# Chybové scenáre

- Chýbajúca surovina → upozorni Restaurant Assistanta a navrhne alternatívu.
- Exspirácia suroviny → upozorni manažéra a označ iprodukt.
- Výpadok databázy → zaznamenaj chybu a po obnovení synchronizuj údaje.

---

# Budúce rozšírenia

- Predikcia spotreby pomocou AI.
- Automatické objednávky dodávateľom.
- Porovnávanie cien dodávateľov.
- Sezónne plánovanie zásob.
- Optimalizácia skladu podľa histórie predaja.

---

# Poznámky

Inventory Agent je zodpovedný za správnosť skladových zásob a patrí medzi najdôležitejšie agentov systému Smart Restaurant AI.

---

# Stav dokumentu

🟡 Rozpracovaný
