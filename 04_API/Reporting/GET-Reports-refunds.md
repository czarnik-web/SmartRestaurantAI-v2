# GET /reports/refunds

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať prehľad refundácií za zvolené časové obdobie.

---

# Business cieľ

Umožniť administrátorovi, Restaurant Assistantovi a Reporting Agentovi sledovať vrátené platby a dôvody ich vzniku.

Zabezpečiť prehľad o počte refundácií a ich celkovej hodnote bez sprístupnenia citlivých osobných údajov zákazníkov.

---

# HTTP Metóda

GET

---

# URL

/api/v1/reports/refunds

---

# Query Parameters

| Parameter | Typ  | Povinný | Popis                          |
| --------- | ---- | -------- | ------------------------------ |
| from_date | Date | Áno     | Začiatok sledovaného obdobia |
| to_date   | Date | Áno     | Koniec sledovaného obdobia    |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Reporting Agent alebo oprávnený používateľ odošle požiadavku na získanie reportu refundácií.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Reporting Agent získa potrebné údaje z Payments modulu.
4. Systém vyberie refundácie patriace do zvoleného časového obdobia.
5. Systém vypočíta počet refundácií.
6. Systém vypočíta celkovú hodnotu refundovaných platieb.
7. Systém spracuje dostupné dôvody refundácií.
8. Reporting Agent vytvorí report refundácií.
9. Systém vráti výsledný report.

---

# Kto môže volať API

- Restaurant Assistant
- Reporting Agent
- Administrátor systému

---

# Response

Úspešná odpoveď obsahuje:

- Začiatok sledovaného obdobia
- Koniec sledovaného obdobia
- Počet refundácií
- Celkovú hodnotu refundácií
- Prehľad dôvodov refundácií
- Čas vytvorenia reportu

---

# HTTP Status Codes

| Kód | Popis                                                  |
| ---- | ------------------------------------------------------ |
| 200  | Report refundácií bol úspešne vytvorený           |
| 400  | Neplatné časové obdobie alebo parametre požiadavky |
| 401  | Neautorizovaná požiadavka                            |
| 403  | Nedostatočné oprávnenia                             |
| 500  | Interná chyba systému                                |

---

# Business pravidlá

- Report refundácií môže zobraziť iba oprávnený používateľ alebo autorizovaný systémový proces.
- Reporting Agent nemení údaje v Payments module.
- Do reportu sa započítavajú iba skutočne vykonané refundácie.
- Celková hodnota refundácií sa vypočíta zo skutočne vrátených súm.
- Dôvod refundácie sa použije iba vtedy, ak je v systéme zaznamenaný.
- Report nesmie obsahovať citlivé platobné údaje zákazníkov.
- Report nesmie obsahovať osobné údaje zákazníkov.
- Údaje reportu musia zodpovedať zvolenému časovému obdobiu.

---

# Súvisiace dokumenty

- GET /reports/daily
- GET /reports/sales
- Reporting Workflow
- Payments API
- Orders API
- AI Agent Communication

---

# Budúce rozšírenia

- Analýza najčastejších dôvodov refundácií.
- Porovnanie refundácií medzi obdobiami.
- Refundácie podľa produktov.
- Refundácie podľa typu objednávky.
- AI analýza príčin zvýšeného počtu refundácií.

---

# Stav dokumentu

🟢 Hotový
