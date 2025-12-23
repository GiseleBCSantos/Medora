# 👥 Funções e Permissões de Usuário — Medora

Medora adota um modelo de **Controle de Acesso Baseado em Funções (RBAC)**, onde cada usuário tem permissões estritamente alinhadas com suas responsabilidades dentro do ecossistema clínico.

Este documento descreve **o que cada função de usuário pode e não pode fazer**, bem como quais **entidades de domínio** cada função pode acessar.

---

## 🧑‍🦱 Paciente

### 🎯 Objetivo da Função

Consumir serviços de saúde, gerenciar consultas e acessar dados clínicos pessoais.

### ✅ Ações Permitidas

- Criar e gerenciar própria conta
- Pesquisar profissionais e clínicas
- Visualizar horários disponíveis
- Solicitar consultas
- Reagendar ou cancelar consultas (de acordo com a política da clínica)
- Pagar por consultas particulares
- Realizar check-in (QR Code)
- Participar de teleconsultas
- Visualizar e baixar:
  - relatórios médicos
  - prescrições
  - certificados
- Avaliar profissionais e clínicas
- Enviar mensagens relacionadas a uma consulta

### ❌ Ações Restritas

- Criar ou modificar horários médicos
- Acessar registros médicos de outros pacientes
- Alterar preços de consultas
- Emitir documentos médicos
- Acessar dados financeiros da clínica
- Confirmar pagamentos manualmente

### 🔗 Entidades Acessíveis

- Patient
- Appointment
- Document (próprio apenas)
- Payment (próprio apenas)
- Message
- Review

---

## 🧑‍⚕️ Médico / Profissional de Saúde

> **Função estritamente clínica. Sem responsabilidades administrativas.**

### 🎯 Objetivo da Função

Fornecer serviços de saúde, registrar dados clínicos e emitir documentos médicos.

### ✅ Ações Permitidas

- Visualizar agenda pessoal diária
- Iniciar consultas presenciais ou online
- Acessar registros médicos de pacientes atribuídos
- Registrar evolução clínica
- Emitir:
  - prescrições
  - relatórios médicos
  - certificados
- Encerrar consultas
- Visualizar avaliações recebidas
- Usar recursos de IA clínica (se habilitado)

### ❌ Ações Restritas

- Criar ou editar agendas
- Alterar preços de consultas
- Gerenciar planos de seguro
- Definir limites de consultas
- Acessar dados financeiros da clínica
- Aprovar ou rejeitar consultas

### 🔗 Entidades Acessíveis

- Doctor
- Appointment
- MedicalRecord
- Document
- Review

---

## 🧑‍💼 Secretário / Atendente

> **Função operacional dentro da clínica.**

### 🎯 Objetivo da Função

Gerenciar agendas, organizar consultas e mediar a interação paciente–profissional.

### ✅ Ações Permitidas

- Criar e editar agendas médicas
- Definir dias e horários de trabalho
- Ajustar slots de consultas diários
- Aprovar, reagendar ou cancelar consultas
- Realizar check-in manual de pacientes
- Confirmar pagamentos
- Enviar notificações
- Visualizar histórico de consultas
- Gerenciar bloqueios de agenda (férias, eventos)

### ❌ Ações Restritas

- Registrar registros médicos
- Emitir documentos médicos
- Modificar dados clínicos
- Acessar registros médicos completos
- Visualizar conteúdo clínico sensível
- Modificar políticas financeiras globais

### 🔗 Entidades Acessíveis

- MedicalSchedule
- DailySchedule
- Appointment
- Payment
- Notification
- ScheduleBlock

---

## 🧑‍💻 Administrador da Clínica

> **Função estratégica e gerencial.**

### 🎯 Objetivo da Função

Configurar, manter e supervisionar operações da clínica.

### ✅ Ações Permitidas

- Gerenciar usuários (médicos e secretários)
- Configurar procedimentos
- Definir políticas de cuidados
- Configurar provedores de seguro
- Definir limites de consultas por tipo de cuidado
- Acessar relatórios financeiros
- Auditar documentos emitidos
- Ativar ou desativar profissionais
- Configurar recursos de IA

### ❌ Ações Restritas

- Modificar registros médicos
- Emitir prescrições ou relatórios médicos
- Fornecer cuidados ao paciente
- Acessar dados clínicos sem justificativa

### 🔗 Entidades Acessíveis

- Clinic
- User
- Procedure
- CarePolicy
- Insurance
- Reports

---

## 🔐 Matriz de Permissões (Resumo)

| Ação                              | Paciente | Médico | Secretário | Admin |
| --------------------------------- | -------- | ------ | ---------- | ----- |
| Agendar consulta                  | ✅       | ❌     | ✅         | ✅    |
| Aprovar consulta                  | ❌       | ❌     | ✅         | ✅    |
| Fornecer cuidados                 | ❌       | ✅     | ❌         | ❌    |
| Registrar registro médico         | ❌       | ✅     | ❌         | ❌    |
| Emitir relatórios/prescrições     | ❌       | ✅     | ❌         | ❌    |
| Criar agendas                     | ❌       | ❌     | ✅         | ✅    |
| Definir limites de seguro         | ❌       | ❌     | ❌         | ✅    |
| Visualizar relatórios financeiros | ❌       | ❌     | ❌         | ✅    |

---
