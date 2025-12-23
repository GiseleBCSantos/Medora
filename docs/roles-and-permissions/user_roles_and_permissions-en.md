# 👥 User Roles and Permissions — Medora

Medora adopts a **Role-Based Access Control (RBAC)** model, where each user has
permissions strictly aligned with their responsibilities inside the clinical ecosystem.

This document describes **what each user role can and cannot do**, as well as
which **domain entities** each role can access.

---

## 🧑‍🦱 Patient

### 🎯 Role Objective

Consume healthcare services, manage appointments, and access personal clinical data.

### ✅ Allowed Actions

- Create and manage own account
- Search professionals and clinics
- View available schedules
- Request appointments
- Reschedule or cancel appointments (according to clinic policy)
- Pay for private appointments
- Perform check-in (QR Code)
- Join teleconsultations
- View and download:
  - medical reports
  - prescriptions
  - certificates
- Review professionals and clinics
- Send messages related to an appointment

### ❌ Restricted Actions

- Create or modify medical schedules
- Access other patients’ medical records
- Change consultation prices
- Issue medical documents
- Access clinic financial data
- Manually confirm payments

### 🔗 Accessible Entities

- Patient
- Appointment
- Document (own only)
- Payment (own only)
- Message
- Review

---

## 🧑‍⚕️ Doctor / Healthcare Professional

> **Strictly clinical role. No administrative responsibilities.**

### 🎯 Role Objective

Provide healthcare services, register clinical data, and issue medical documents.

### ✅ Allowed Actions

- View personal daily schedule
- Start in-person or online appointments
- Access medical records of assigned patients
- Register clinical evolution
- Issue:
  - prescriptions
  - medical reports
  - certificates
- Close appointments
- View received reviews
- Use clinical AI features (if enabled)

### ❌ Restricted Actions

- Create or edit schedules
- Change consultation prices
- Manage insurance plans
- Define appointment limits
- Access clinic financial data
- Approve or reject appointments

### 🔗 Accessible Entities

- Doctor
- Appointment
- MedicalRecord
- Document
- Review

---

## 🧑‍💼 Secretary / Attendant

> **Operational role within the clinic.**

### 🎯 Role Objective

Manage schedules, organize appointments, and mediate patient–professional interaction.

### ✅ Allowed Actions

- Create and edit medical schedules
- Define working days and hours
- Adjust daily appointment slots
- Approve, reschedule, or cancel appointments
- Perform manual patient check-in
- Confirm payments
- Send notifications
- View appointment history
- Manage schedule blocks (vacations, events)

### ❌ Restricted Actions

- Register medical records
- Issue medical documents
- Modify clinical data
- Access full medical records
- View sensitive clinical content
- Modify global financial policies

### 🔗 Accessible Entities

- MedicalSchedule
- DailySchedule
- Appointment
- Payment
- Notification
- ScheduleBlock

---

## 🧑‍💻 Clinic Administrator

> **Strategic and managerial role.**

### 🎯 Role Objective

Configure, maintain, and oversee clinic operations.

### ✅ Allowed Actions

- Manage users (doctors and secretaries)
- Configure procedures
- Define care policies
- Configure insurance providers
- Define appointment limits by care type
- Access financial reports
- Audit issued documents
- Activate or deactivate professionals
- Configure AI features

### ❌ Restricted Actions

- Modify medical records
- Issue prescriptions or medical reports
- Provide patient care
- Access clinical data without justification

### 🔗 Accessible Entities

- Clinic
- User
- Procedure
- CarePolicy
- Insurance
- Reports

---

## 🔐 Permission Matrix (Summary)

| Action                      | Patient | Doctor | Secretary | Admin |
| --------------------------- | ------- | ------ | --------- | ----- |
| Schedule appointment        | ✅      | ❌     | ✅        | ✅    |
| Approve appointment         | ❌      | ❌     | ✅        | ✅    |
| Provide care                | ❌      | ✅     | ❌        | ❌    |
| Register medical record     | ❌      | ✅     | ❌        | ❌    |
| Issue reports/prescriptions | ❌      | ✅     | ❌        | ❌    |
| Create schedules            | ❌      | ❌     | ✅        | ✅    |
| Define insurance limits     | ❌      | ❌     | ❌        | ✅    |
| View financial reports      | ❌      | ❌     | ❌        | ✅    |

---
