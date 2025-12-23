# 🗺️ Development Roadmap — HealthSync

This roadmap organizes the project into incremental sprints, each one delivering a coherent and demonstrable set of features.  
Each sprint can be treated as an independent milestone or sprint backlog.

---

## 🟢 Sprint 1 — System Foundation

### 🎯 Sprint Goal

Bring the system to life with authentication, core infrastructure and base domain.

### 🔧 Backend — Sprint Backlog

- [ ] Django + Django REST Framework setup
- [ ] Docker & Docker Compose configuration
- [ ] PostgreSQL database integration
- [ ] JWT authentication
- [ ] User model with roles
- [ ] Clinic CRUD
- [ ] Basic RBAC permissions by user type

### 🎨 Frontend — Sprint Backlog

- [ ] React (Vite or Next.js) setup
- [ ] Tailwind CSS configuration
- [ ] Base layout (header, navigation, footer)
- [ ] Login / Logout flow
- [ ] Route protection by role

### 📄 Deliverable

- ✔ Authentication working
- ✔ Users can log in with roles
- ✔ Clinics can be created
- ✔ Secure API + protected UI

📌 **Strong foundation checkpoint**

---

## 🟢 Sprint 2 — Clinical Core Domain

### 🎯 Sprint Goal

Model the real-world clinical structure.

### 🔧 Backend — Sprint Backlog

- [ ] Doctor CRUD
- [ ] Patient CRUD
- [ ] Procedure CRUD
- [ ] Clinic relationships
- [ ] Permissions:
  - Admin / Secretary manage
  - Patient read-only

### 🎨 Frontend — Sprint Backlog

- [ ] Doctor registration screen
- [ ] Patient registration screen
- [ ] Procedure listing
- [ ] Validated forms

### 📄 Deliverable

- ✔ Core healthcare entities fully modeled
- ✔ Data visible and manageable in UI

---

## 🟢 Sprint 3 — Medical Schedule (Weekly Rules)

### 🎯 Sprint Goal

Define when doctors are available.

### 🔧 Backend — Sprint Backlog

- [ ] AgendaMedica CRUD
- [ ] BloqueioAgenda CRUD
- [ ] Business rules:
  - Valid weekdays
  - Valid time ranges

### 🎨 Frontend — Sprint Backlog

- [ ] Weekly schedule configuration screen
- [ ] Agenda block management

### 📄 Deliverable

- ✔ Weekly schedules configured
- ✔ Exceptions applied correctly

📌 **High-value domain feature**

---

## 🟡 Sprint 4 — Daily Agenda & Capacity Control

### 🎯 Sprint Goal

Turn rules into real, daily schedules.

### 🔧 Backend — Sprint Backlog

- [ ] AgendaDia CRUD
- [ ] Automatic generation from AgendaMedica
- [ ] Daily slot capacity adjustment
- [ ] Adjustment audit log (AjusteAgendaLog)

### 🎨 Frontend — Sprint Backlog

- [ ] Daily agenda visualization
- [ ] Manual capacity adjustment
- [ ] Conflict warnings

### 📄 Deliverable

- ✔ Real daily agenda
- ✔ Capacity safely controlled

---

## 🟡 Sprint 5 — Appointment Flow

### 🎯 Sprint Goal

Allow patients to request appointments.

### 🔧 Backend — Sprint Backlog

- [ ] Appointment CRUD
- [ ] Availability validation
- [ ] Limits by appointment type
- [ ] Appointment status lifecycle

### 🎨 Frontend — Sprint Backlog

- [ ] Doctor catalog
- [ ] Date & time selection
- [ ] Appointment request flow

### 📄 Deliverable

- ✔ Appointment requests working
- ✔ Status visible to all roles

---

## 🟠 Sprint 6 — Approval & Critical Rules

### 🎯 Sprint Goal

Enable real administrative control.

### 🔧 Backend — Sprint Backlog

- [ ] Approve / reject appointments
- [ ] Automatic refund record creation
- [ ] Internal notifications

### 🎨 Frontend — Sprint Backlog

- [ ] Secretary dashboard
- [ ] Approve / reject actions
- [ ] Patient feedback messages

### 📄 Deliverable

- ✔ Full administrative workflow
- ✔ Refund logic modeled

📌 **Perfect demo milestone**

---

## 🟠 Sprint 7 — Payments (PIX)

### 🎯 Sprint Goal

Introduce financial traceability.

### 🔧 Backend — Sprint Backlog

- [ ] Payment entity
- [ ] PIX integration (or mock)
- [ ] Webhook simulation
- [ ] Refund automation

### 🎨 Frontend — Sprint Backlog

- [ ] Payment screen
- [ ] PIX QR Code display
- [ ] Payment status updates

### 📄 Deliverable

- ✔ Payments traceable
- ✔ Refunds consistent

---

## 🔵 Sprint 8 — Check-in & Appointment Day Flow

### 🎯 Sprint Goal

Support the consultation day workflow.

### 🔧 Backend — Sprint Backlog

- [ ] QR Code check-in
- [ ] Time validation rules
- [ ] Appointment status transitions

### 🎨 Frontend — Sprint Backlog

- [ ] Check-in screen
- [ ] QR code scanner
- [ ] Status visualization

### 📄 Deliverable

- ✔ Check-in working

---

## 🔵 Sprint 9 — Medical Records & Documents

### 🎯 Sprint Goal

Deliver real clinical value.

### 🔧 Backend — Sprint Backlog

- [ ] Medical record CRUD
- [ ] Medical documents CRUD
- [ ] PDF generation
- [ ] Access control enforcement

### 🎨 Frontend — Sprint Backlog

- [ ] Doctor medical record screen
- [ ] Patient document download

### 📄 Deliverable

- ✔ Consultations documented
- ✔ Legal medical documents generated

---

## 🔵 Sprint 10 — Teleconsultation & Advanced Features

### 🎯 Sprint Goal

Showcase advanced capabilities.

### 🔧 Backend — Sprint Backlog

- [ ] Teleconsultation room creation
- [ ] Access tokens
- [ ] Session logs

### 🎨 Frontend — Sprint Backlog

- [ ] Video consultation screen
- [ ] Online appointment access

### 📄 Deliverable

- ✔ Teleconsultation implemented or documented

📌 **Excellent project closure**

---

## 🧠 Strategic Note

If scope or time becomes constrained:
👉 Stop at **Sprint 6**  
👉 Everything after becomes **future work**

This still delivers a complete, impressive healthcare platform.
