# Medora — Resumo de Domínio por App

Este documento organiza o domínio do banco de dados do Medora por módulos lógicos de aplicação (apps).
Foca exclusivamente em **entities e relationships**, sem preocupações de implementação ou ORM.

---

## 📦 accounts app

### 🔐 User

**Descrição**  
Representa a identidade e camada de autenticação do sistema.  
Gerencia login, permissões e papéis de usuário.

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

**Por que este app existe**

- Mantém a autenticação isolada da lógica do domínio de saúde
- Permite usuários não médicos (secretária, admin)
- Centraliza controle de acesso e auditoria

---

## 📦 clinics app

### 🏥 Clinic

### 📊 CarePolicy

**Descrição**  
Representa organizações de saúde e suas regras operacionais.

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

**Por que este app existe**

- Define o limite multi-clínica (multi-inquilino)
- Centraliza políticas institucionais e financeiras
- Permite regras diferentes por clínica

---

## 📦 professionals app

### 🧑‍⚕️ Doctor

**Descrição**  
Representa um profissional de saúde responsável por serviços clínicos.

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

**Por que este app existe**

- Separa responsabilidade clínica das operações
- Permite que secretárias gerenciem agendas de médicos
- Suporta médicos sem acesso direto ao sistema

---

## 📦 patients app

### 🧑 Patient

**Descrição**  
Representa uma pessoa que recebe serviços de saúde.

**Entities**

- Patient

**Relationships**

- Patient → User (1..1)
- Patient → Appointment (1..N)
- Patient → MedicalRecord (1..N)
- Patient → Review (1..N)

**Por que este app existe**

- Isole dados pessoais e médicos
- Facilita requisitos de privacidade e conformidade

---

## 📦 scheduling app

### 🗓️ MedicalSchedule

### 📆 DailySchedule

### ⛔ ScheduleBlock

### 📅 Appointment

**Descrição**  
Gerencia regras de disponibilidade, exceções e ciclo de vida de appointments.

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

**Por que este app existe**

- Domínio de alta concorrência
- Requer integridade transacional
- Centraliza lógica de agendamento

---

## 📦 clinical app

### 🩺 MedicalRecord

### 📎 Document

**Descrição**  
Armazena dados clínicos e documentos médicos gerados.

**Entities**

- MedicalRecord
- Document

**Relationships**

- MedicalRecord → Appointment (1..1)
- MedicalRecord → Patient (N..1)
- MedicalRecord → Doctor (N..1)
- Document → Appointment (N..1)
- Document → User (generated_by)

**Por que este app existe**

- Separa dados clínicos da lógica operacional
- Facilita auditoria e armazenamento seguro

---

## 📦 billing app

### 💰 Payment

### 💸 Refund

### 🏥 Insurance

**Descrição**  
Gerencia transações financeiras e dados de convênios.

**Entities**

- Payment
- Refund
- Insurance

**Relationships**

- Payment → Appointment (1..1)
- Refund → Payment (1..1)
- Appointment → Insurance (0..1)

**Por que este app existe**

- Fluxos financeiros são assíncronos e sensíveis
- Permite evolução independente da lógica de cobrança

---

## 📦 communication app

### 💬 Message

### ⭐ Review

**Descrição**  
Gerencia comunicação entre usuários e feedbacks.

**Entities**

- Message
- Review

**Relationships**

- Message → Appointment (N..1)
- Message → User (sender / receiver)
- Review → Appointment (1..1)
- Review → Patient (N..1)
- Review → Doctor (N..1)

**Por que este app existe**

- Funcionalidades não críticas, mas voltadas ao usuário
- Fácil de escalar e modificar independentemente

---

## 📦 notifications app

### 🔔 Notification

**Descrição**  
Representa alertas gerados pelo sistema.

**Entities**

- Notification

**Relationships**

- Notification → User (N..1)

**Por que este app existe**

- Suporta notificações assíncronas e multicanal
- Desacopla mensagens dos fluxos principais

---

## 📦 audit app

### 🔄 ScheduleAdjustmentLog

**Descrição**  
Rastreia alterações manuais na disponibilidade diária.

**Entities**

- ScheduleAdjustmentLog

**Relationships**

- ScheduleAdjustmentLog → DailySchedule (N..1)
- ScheduleAdjustmentLog → User (performed_by)

**Por que este app existe**

- Garante rastreabilidade e responsabilidade
- Necessário para conformidade e auditoria
