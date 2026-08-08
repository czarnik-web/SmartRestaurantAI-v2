# GET /orders/

## Verzia dokumentu

v1.0

---

# Účel endpointu

Získať detail konkrétnej objednávky podľa jej jedinečného identifikátora.

---

# Business cieľ

Umožniť zákazníkovi, personálu a interným systémom zobraziť aktuálny stav objednávky vrátane všetkých dôležitých informácií potrebných počas jej životného cyklu.

---

# HTTP Metóda

GET

---

# URL

/api/v1/orders/{id}

---

# Path Parameters

| Parameter | Typ  | Povinný | Popis                                  |
| --------- | ---- | -------- | -------------------------------------- |
| id        | UUID | Áno     | Jedinečný identifikátor objednávky |

---

# Request Body

GET endpoint nevyžaduje Request Body.

---

# Response

Pri úspešnom spracovaní endpoint vráti kompletné informácie o objednávke.

Príklad:

```json
{
  "id": "ord_123456",
  "status": "PREPARING",
  "customer": {
    "id": "cus_001",
    "name": "John Doe"
  },
  "items": [
    {
      "product_id": "prod_001",
      "name": "Pizza Margherita",
      "quantity": 2,
      "price": 8.90
    }
  ],
  "total_price": 17.80,
  "currency": "EUR",
  "created_at": "2026-07-07T18:15:00Z",
  "updated_at": "2026-07-07T18:22:00Z"
}
```

---

# HTTP Status Codes

| Status                    | Popis                                                  |
| ------------------------- | ------------------------------------------------------ |
| 200 OK                    | Objednávka bola úspešne načítaná.                |
| 400 Bad Request           | Neplatný identifikátor objednávky.                  |
| 401 Unauthorized          | Používateľ nie je autentifikovaný.                 |
| 403 Forbidden             | Používateľ nemá oprávnenie zobraziť objednávku. |
| 404 Not Found             | Objednávka neexistuje.                                |
| 500 Internal Server Error | Neočakávaná chyba servera.                          |

# Business pravidlá

- Endpoint vracia údaje iba o jednej objednávke.
- Endpoint slúži iba na čítanie údajov.
- Endpoint neumožňuje meniť stav objednávky.
- Endpoint vracia iba údaje patriace do domény objednávok.
- Údaje o platbe, notifikáciách, reportoch alebo histórii sa získavajú prostredníctvom samostatných API endpointov.
- Objednávky sa v systéme fyzicky neodstraňujú.
- Aktuálny stav objednávky musí zodpovedať workflow systému.
- Prístup k objednávke podlieha autentifikácii a autorizácii.

---

# Súvisiace dokumenty

- Orders Workflow
- Orders Database
- POST /orders
- PATCH /orders/{id}/status

---

# Budúce rozšírenia

- Predpokladaný čas dokončenia objednávky.
- História zmien stavu objednávky.
- Informácie o platbe.
- Informácie o priebehu prípravy v kuchyni.

---

# Stav dokumentu

🟢 Hotový
