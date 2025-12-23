# 📚 Medora — Project Documentation

This directory contains the complete technical documentation for the **Medora** healthcare platform.

The documentation follows a **documentation-first**, **domain-driven** and **production-oriented** approach.  
Each folder represents a specific concern of the system, making the project easier to understand, maintain and evolve.

---

## 📂 Documentation Structure

```
docs/
├── deliverables
├── domain-summary
├── entities
├── roles-and-permissions
├── ui-screens
└── use-cases
```

---

## 🧱 domain-summary

**Purpose**  
Provide a high-level overview of the system domain and its boundaries.

**What you will find**

- Global domain description
- Core concepts and responsibilities
- How major parts of the system relate to each other

**When to read**

- First contact with the project
- Architectural and academic review

---

## 🧩 entities

**Purpose**  
Define the complete data model of the system.

**What you will find**

- All system entities
- Entity attributes and constraints
- Relationships and cardinality
- Explanations focused on real-world healthcare scenarios

**Important**

- Framework-agnostic
- Designed before Django models
- Optimized for scalability and data integrity

---

## 👥 roles-and-permissions

**Purpose**  
Describe how access control works across the system.

**What you will find**

- User roles (Patient, Doctor, Secretary, Admin)
- RBAC rules (Role-Based Access Control)
- What each role can and cannot do
- Permission matrices and explanations

**Why it matters**
Healthcare systems require strict permission control and auditability.

---

## 📋 use-cases

**Purpose**  
Explain system behavior from a functional point of view.

**What you will find**

- Use cases organized by user profile
- Main flows and alternative flows
- Business rules and critical scenarios
- Payment, refund and cancellation logic

**Audience**

- Developers
- Professors
- Product-oriented reviewers

---

## 🎨 ui-screens

**Purpose**  
Organize and track frontend screens.

**What you will find**

- Screen lists per user role
- Screen maps and navigation structure
- UI checklists for implementation tracking

**Example**

```
docs/ui-screens/ui_screens_checklist.md
```

---

## 🗺️ deliverables

**Purpose**  
Guide the incremental development of the system.

**What you will find**

- Sprint-based roadmap
- Backend and frontend responsibilities per stage
- Clear stopping points for presentations and evaluations

**Why it exists**
To ensure the project can be built and demonstrated incrementally.

---

## 🧠 Documentation Principles

- Documentation-first
- Domain before framework
- Real-world healthcare modeling
- Clear separation of concerns
- Production-oriented thinking

---

## ✅ How to Navigate

1. Start with **domain-summary**
2. Review **entities** to understand the data model
3. Check **roles-and-permissions** for access control
4. Read **use-cases** for system behavior
5. Use **ui-screens** to guide frontend implementation
6. Follow **deliverables** to plan development
