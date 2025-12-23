# 🎨 UI Screens by Role — Medora

This document describes the application screens organized by **user role**.
It serves as a reference for **frontend development, UX design, and feature validation**.

---

## 👤 Patient Screens

### 🏠 Home / Professional Catalog

**Goal:** Service discovery

**Components:**

- Search by specialty
- Filters:
  - City / Teleconsultation
  - Accepted insurance
  - Price
  - Availability
- List of professionals and clinics

---

### 👨‍⚕️ Professional Profile Page

**Components:**

- Doctor information
- Specialty
- Ratings and reviews
- Offered procedures
- **Schedule Appointment** button

---

### 📅 Appointment Scheduling

**Components:**

- Calendar with available time slots
- Selection options:
  - Care type (PRIVATE / INSURANCE)
  - Modality (ONLINE / PRESENTIAL)
- Document upload (if required)

---

### 💳 Payment Screen

**Components:**

- PIX QR Code
- Payment status
- Instructions and expiration time

---

### 📋 My Appointments

**Description:**  
List of appointments grouped by status.

**Statuses:**

- Pending
- Confirmed
- Paid
- Completed

**Actions:**

- Cancel
- Reschedule
- Perform check-in
- Join teleconsultation

---

### 📲 Check-in

**Components:**

- Appointment QR Code
- Presence status confirmation

---

### 💬 Appointment Chat

**Description:**  
Messaging related to a specific appointment.

**Features:**

- Send pre-appointment questions
- Receive documents and instructions

---

### 📄 Documents & Reports

**Components:**

- Chronological list of documents
- PDF download
- QR Code validation

---

### ⭐ Appointment Review

**Components:**

- Rating (stars)
- Written feedback

---

## 🧑‍⚕️ Doctor / Healthcare Professional Screens

### 🏠 Professional Dashboard

**Overview:**

- Appointments scheduled for the day
- Appointments in progress
- Basic performance indicators

---

### 📅 Daily Agenda

**Components:**

- Patient list
- Time slots
- Status:
  - Waiting
  - In progress
  - Completed

---

### 🩺 Appointment Screen

**Components:**

- Patient basic data
- Clinical history summary
- **Start Appointment** action

---

### 📘 Digital Medical Record

**Components:**

- Clinical evolution
- Diagnosis
- Conduct
- Exam uploads
- AI suggestions (optional)

---

### 📄 Medical Document Issuance

**Components:**

- Document type selection:
  - Prescription
  - Medical report
  - Certificate
- PDF preview
- Digital signature

---

### 📹 Teleconsultation

**Components:**

- Video call
- Chat
- Appointment closing action

---

### ⭐ Received Reviews

**Components:**

- List of patient feedback
- Average rating

---

## 🧑‍💼 Secretary / Attendant Screens

### 🏠 Operational Dashboard

**Overview:**

- Daily agenda summary
- Pending approvals
- Payments
- Critical alerts

---

### 🗓️ Medical Schedule Management

**Components:**

- Weekly configuration
- Working days
- Time ranges
- Slot duration

---

### 📆 Daily Agenda Management

**Components:**

- Total slots
- Occupied slots
- Adjust slot limits

---

### 📋 Appointment Management

**Lists:**

- Pending
- Paid
- Confirmed

**Actions:**

- Approve
- Reject
- Reschedule
- Cancel

---

### 💳 Payment Management

**Components:**

- Payment list
- Manual confirmation
- Refund status

---

### ⛔ Schedule Blocks

**Components:**

- Create blocks
- Edit or remove blocks

---

### 🔔 Notifications

**Components:**

- Send notifications to patients

---

## 🧑‍💻 Administrator Screens

### 🏠 Administrative Dashboard

**Indicators:**

- Revenue
- Schedule occupancy
- Appointments by care type

---

### 👥 User Management

**Actions:**

- Create doctors
- Create secretaries
- Activate / deactivate users

---

### 🏥 Clinic Management

**Components:**

- Clinic data
- General configurations

---

### 🩺 Procedure Management

**Components:**

- Create / edit procedures
- Pricing
- Modality

---

### 💼 Insurance Management

**Components:**

- Insurance registration
- Acceptance rules

---

### 📊 Care Policies

**Components:**

- Limits by care type:
  - Private
  - Insurance
- Maximum percentages
- Scope by doctor or procedure

---

### 📈 Reports

**Types:**

- Financial
- Schedule utilization
- Appointments
- Refunds

---

## 🧭 Screen Map (High-Level)

### Patient

- Home
- Professional Profile
- Appointment
- Payment
- Check-in
- Teleconsultation
- Documents
- Review

### Doctor

- Dashboard
- Daily Agenda
- Appointment
- Medical Record
- Documents
- Reviews

### Secretary

- Dashboard
- Medical Schedule
- Daily Agenda
- Appointments
- Payments
- Schedule Blocks

### Admin

- Dashboard
- Users
- Clinic
- Procedures
- Insurance
- Care Policies
- Reports
