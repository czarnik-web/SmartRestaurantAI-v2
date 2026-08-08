# Backup Agent

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje Backup Agenta systému Smart Restaurant AI.

Backup Agent zabezpečuje automatické zálohovanie databáz, konfigurácií systému a dôležitých súborov. Umožňuje obnovu systému po zlyhaní alebo strate dát.

---

# Identifikácia agenta

**ID:** AG-011

**Názov agenta:** Backup Agent

**Typ agenta:** System Agent

**Verzia:** v1.0

**Priorita:** Kritická

**Stav:** 🟡 Rozpracovaný

---

# Business informácie

## Účel agenta

Chrániť údaje zákazníka pred stratou a zabezpečiť rýchlu obnovu systému.

## Problém, ktorý rieši

Minimalizuje riziko straty údajov spôsobenej poruchou hardvéru, chybou používateľa alebo výpadkom systému.

## Hodnota pre zákazníka

- Automatické zálohovanie.
- Rýchla obnova systému.
- Ochrana firemných údajov.
- Istota pri technických problémoch.

---

# Kompetencie

## Agent môže

- vytvárať automatické zálohy
- vytvárať manuálne zálohy
- kontrolovať úspešnosť záloh
- obnovovať údaje zo zálohy
- archivovať staršie zálohy
- upozorniť administrátora na chybu

## Agent nesmie

- meniť obsah databázy počas zálohovania
- mazať poslednú funkčnú zálohu
- obnoviť systém bez oprávnenia administrátora

---

# Rozhodovacie právomoci

## Samostatné rozhodnutia

- spustiť plánovanú zálohu
- overiť integritu zálohy
- archivovať staré zálohy

## Rozhodnutia vyžadujúce schválenie administrátora

- obnova systému
- zmena harmonogramu záloh
- trvalé odstránenie záloh

---

# Workflow

1. Spustí plánovanú zálohu.
2. Vytvorí záložný súbor.
3. Overí integritu zálohy.
4. Uloží zálohu.
5. Zapíše výsledok do logu.
6. Informuje administrátora o úspechu alebo chybe.

---

# Rozhodovacia logika

Ak je záloha úspešná

↓

Over integritu

↓

Archivuj podľa pravidiel

↓

Zapíš výsledok

Ak záloha zlyhá

↓

Opakuj pokus

↓

Ak opakovane zlyhá

↓

Informuj administrátora

---

# Komunikácia

## Prijíma údaje od

- databázy
- administrátora
- System Monitor Agenta

## Odosiela údaje

- administrátor
- Reporting Agent
- Notification Agent

---

# Databáza

## Číta tabuľky

- všetky systémové databázy

## Zapisuje tabuľky

- Backup_Log

---

# API a externé služby

- Cloud Storage
- Lokálne úložisko

---

# Logovanie

Agent zaznamenáva

- čas vytvorenia zálohy
- veľkosť zálohy
- úspešnosť zálohy
- obnovy systému
- chyby zálohovania

---

# Bezpečnostné pravidlá

- Zálohy musia byť šifrované.
- Prístup k zálohám majú iba oprávnení administrátori.
- Posledná funkčná záloha nesmie byť odstránená.

---

# KPI

- Úspešnosť záloh.
- Čas vytvorenia zálohy.
- Čas obnovy systému.
- Počet úspešných obnov.

---

# ROI

**Úspora času:** Automatizované zálohovanie.

**Úspora nákladov:** Prevencia straty dát.

**Zníženie rizika:** Možnosť rýchlej obnovy systému.

**Odhad návratnosti investície:** Ochrana kritických firemných údajov.

---

# Chybové scenáre

- Nedostatok miesta na disku.
- Poškodená záloha.
- Výpadok úložiska.
- Chyba pri obnove systému.

---

# Budúce rozšírenia

- Inkrementálne zálohy.
- Geograficky oddelené zálohy.
- AI kontrola integrity dát.
- Automatická obnova testovacieho prostredia.

---

# Poznámky

Backup Agent zabezpečuje ochranu všetkých údajov platformy Smart Restaurant AI a spolupracuje so System Monitor Agentom pri riešení technických incidentov.

---

# Stav dokumentu

🟡 Rozpracovaný
