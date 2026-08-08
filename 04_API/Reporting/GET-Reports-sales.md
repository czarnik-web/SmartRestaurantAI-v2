# GET /reports/sales

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať prehľad predaja za zvolené časové obdobie.

---

# Business cieľ

Umožniť administrátorovi, Restaurant Assistantovi a Reporting Agentovi sledovať základné výsledky predaja reštaurácie.

Zabezpečiť prehľad o tržbách, počte predaných produktov a najpredávanejších produktoch za vybrané obdobie.

---

# HTTP Metóda

GET

---

# URL

/api/v1/reports/sales

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

1. Reporting Agent alebo oprávnený používateľ odošle požiadavku na získanie reportu predaja.
2. Systém overí identitu a oprávnenie žiadateľa.
3. Reporting Agent získa potrebné údaje z príslušných modulov systému.
4. Systém vyberie údaje patriace do zvoleného časového obdobia.
5. Systém vypočíta celkovú tržbu.
6. Systém vypočíta počet dokončených objednávok.
7. Systém vypočíta počet predaných produktov.
8. Systém určí najpredávanejšie produkty.
9. Reporting Agent vytvorí report predaja.
10. Systém vráti výsledný report.

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
- Celkovú tržbu
- Počet dokončených objednávok
- Počet predaných produktov
- Najpredávanejšie produkty
- Čas vytvorenia reportu

---

# HTTP Status Codes

| Kód | Popis                                                  |
| ---- | ------------------------------------------------------ |
| 200  | Report predaja bol úspešne vytvorený                |
| 400  | Neplatné časové obdobie alebo parametre požiadavky |
| 401  | Neautorizovaná požiadavka                            |
| 403  | Nedostatočné oprávnenia                             |
| 500  | Interná chyba systému                                |

---

# Business pravidlá

- Report predaja môže zobraziť iba oprávnený používateľ alebo autorizovaný systémový proces.
- Reporting Agent nemení údaje v zdrojových moduloch.
- Celková tržba sa vypočíta iba z úspešne dokončených platieb.
- Do počtu dokončených objednávok sa započítavajú iba objednávky v dokončenom stave.
- Zrušené objednávky sa nezapočítavajú do výsledkov predaja.
- Najpredávanejšie produkty sa určujú podľa počtu predaných kusov.
- Report nesmie obsahovať osobné údaje zákazníkov.
- Údaje reportu musia zodpovedať zvolenému časovému obdobiu.

---

# Súvisiace dokumenty

- GET /reports/daily
- Reporting Workflow
- Orders API
- Payments API
- Products API
- AI Agent Communication

---

# Budúce rozšírenia

- Porovnanie predaja medzi obdobiami.
- Predaj podľa kategórií produktov.
- Priemerná hodnota objednávky.
- Analýza predaja podľa času a dní.
- AI analýza trendov predaja.

---

# Stav dokumentu

🟢 Hotový
