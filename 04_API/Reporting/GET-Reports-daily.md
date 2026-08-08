# GET /reports/daily

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať denný report o prevádzke reštaurácie.

---

# Business cieľ

Umožniť administrátorovi, Restaurant Assistantovi a Reporting Agentovi získať prehľad o výsledkoch prevádzky za konkrétny deň.

Zabezpečiť automatické spracovanie základných údajov o tržbách, objednávkach, najpredávanejších produktoch a stave zásob.

---

# HTTP Metóda

GET

---

# URL

/api/v1/reports/daily

---

# Query Parameters

| Parameter | Typ  | Povinný | Popis                                               |
| --------- | ---- | -------- | --------------------------------------------------- |
| date      | Date | Nie      | Dátum, za ktorý má byť denný report vytvorený |

Ak parameter date nie je zadaný, systém použije predvolený dátum podľa definovaného Reporting Workflow.

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Workflow

1. Reporting Agent alebo oprávnený používateľ odošle požiadavku na získanie denného reportu.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Reporting Agent získa potrebné údaje z príslušných modulov systému.
4. Systém vypočíta dennú tržbu.
5. Systém spočíta počet objednávok.
6. Systém určí Top 3 najpredávanejšie produkty.
7. Systém získa prehľad skladových položiek, ktoré je potrebné doplniť.
8. Reporting Agent vytvorí denný report.
9. Systém vráti výsledný report.

---

# Kto môže volať API

- Restaurant Assistant
- Reporting Agent
- Administrátor systému

---

# Response

Úspešná odpoveď obsahuje:

- Dátum reportu
- Dennú tržbu
- Počet objednávok
- Top 3 najpredávanejšie produkty
- Skladové položky, ktoré je potrebné doplniť
- Čas vytvorenia reportu

---

# HTTP Status Codes

| Kód | Popis                                        |
| ---- | -------------------------------------------- |
| 200  | Denný report bol úspešne vytvorený       |
| 400  | Neplatný dátum alebo parametre požiadavky |
| 401  | Neautorizovaná požiadavka                  |
| 403  | Nedostatočné oprávnenia                   |
| 500  | Interná chyba systému                      |

---

# Business pravidlá

- Denný report môže zobraziť iba oprávnený používateľ alebo autorizovaný systémový proces.
- Reporting Agent získava údaje potrebné na vytvorenie reportu z príslušných modulov systému.
- Reporting Agent nemení údaje v zdrojových moduloch.
- Denná tržba sa vypočíta iba z úspešne dokončených platieb.
- Počet objednávok sa vypočíta podľa údajov z Orders API.
- Top 3 produkty sa určia podľa počtu predaných kusov.
- Informácie o zásobách sa získavajú prostredníctvom Inventory API.
- Report nesmie obsahovať osobné údaje zákazníkov.
- Údaje reportu musia zodpovedať zvolenému dátumu.

---

# Súvisiace dokumenty

- Reporting Workflow
- Orders API
- Payments API
- Products API
- Inventory API
- Notifications API
- AI Agent Communication

---

# Budúce rozšírenia

- Týždenné reporty.
- Mesačné reporty.
- Porovnanie výsledkov medzi obdobiami.
- Pokročilé finančné štatistiky.
- AI analýza trendov a odporúčania pre prevádzku.

---

# Stav dokumentu

🟢 Hotový
