# PATCH /orders//status

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Definovať proces zmeny stavu existujúcej objednávky počas jej životného cyklu v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť bezpečnú a kontrolovanú aktualizáciu stavu objednávky podľa aktuálneho priebehu spracovania.

Zabezpečiť, aby všetky zmeny objednávky prebiehali koordinovane prostredníctvom Restaurant Assistant a boli zaznamenané v systéme.

---

# Endpoint

PATCH /orders/{id}/status

---

# HTTP Metóda

PATCH

---

# URL

/api/v1/orders/{id}/status

---

# Popis

Endpoint aktualizuje aktuálny stav objednávky počas jej životného cyklu.

Zmena stavu je vykonaná iba prostredníctvom Restaurant Assistant, ktorý koordinuje komunikáciu medzi jednotlivými AI agentmi a zabezpečuje správnosť procesu.

Špecializované AI agenty poskytujú informácie zo svojej domény, ale nemenia stav objednávky priamo.

---

# Kto môže volať API

- Restaurant Assistant
- Administrátor systému

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                                  |
| --------- | ---- | -------- | -------------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor objednávky |

---

# Vstupné údaje (Request)

Požiadavka obsahuje:

- Nový stav objednávky
- Dôvod zmeny (voliteľné)
- Identifikátor vykonávateľa zmeny

---

# Workflow

1. Špecializovaný AI agent odošle informáciu o zmene procesu Restaurant Assistantovi.
2. Restaurant Assistant vyhodnotí požiadavku a koordinuje ďalší postup.
3. Systém overí oprávnenie a správnosť požadovanej zmeny stavu.
4. Systém overí, či je prechod medzi stavmi povolený podľa Orders Workflow.
5. Orders Database aktualizuje stav objednávky.
6. Notification Agent odošle informáciu zákazníkovi o zmene stavu.
7. Reporting Agent zaznamená zmenu do štatistík a auditu systému.

---

# Povolené stavy objednávky

- Payment Pending
- Paid
- Preparing
- Ready
- Completed
- Cancelled
- Payment Failed

---

# Odpoveď systému (Response)

Úspešná odpoveď obsahuje:

- Order ID
- Predchádzajúci stav objednávky
- Nový stav objednávky
- Čas zmeny
- Vykonávateľa zmeny

---

# Chybové stavy

- Objednávka neexistuje.
- Neplatný identifikátor objednávky.
- Neplatný prechod medzi stavmi.
- Používateľ alebo systém nemá oprávnenie vykonať zmenu.
- Interná chyba systému.

---

# Audit

Systém zaznamenáva:

- pôvodný stav objednávky,
- nový stav objednávky,
- čas zmeny,
- dôvod zmeny,
- vykonávateľa zmeny.

---

# Bezpečnosť

- Autorizácia požiadavky.
- Kontrola oprávnení.
- Validácia povolených prechodov stavov.
- Audit všetkých zmien objednávky.
- Ochrana proti neoprávneným úpravám.

---

# Business pravidlá

- Stav objednávky je možné meniť iba podľa definovaného Orders Workflow.
- AI agenti nemenia stav objednávky priamo.
- Každá zmena stavu prechádza cez Restaurant Assistant.
- Restaurant Assistant koordinuje proces, ale nenahrádza špecializované AI agenty.
- Každý AI agent je zodpovedný iba za svoju business doménu.
- Objednávky sa v systéme fyzicky neodstraňujú.
- Každá zmena stavu musí byť zaznamenaná.

---

# Súvisiace dokumenty

- Orders Workflow
- Orders Database
- POST /orders
- GET /orders/{id}
- Restaurant Assistant Architecture
- AI Agent Communication

---

# Budúce rozšírenia

- Detailná história zmien objednávky.
- Automatické upozornenia podľa typu zmeny.
- AI predikcia času dokončenia objednávky.
- Analýza priebehu objednávok.

---

# Stav dokumentu

🟢 Hotový
