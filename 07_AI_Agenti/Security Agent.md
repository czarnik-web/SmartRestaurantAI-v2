# Security Agent

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje Security Agenta systému Smart Restaurant AI.

Security Agent zabezpečuje ochranu systému, správu používateľských oprávnení, monitorovanie aktivít a evidenciu bezpečnostných udalostí.

---

# Identifikácia agenta

**ID:** AG-008

**Názov agenta:** Security Agent

**Typ agenta:** System Agent

**Verzia:** v1.0

**Priorita:** Kritická

**Stav:** 🟡 Rozpracovaný

---

# Business informácie

## Účel agenta

Chrániť systém, údaje zákazníkov a firemné informácie pred neoprávneným prístupom.

## Problém, ktorý rieši

Minimalizuje bezpečnostné riziká, sleduje podozrivé aktivity a zabezpečuje, aby mal každý používateľ prístup iba k svojim oprávneniam.

## Hodnota pre zákazníka

- Bezpečné uloženie údajov.
- Kontrola prístupov.
- Evidencia všetkých dôležitých udalostí.
- Ochrana pred neoprávnenými zásahmi.

---

# Kompetencie

## Agent môže

- spravovať používateľské oprávnenia
- monitorovať prihlásenia
- zaznamenávať bezpečnostné udalosti
- upozorniť na podozrivé aktivity
- blokovať neoprávnené pokusy o prístup

## Agent nesmie

- meniť obchodné údaje
- meniť objednávky
- vykonávať finančné operácie
- meniť skladové údaje

---

# Rozhodovacie právomoci

## Samostatné rozhodnutia

- zablokovať podozrivé prihlásenie
- upozorniť administrátora
- zaznamenať bezpečnostný incident

## Rozhodnutia vyžadujúce schválenie manažéra

- vytvorenie nového administrátora
- zmena bezpečnostných pravidiel
- trvalé zablokovanie používateľa

---

# Workflow

1. Sleduje prihlásenia používateľov.
2. Kontroluje oprávnenia.
3. Monitoruje systémové udalosti.
4. Zaznamenáva bezpečnostné incidenty.
5. Informuje administrátora alebo manažéra.

---

# Rozhodovacia logika

Ak je prihlásenie úspešné

↓

Over oprávnenia

↓

Povoľ prístup

Ak je zistená podozrivá aktivita

↓

Zablokuj prístup

↓

Vytvor záznam

↓

Informuj administrátora

---

# Komunikácia

## Prijíma údaje od

- všetkých agentov
- používateľov systému

## Odosiela údaje

- administrátor
- manažér
- Reporting Agent

---

# Databáza

## Číta tabuľky

- Users
- Roles
- Permissions
- Security_Log

## Zapisuje tabuľky

- Security_Log
- User_Sessions

---

# API a externé služby

- Autentifikačný systém

---

# Logovanie

Agent zaznamenáva

- prihlásenia
- odhlásenia
- neúspešné pokusy
- zmeny oprávnení
- bezpečnostné incidenty

---

# Bezpečnostné pravidlá

- Každá udalosť musí byť zaznamenaná.
- Používatelia majú iba potrebné oprávnenia.
- Citlivé údaje musia byť chránené.

---

# KPI

- Počet bezpečnostných incidentov.
- Počet neúspešných prihlásení.
- Čas reakcie na incident.
- Dostupnosť systému.

---

# ROI

**Úspora času:** Automatické monitorovanie systému.

**Úspora nákladov:** Prevencia bezpečnostných incidentov.

**Zníženie chybovosti:** Kontrola oprávnení a prístupov.

**Odhad návratnosti investície:** Vyššia bezpečnosť systému.

---

# Chybové scenáre

- Opakované neúspešné prihlásenie → dočasne zablokuj účet.
- Neoprávnený prístup → zaznamenaj incident a informuj administrátora.
- Výpadok autentifikačného systému → obmedz prístup a upozorni správcu.

---

# Budúce rozšírenia

- Dvojfaktorové overenie (2FA).
- AI detekcia podozrivého správania.
- Automatické bezpečnostné audity.
- Integrácia s externými bezpečnostnými systémami.

---

# Poznámky

Security Agent zabezpečuje ochranu celej platformy Smart Restaurant AI a spolupracuje so všetkými ostatnými agentmi.

---

# Stav dokumentu

🟡 Rozpracovaný
