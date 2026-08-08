# Kitchen Workflow

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať kompletný proces spracovania objednávky v kuchyni.

---

# Business cieľ

Zabezpečiť efektívne spracovanie objednávok od ich prijatia až po dokončenie.

---

# Začiatok procesu

Proces začína vo chvíli, keď je objednávka potvrdená.

---

# Workflow

## 1. Prijatie objednávky

Restaurant Assistant odošle objednávku Kitchen Agentovi.

↓

Kitchen Agent zaradí objednávku do fronty.

---

## 2. Čakanie vo fronte

Objednávka čaká na pridelenie kuchárovi.

↓

Stav:

Waiting

---

## 3. Začatie prípravy

Kuchár prijme objednávku.

↓

Kitchen Agent zmení stav.

↓

Preparing

---

## 4. Príprava jedla

Kuchyňa pripravuje objednávku.

Počas prípravy môže byť:

- pozastavená
- upravená
- zrušená

---

## 5. Dokončenie

Kuchár označí objednávku ako hotovú prostredníctvom používateľského rozhrania.

Restaurant Assistant pred zmenou stavu overí, či je zmena platná.

Ak je zmena povolená:

↓

Kitchen Agent odošle informáciu Restaurant Assistantovi.

↓

Restaurant Assistant zmení stav objednávky na **Ready**.

↓

Notification Agent pripraví oznámenie pre zákazníka.

↓

Reporting Agent zapíše zmenu do histórie objednávky.

---

## 6. Oznámenie

Notification Agent informuje:

- zákazníka
- čašníka
- výdajné miesto

---

## 7. Výdaj

Objednávka je odovzdaná zákazníkovi.

↓

Restaurant Assistant nastaví stav.

↓

Completed

---

# AI Agenti

- Restaurant Assistant
- Kitchen Agent
- Notification Agent
- Reporting Agent

---

# Databázy

- Orders Database
- Products Database

---

# Stavy objednávky

Waiting

↓

Preparing

↓

Ready

↓

Completed

Možné alternatívne stavy:

Paused

Cancelled

---

# Koniec procesu

Proces končí úspešným vydaním objednávky alebo jej zrušením.

---

# Budúce rozšírenia

- Priorita objednávok
- Viac kuchynských staníc
- Automatické prideľovanie kuchárov
- AI odhad času prípravy
- Integrácia s Kitchen Display System (KDS)

---

# Stav dokumentu

🟡 Rozpracovaný
