# Medora — Domain Summary (Database-Centric)

This document describes the **core database domain model** of Medora.
It is **technology-agnostic**, focused purely on entities, attributes, and relationships,
and serves as the foundation for later Django ORM modeling.

---

## 1. User

### Description

Represents system identity and authentication. A user may act as a patient, doctor,
secretary, or administrator.

### Attributes

- id (PK)
- name
- email (UNIQUE)
- password_hash
- type (PATIENT | DOCTOR | ADMIN | SECRETARY)
- phone
- active
- created_at
- updated_at

### Relationships

- User → Patient (0..1)
- User → Doctor (0..1)
- User → Appointment (0..N, created_by)
- User → Document (0..N, generated_by)
- User → Notification (0..N)
- User → Message (0..N, sender/receiver)

### Relationship Explanation

User is the root identity. Domain-specific roles (Patient, Doctor) extend User
without coupling authentication to healthcare data.

---

## 2. Clinic

### Description

Represents a healthcare organization or unit.

### Attributes

- id (PK)
- name
- cnpj
- address
- phone
- email
- active
- created_at

### Relationships

- Clinic → Doctor (1..N)
- Clinic → User (1..N, admin/secretary)
- Clinic → Procedure (1..N)
- Clinic → CarePolicy (1..N)
- Clinic → Schedule (1..N)

### Relationship Explanation

Clinic is the multi-tenant boundary and owner of operational rules.

---

## 3. Doctor

### Description

Represents a clinical professional who provides healthcare services.

### Attributes

- id (PK)
- user_id (FK User, optional)
- clinic_id (FK Clinic)
- public_name
- specialty
- professional_registry
- registry_state
- biography
- attends_online
- attends_presential
- active
- created_at

### Relationships

- Doctor → MedicalSchedule (1..N)
- Doctor → DailySchedule (1..N)
- Doctor → Procedure (1..N)
- Doctor → Appointment (1..N)
- Doctor → MedicalRecord (1..N)
- Doctor → Review (1..N)

---

## 4. Patient

### Description

Represents a person receiving healthcare services.

### Attributes

- id (PK)
- user_id (FK User)
- cpf
- birth_date
- gender
- emergency_phone
- allergies
- chronic_conditions
- notes
- created_at

### Relationships

- Patient → Appointment (1..N)
- Patient → MedicalRecord (1..N)
- Patient → Review (1..N)

---

## 5. Procedure

### Description

Defines a healthcare service that can be scheduled.

### Attributes

- id (PK)
- clinic_id (FK Clinic)
- doctor_id (FK Doctor)
- name
- description
- type (CONSULTATION | EXAM | FOLLOW_UP | THERAPY)
- duration_minutes
- modality (ONLINE | PRESENTIAL)
- price
- requires_confirmation
- active

### Relationships

- Procedure → Appointment (1..N)
- Procedure → CarePolicy (1..N)

---

## 6. MedicalSchedule

### Description

Defines recurring weekly availability rules.

### Attributes

- id (PK)
- doctor_id (FK Doctor)
- clinic_id (FK Clinic)
- weekday (0–6)
- start_time
- end_time
- slot_duration_minutes
- max_patients_per_slot
- active

### Relationships

- MedicalSchedule → DailySchedule (1..N)

---

## 7. DailySchedule

### Description

Represents real availability for a specific date.

### Attributes

- id (PK)
- doctor_id (FK Doctor)
- clinic_id (FK Clinic)
- date
- total_slots
- booked_slots
- status (OPEN | CLOSED | BLOCKED)

### Relationships

- DailySchedule → Appointment (1..N)

---

## 8. ScheduleBlock

### Description

Represents temporary unavailability (vacations, events).

### Attributes

- id (PK)
- doctor_id (FK Doctor)
- clinic_id (FK Clinic)
- start_date
- end_date
- reason

---

## 9. Appointment

### Description

Represents a scheduled healthcare service instance.

### Attributes

- id (PK)
- patient_id (FK Patient)
- doctor_id (FK Doctor)
- clinic_id (FK Clinic)
- procedure_id (FK Procedure)
- daily_schedule_id (FK DailySchedule)
- created_by_user_id (FK User)
- care_type (PRIVATE | INSURANCE | FREE)
- insurance_id (FK Insurance, optional)
- start_datetime
- end_datetime
- status
- checkins_count
- created_at

### Relationships

- Appointment → MedicalRecord (1..1)
- Appointment → Document (1..N)
- Appointment → Payment (0..1)
- Appointment → Review (0..1)

---

## 10. MedicalRecord

### Description

Clinical documentation of the appointment.

### Attributes

- id (PK)
- appointment_id (FK Appointment)
- doctor_id (FK Doctor)
- patient_id (FK Patient)
- evolution
- diagnosis
- conduct
- ai_assisted
- created_at

---

## 11. Document

### Description

Clinical or administrative generated documents.

### Attributes

- id (PK)
- appointment_id (FK Appointment)
- type (PRESCRIPTION | REPORT | CERTIFICATE | DECLARATION)
- generated_by_user_id (FK User)
- pdf_url
- validation_code
- created_at

---

## 12. Payment

### Description

Represents a financial transaction.

### Attributes

- id (PK)
- appointment_id (FK Appointment)
- amount
- method (PIX)
- status (PENDING | CONFIRMED | FAILED)
- transaction_id
- created_at

---

## 13. Insurance

### Description

Represents a healthcare insurance provider.

### Attributes

- id (PK)
- name
- code
- active

---

## 14. CarePolicy

### Description

Defines limits and quotas by care type.

### Attributes

- id (PK)
- clinic_id (FK Clinic)
- doctor_id (FK Doctor, optional)
- procedure_id (FK Procedure, optional)
- care_type (PRIVATE | INSURANCE | FREE)
- daily_limit
- weekly_limit
- monthly_limit
- max_schedule_percentage
- active

---

## 15. Notification

### Description

System-generated user alerts.

### Attributes

- id (PK)
- user_id (FK User)
- type
- message
- read
- created_at

---

## 16. Message

### Description

Direct communication between users.

### Attributes

- id (PK)
- appointment_id (FK Appointment)
- sender_id (FK User)
- receiver_id (FK User)
- title
- content
- created_at

---

## 17. Review

### Description

Patient feedback after appointment completion.

### Attributes

- id (PK)
- appointment_id (FK Appointment)
- patient_id (FK Patient)
- doctor_id (FK Doctor)
- rating
- comment
- created_at

---

## 18. Refund

### Description

Represents a refund process.

### Attributes

- id (PK)
- payment_id (FK Payment)
- amount
- reason
- status (REQUESTED | PROCESSING | COMPLETED | FAILED)
- created_by_user_id (FK User)
- created_at

---

## 19. ScheduleAdjustmentLog

### Description

Audit log for manual schedule changes.

### Attributes

- id (PK)
- daily_schedule_id (FK DailySchedule)
- slots_before
- slots_after
- performed_by_user_id (FK User)
- reason
- created_at
