# Users Database

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Správa používateľov systému.

---

# Hlavné entity

## User

- User ID
- First Name
- Last Name
- Email
- Role
- Status

---

## Role

- Role ID
- Role Name
- Description

---

## Permission

- Permission ID
- Permission Name

---

## Session

- Session ID
- User ID
- Login Time
- Logout Time

---

# Vzťahy

User

↓

Role

↓

Permission

---

User

↓

Session

---

# Používatelia databázy

- Security Agent
- System Monitor Agent

---

# Stav dokumentu

🟡 Rozpracovaný
