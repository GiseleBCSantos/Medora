# Medora — Entities (Database-Centric)

Este documento descreve o **modelo de domínio central do banco de dados** do Medora.
É **agnóstico em relação à tecnologia**, focado apenas em entidades, atributos e relacionamentos,
e serve como base para o posterior mapeamento ORM no Django.

---

## 1. User

### Description

Representa a identidade e autenticação do sistema. Um usuário pode atuar como paciente, médico,
secretário ou administrador.

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

User é a identidade raiz. Papéis específicos do domínio (Patient, Doctor) estendem User
sem acoplar autenticação aos dados de saúde.

---

## 2. Clinic

### Description

Representa uma organização ou unidade de saúde.

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

Clinic é o limite multi-inquilino e responsável pelas regras operacionais.

---

## 3. Doctor

### Description

Representa um profissional clínico que presta serviços de saúde.

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

Representa uma pessoa que recebe serviços de saúde.

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

Define um serviço de saúde que pode ser agendado.

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

Define regras recorrentes de disponibilidade semanal.

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

Representa a disponibilidade real para uma data específica.

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

Representa indisponibilidade temporária (férias, eventos).

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

Representa uma instância de serviço de saúde agendada.

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

Documentação clínica do appointment.

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

Documentos gerados clinicamente ou administrativamente.

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

Representa uma transação financeira.

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

Representa uma operadora de plano de saúde.

### Attributes

- id (PK)
- name
- code
- active

---

## 14. CarePolicy

### Description

Define limites e cotas por tipo de atendimento.

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

Alertas de usuário gerados pelo sistema.

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

Comunicação direta entre usuários.

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

Feedback do paciente após a conclusão do appointment.

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

Representa um processo de reembolso.

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

Registro de auditoria para alterações manuais de agenda.

### Attributes

- id (PK)
- daily_schedule_id (FK DailySchedule)
- slots_before
- slots_after
- performed_by_user_id (FK User)
- reason
- created_at
