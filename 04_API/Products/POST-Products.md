# POST /products

## Verzia dokumentu

v1.0

---

# Účel endpointu

Vytvoriť nový produkt v systéme Smart Restaurant AI.

---

# Business cieľ

Umožniť administrátorovi vytvárať nové produkty, ktoré budú dostupné v ponuke reštaurácie.

Zabezpečiť, aby vytváranie produktov bolo kontrolované a aby AI agenti nemohli samostatne pridávať nové produkty do ponuky.

---

# HTTP Metóda

POST

---

# URL

/api/v1/products

---

# Request Body

Požiadavka obsahuje:

- Názov produktu
- Popis produktu
- Kategóriu
- Predajnú cenu
- Menu
- Alergény
- Zloženie produktu
- Dostupnosť
- Stav produktu

---

# Response

Úspešná odpoveď obsahuje:

- Product ID
- Názov produktu
- Kategóriu
- Predajnú cenu
- Dostupnosť
- Stav produktu
- Dátum vytvorenia

---

# HTTP Status Codes

| Kód | Popis                                     |
| ---- | ----------------------------------------- |
| 201  | Produkt bol úspešne vytvorený          |
| 400  | Neplatné alebo neúplné vstupné údaje |
| 401  | Neautorizovaná požiadavka               |
| 403  | Nedostatočné oprávnenia                |
| 409  | Produkt s rovnakými údajmi už existuje |
| 500  | Interná chyba systému                   |

---

# Business pravidlá

- Nový produkt môže vytvoriť iba administrátor systému.
- AI agenti nemôžu samostatne vytvárať nové produkty.
- Každý produkt musí mať jedinečný Product ID.
- Produkt musí obsahovať všetky povinné údaje.
- Cena produktu je určená administrátorom.
- AI agenti nemôžu samostatne meniť cenu produktu.
- Zloženie produktu vytvorené administrátorom predstavuje oficiálnu definíciu produktu.
- Individuálne úpravy produktu zákazníkom sa vzťahujú iba na konkrétnu objednávku a nemenia produkt uložený v Products Database.
- Novovytvorený produkt musí mať definovaný stav a dostupnosť.

---

# Súvisiace dokumenty

- GET /products/{id}
- GET /products
- PATCH /products/{id}
- PATCH /products/{id}/status
- Products Database
- Orders API
- Inventory API

---

# Budúce rozšírenia

- Fotografie produktov.
- Nutričné hodnoty.
- Rozšírené varianty produktov.
- Platené doplnky a extra suroviny.
- Hromadný import produktov.

---

# Stav dokumentu

🟢 Hotový
