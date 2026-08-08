# Payments Database

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje databázovú oblasť Payments systému Smart Restaurant AI.

Payments Database slúži na evidenciu platieb, refundácií a histórie finančných transakcií.

---

# Business cieľ

Zabezpečiť bezpečné spracovanie a evidenciu všetkých platieb.

---

# Hlavné entity

## Payment

- Payment ID
- Order ID
- Payment Method
- Amount
- Status
- Payment Date

---

## Payment Status

- Pending
- Paid
- Failed
- Refunded
- Cancelled

---

## Refund

- Refund ID
- Payment ID
- Refund Amount
- Refund Date
- Reason

---

## Payment Log

- Log ID
- Payment ID
- Event
- Timestamp

---

# Vzťahy

Order

↓

Payment

↓

Refund

---

Payment

↓

Payment Log

---

# Používatelia databázy

- Payment Agent
- Reporting Agent
- Restaurant Assistant

---

# Stav dokumentu

🟡 Rozpracovaný
