# Database Overview

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument definuje hlavné databázové oblasti systému Smart Restaurant AI.

Jeho cieľom je poskytnúť prehľad všetkých dátových celkov, ktoré budú využívať jednotliví agenti systému.

---

# Databázové oblasti

## Customers

Údaje o zákazníkoch.

### Obsahuje

- Customer
- Customer Preferences
- Customer History
- Loyalty Account

### Používa

- Restaurant Assistant
- Reservation Agent
- Notification Agent
- Sales Agent

---

## Orders

Údaje o objednávkach.

### Obsahuje

- Order
- Order Item
- Order Status
- Order History

### Používa

- Restaurant Assistant
- Kitchen Agent
- Payment Agent
- Reporting Agent

---

## Products

Údaje o produktoch.

### Obsahuje

- Product
- Product Category
- Product Price
- Product Availability

### Používa

- Restaurant Assistant
- Inventory Agent
- Kitchen Agent
- Sales Agent

---

## Inventory

Údaje o sklade.

### Obsahuje

- Inventory Item
- Ingredient
- Stock Movement
- Inventory Alert

### Používa

- Inventory Agent
- Kitchen Agent
- Sales Agent

---

## Reservations

Údaje o rezerváciách.

### Obsahuje

- Reservation
- Reservation Status
- Table
- Reservation History

### Používa

- Reservation Agent
- Restaurant Assistant
- Reporting Agent

---

## Payments

Údaje o platbách.

### Obsahuje

- Payment
- Payment Status
- Refund
- Payment Log

### Používa

- Payment Agent
- Reporting Agent

---

## Users

Používatelia systému.

### Obsahuje

- User
- Role
- Permission
- Session

### Používa

- Security Agent
- System Monitor Agent

---

## Notifications

Komunikačné údaje.

### Obsahuje

- Notification
- Notification Template
- Notification Log

### Používa

- Notification Agent

---

## Reports

Výstupy a analytika.

### Obsahuje

- Daily Report
- Weekly Report
- Monthly Report
- KPI Report

### Používa

- Reporting Agent

---

## System

Technické údaje systému.

### Obsahuje

- System Status
- Service Status
- Monitoring Log
- Incident Log
- Backup Log

### Používa

- Security Agent
- System Monitor Agent
- Backup Agent

---

# Vzťahy medzi databázovými oblasťami

Customers

↓

Orders

↓

Payments

↓

Reports

---

Products

↓

Inventory

↓

Kitchen

↓

Orders

---

Customers

↓

Reservations

↓

Reports

---

Users

↓

Security

↓

System

---

# Databázové princípy

- Každá oblasť má vlastnú zodpovednosť.
- Dáta sa neukladajú duplicitne.
- Každá zmena musí byť dohľadateľná.
- Kritické operácie musia byť logované.
- Bezpečnostné údaje sú oddelené od business dát.

---

# Budúce rozšírenia

- Supplier Management
- Delivery Management
- Marketing Module
- Accounting Module
- AI Analytics Module

---

# Poznámky

Tento dokument predstavuje najvyššiu úroveň databázovej architektúry Smart Restaurant AI.

Detailné tabuľky budú definované v samostatných dokumentoch.
