# 📌 Use Cases — Medora

_(Organized by User Role)_

This document describes the main use cases of the Medora platform,
organized by user profile and aligned with the RBAC model.

---

## 👤 Patient — Use Cases

### UC-01 — Create Patient Account

**Actor:** Patient

**Description:**  
Allows a new patient to create an account in the system.

**Main Flow:**

1. Patient provides name, email, password, and CPF
2. System validates data
3. System creates a User with role PATIENT
4. System creates a Patient profile linked to the User

**Business Rules:**

- CPF and email must be unique
- Account starts as active

---

### UC-02 — Search Professional or Clinic

**Actor:** Patient

**Description:**  
Allows searching for available professionals or clinics.

**Filters:**

- Specialty
- Modality (in-person / teleconsultation)
- Accepted insurance
- Price
- Available days

---

### UC-03 — Request Appointment

**Actor:** Patient

**Description:**  
Requests a consultation or procedure.

**Main Flow:**

1. Selects professional or procedure
2. Chooses available date and time
3. Selects care type (PRIVATE / INSURANCE)
4. System validates care policy limits
5. System creates appointment with status PENDING

**Alternative Flow:**

- If insurance limit is exceeded → request is blocked

---

### UC-04 — Make Payment

**Actor:** Patient

**Description:**  
Performs payment via PIX.

**Postcondition:**

- Appointment status updated to PAID

---

### UC-05 — Perform Check-in

**Actor:** Patient

**Description:**  
Confirms presence using QR Code.

---

### UC-06 — Join Teleconsultation

**Actor:** Patient

**Precondition:**  
Appointment confirmed

**Description:**  
Joins the virtual consultation room at the scheduled time.

---

### UC-07 — View Medical Documents

**Actor:** Patient

**Description:**  
Downloads prescriptions, reports, and certificates issued for their appointments.

---

### UC-08 — Review Appointment

**Actor:** Patient

**Precondition:**  
Appointment finalized

**Description:**  
Rates and reviews the professional and clinic.

---

## 🧑‍⚕️ Doctor — Use Cases

### UC-09 — View Daily Schedule

**Actor:** Doctor

**Description:**  
Views daily appointments organized by time.

---

### UC-10 — Start Appointment

**Actor:** Doctor

**Description:**  
Starts in-person or teleconsultation appointment.

---

### UC-11 — Register Medical Record

**Actor:** Doctor

**Description:**  
Registers clinical evolution, diagnosis, and conduct.

**Optional AI Flow:**

- System suggests summary or ICD-10 code

---

### UC-12 — Issue Medical Document

**Actor:** Doctor

**Description:**  
Issues:

- Prescription
- Medical report
- Certificate
- Declaration

**Postcondition:**

- PDF generated with validation QR Code

---

### UC-13 — Close Appointment

**Actor:** Doctor

**Description:**  
Finalizes appointment and releases documents to the patient.

---

### UC-14 — View Reviews

**Actor:** Doctor

**Description:**  
Views feedback received from patients.

---

## 🧑‍💼 Secretary — Use Cases

### UC-15 — Create Medical Schedule

**Actor:** Secretary

**Description:**  
Defines weekly working days and hours for a doctor.

---

### UC-16 — Generate Daily Schedule

**Actor:** System (triggered by Secretary)

**Description:**  
Automatically generates daily schedule based on weekly rules.

---

### UC-17 — Approve or Reject Appointment

**Actor:** Secretary  
**Secondary Actor:** Payment System

**Description:**  
Approves or rejects appointment requests, handling payments if needed.

**Main Flow (Approval):**

1. Secretary reviews pending appointment
2. System validates availability
3. Appointment status set to CONFIRMED
4. Patient is notified

**Alternative Flow A — Rejection without payment:**

- Status set to REJECTED
- Patient notified

**Alternative Flow B — Rejection with payment:**

- Appointment set to REJECTED
- Refund record created
- Refund process started
- Patient notified

**Business Rules:**

- All payments must remain traceable
- Refunds do not delete financial records

---

### UC-18 — Adjust Daily Slots

**Actor:** Secretary

**Description:**  
Adjusts the number of available slots for a specific day.

**Main Flow:**

1. Secretary updates slot limit
2. System validates existing appointments
3. New configuration is saved
4. Audit log is created

**Alternative Flow:**

- If new limit < confirmed appointments:
  - System blocks change
  - Secretary must reschedule or cancel appointments
  - Paid cancellations trigger refunds

---

### UC-19 — Confirm Payment

**Actor:** Secretary

**Description:**  
Manually confirms a payment in exceptional cases.

---

### UC-20 — Perform Manual Check-in

**Actor:** Secretary

**Description:**  
Registers patient presence manually.

---

### UC-21 — Block Schedule

**Actor:** Secretary

**Description:**  
Blocks schedule dates due to vacation or unavailability.

---

## 🧑‍💻 Administrator — Use Cases

### UC-22 — Manage Users

**Actor:** Admin

**Description:**  
Creates, edits, and deactivates users.

---

### UC-23 — Configure Procedures

**Actor:** Admin

**Description:**  
Defines procedure price, duration, and modality.

---

### UC-24 — Configure Insurance Providers

**Actor:** Admin

**Description:**  
Registers accepted insurance providers.

---

### UC-25 — Define Care Policies

**Actor:** Admin

**Description:**  
Defines appointment limits by care type:

- Private
- Insurance
- Free

---

### UC-26 — View Reports

**Actor:** Admin

**Description:**  
Accesses:

- Financial reports
- Schedule occupancy
- Appointments by care type

---
