# Reservations Database

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Správa rezervácií stolov.

---

# Hlavné entity

## Reservation

- Reservation ID
- Customer ID
- Table ID
- Reservation Date
- Guest Count
- Status

---

## Table

- Table ID
- Table Number
- Capacity
- Status

---

## Reservation History

- History ID
- Reservation ID
- Previous Status
- New Status
- Timestamp

---

# Vzťahy

Customer

↓

Reservation

↓

Table

---

# Používatelia databázy

- Reservation Agent
- Restaurant Assistant
- Reporting Agent

---

# Stav dokumentu

🟡 Rozpracovaný
