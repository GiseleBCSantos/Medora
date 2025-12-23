# Medora — Domain Summary by App

This document organizes the Medora database domain by logical application modules (apps).
It focuses exclusively on **entities and relationships**, without implementation or ORM concerns.

---

## 📦 accounts app

### 🔐 User

**Description**  
Represents the system identity and authentication layer.  
Handles login, permissions, and user roles.

**Entities**

- User

**Relationships**

- User → Patient (0..1)
- User → Doctor (0..1)
- User → Appointment (0..N, created_by)
- User → Document (0..N, generated_by)
- User → Notification (0..N)
- User → Message (0..N, sender / receiver)
- User → Refund (0..N, created_by)
- User → ScheduleAdjustmentLog (0..N, performed_by)

**Why this app exists**

- Keeps authentication isolated from healthcare domain logic
- Allows non-medical users (secretary, admin)
- Centralizes access control and auditing

---

## 📦 clinics app

### 🏥 Clinic

### 📊 CarePolicy

**Description**  
Represents healthcare organizations and their operational rules.

**Entities**

- Clinic
- CarePolicy

**Relationships**

- Clinic → Doctor (1..N)
- Clinic → User (1..N, ADMIN / SECRETARY)
- Clinic → Procedure (1..N)
- Clinic → CarePolicy (1..N)
- Clinic → MedicalSchedule (1..N)
- Clinic → DailySchedule (1..N)
- Clinic → ScheduleBlock (1..N)

**Why this app exists**

- Defines the multi-clinic (multi-tenant) boundary
- Centralizes institutional and financial policies
- Allows different rules per clinic

---

## 📦 professionals app

### 🧑‍⚕️ Doctor

**Description**  
Represents a healthcare professional responsible for clinical services.

**Entities**

- Doctor

**Relationships**

- Doctor → Clinic (N..1)
- Doctor → MedicalSchedule (1..N)
- Doctor → DailySchedule (1..N)
- Doctor → Procedure (1..N)
- Doctor → Appointment (1..N)
- Doctor → MedicalRecord (1..N)
- Doctor → Review (1..N)

**Why this app exists**

- Separates clinical responsibility from operations
- Allows secretaries to manage doctor schedules
- Supports doctors without direct system access

---

## 📦 patients app

### 🧑 Patient

**Description**  
Represents a person receiving healthcare services.

**Entities**

- Patient

**Relationships**

- Patient → User (1..1)
- Patient → Appointment (1..N)
- Patient → MedicalRecord (1..N)
- Patient → Review (1..N)

**Why this app exists**

- Isolates personal and medical data
- Facilitates privacy and compliance requirements

---

## 📦 scheduling app

### 🗓️ MedicalSchedule

### 📆 DailySchedule

### ⛔ ScheduleBlock

### 📅 Appointment

**Description**  
Handles availability rules, exceptions, and appointment lifecycle.

**Entities**

- MedicalSchedule
- DailySchedule
- ScheduleBlock
- Appointment

**Relationships**

- MedicalSchedule → DailySchedule (1..N)
- DailySchedule → Appointment (1..N)
- Appointment → Patient (N..1)
- Appointment → Doctor (N..1)
- Appointment → Clinic (N..1)
- Appointment → Procedure (N..1)

**Why this app exists**

- High-concurrency domain
- Requires transactional integrity
- Centralizes scheduling logic

---

## 📦 clinical app

### 🩺 MedicalRecord

### 📎 Document

**Description**  
Stores clinical data and generated medical documents.

**Entities**

- MedicalRecord
- Document

**Relationships**

- MedicalRecord → Appointment (1..1)
- MedicalRecord → Patient (N..1)
- MedicalRecord → Doctor (N..1)
- Document → Appointment (N..1)
- Document → User (generated_by)

**Why this app exists**

- Separates clinical data from operational logic
- Facilitates auditing and secure storage

---

## 📦 billing app

### 💰 Payment

### 💸 Refund

### 🏥 Insurance

**Description**  
Handles financial transactions and insurance data.

**Entities**

- Payment
- Refund
- Insurance

**Relationships**

- Payment → Appointment (1..1)
- Refund → Payment (1..1)
- Appointment → Insurance (0..1)

**Why this app exists**

- Financial workflows are asynchronous and sensitive
- Allows independent evolution of billing logic

---

## 📦 communication app

### 💬 Message

### ⭐ Review

**Description**  
Manages user communication and feedback.

**Entities**

- Message
- Review

**Relationships**

- Message → Appointment (N..1)
- Message → User (sender / receiver)
- Review → Appointment (1..1)
- Review → Patient (N..1)
- Review → Doctor (N..1)

**Why this app exists**

- Non-critical but user-facing features
- Easy to scale and modify independently

---

## 📦 notifications app

### 🔔 Notification

**Description**  
Represents system-generated alerts.

**Entities**

- Notification

**Relationships**

- Notification → User (N..1)

**Why this app exists**

- Supports async and multi-channel notifications
- Decouples messaging from core workflows

---

## 📦 audit app

### 🔄 ScheduleAdjustmentLog

**Description**  
Tracks manual changes to daily availability.

**Entities**

- ScheduleAdjustmentLog

**Relationships**

- ScheduleAdjustmentLog → DailySchedule (N..1)
- ScheduleAdjustmentLog → User (performed_by)

**Why this app exists**

- Ensures traceability and accountability
- Required for compliance and auditing
