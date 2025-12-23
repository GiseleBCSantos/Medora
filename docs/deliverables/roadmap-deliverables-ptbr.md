# 🗺️ Roadmap de Desenvolvimento — HealthSync

Este roadmap organiza o projeto em sprints incrementais, cada um entregando um conjunto coerente e demonstrável de funcionalidades.  
Cada sprint pode ser tratado como um marco independente ou backlog de sprint.

---

## 🟢 Sprint 1 — Fundação do Sistema

### 🎯 Objetivo do Sprint

Dar vida ao sistema com autenticação, infraestrutura principal e domínio base.

### 🔧 Backend — Sprint Backlog

- [ ] Configuração Django + Django REST Framework
- [ ] Configuração Docker & Docker Compose
- [ ] Integração com banco de dados PostgreSQL
- [ ] Autenticação JWT
- [ ] Modelo de usuário com funções
- [ ] CRUD de Clínica
- [ ] Permissões básicas RBAC por tipo de usuário

### 🎨 Frontend — Sprint Backlog

- [ ] Configuração React (Vite ou Next.js)
- [ ] Configuração Tailwind CSS
- [ ] Layout base (cabeçalho, navegação, rodapé)
- [ ] Fluxo de Login / Logout
- [ ] Proteção de rotas por função

### 📄 Entregável

- ✔ Autenticação funcionando
- ✔ Usuários podem fazer login com funções
- ✔ Clínicas podem ser criadas
- ✔ API segura + UI protegida

📌 **Checkpoint de fundação sólida**

---

## 🟢 Sprint 2 — Domínio Clínico Principal

### 🎯 Objetivo do Sprint

Modelar a estrutura clínica do mundo real.

### 🔧 Backend — Sprint Backlog

- [ ] CRUD de Médico
- [ ] CRUD de Paciente
- [ ] CRUD de Procedimento
- [ ] Relacionamentos de Clínica
- [ ] Permissões:
  - Admin / Secretário gerenciam
  - Paciente somente leitura

### 🎨 Frontend — Sprint Backlog

- [ ] Tela de cadastro de médico
- [ ] Tela de cadastro de paciente
- [ ] Listagem de procedimentos
- [ ] Formulários validados

### 📄 Entregável

- ✔ Entidades principais de saúde totalmente modeladas
- ✔ Dados visíveis e gerenciáveis na UI

---

## 🟢 Sprint 3 — Agenda Médica (Regras Semanais)

### 🎯 Objetivo do Sprint

Definir quando os médicos estão disponíveis.

### 🔧 Backend — Sprint Backlog

- [ ] CRUD de AgendaMedica
- [ ] CRUD de BloqueioAgenda
- [ ] Regras de negócio:
  - Dias úteis válidos
  - Faixas de horário válidas

### 🎨 Frontend — Sprint Backlog

- [ ] Tela de configuração de agenda semanal
- [ ] Gerenciamento de bloqueios de agenda

### 📄 Entregável

- ✔ Agendas semanais configuradas
- ✔ Exceções aplicadas corretamente

📌 **Funcionalidade de domínio de alto valor**

---

## 🟡 Sprint 4 — Agenda Diária & Controle de Capacidade

### 🎯 Objetivo do Sprint

Transformar regras em agendas diárias reais.

### 🔧 Backend — Sprint Backlog

- [ ] CRUD de AgendaDia
- [ ] Geração automática a partir de AgendaMedica
- [ ] Ajuste de capacidade de slots diários
- [ ] Log de auditoria de ajustes (AjusteAgendaLog)

### 🎨 Frontend — Sprint Backlog

- [ ] Visualização de agenda diária
- [ ] Ajuste manual de capacidade
- [ ] Avisos de conflitos

### 📄 Entregável

- ✔ Agenda diária real
- ✔ Capacidade controlada com segurança

---

## 🟡 Sprint 5 — Fluxo de Consultas

### 🎯 Objetivo do Sprint

Permitir que pacientes solicitem consultas.

### 🔧 Backend — Sprint Backlog

- [ ] CRUD de Consulta
- [ ] Validação de disponibilidade
- [ ] Limites por tipo de consulta
- [ ] Ciclo de vida do status da consulta

### 🎨 Frontend — Sprint Backlog

- [ ] Catálogo de médicos
- [ ] Seleção de data e horário
- [ ] Fluxo de solicitação de consulta

### 📄 Entregável

- ✔ Solicitações de consulta funcionando
- ✔ Status visível para todas as funções

---

## 🟠 Sprint 6 — Aprovação & Regras Críticas

### 🎯 Objetivo do Sprint

Habilitar controle administrativo real.

### 🔧 Backend — Sprint Backlog

- [ ] Aprovar / rejeitar consultas
- [ ] Criação automática de registro de reembolso
- [ ] Notificações internas

### 🎨 Frontend — Sprint Backlog

- [ ] Dashboard do secretário
- [ ] Ações de aprovar / rejeitar
- [ ] Mensagens de feedback ao paciente

### 📄 Entregável

- ✔ Fluxo administrativo completo
- ✔ Lógica de reembolso modelada

📌 **Marco perfeito para demonstração**

---

## 🟠 Sprint 7 — Pagamentos (PIX)

### 🎯 Objetivo do Sprint

Introduzir rastreabilidade financeira.

### 🔧 Backend — Sprint Backlog

- [ ] Entidade de Pagamento
- [ ] Integração PIX (ou mock)
- [ ] Simulação de webhook
- [ ] Automação de reembolso

### 🎨 Frontend — Sprint Backlog

- [ ] Tela de pagamento
- [ ] Exibição de QR Code PIX
- [ ] Atualizações de status de pagamento

### 📄 Entregável

- ✔ Pagamentos rastreáveis
- ✔ Reembolsos consistentes

---

## 🔵 Sprint 8 — Check-in & Fluxo do Dia da Consulta

### 🎯 Objetivo do Sprint

Suportar o fluxo de trabalho do dia da consulta.

### 🔧 Backend — Sprint Backlog

- [ ] Check-in por QR Code
- [ ] Regras de validação de horário
- [ ] Transições de status de consulta

### 🎨 Frontend — Sprint Backlog

- [ ] Tela de check-in
- [ ] Scanner de QR code
- [ ] Visualização de status

### 📄 Entregável

- ✔ Check-in funcionando

---

## 🔵 Sprint 9 — Registros Médicos & Documentos

### 🎯 Objetivo do Sprint

Entregar valor clínico real.

### 🔧 Backend — Sprint Backlog

- [ ] CRUD de registro médico
- [ ] CRUD de documentos médicos
- [ ] Geração de PDF
- [ ] Aplicação de controle de acesso

### 🎨 Frontend — Sprint Backlog

- [ ] Tela de registro médico do médico
- [ ] Download de documentos do paciente

### 📄 Entregável

- ✔ Consultas documentadas
- ✔ Documentos médicos legais gerados

---

## 🔵 Sprint 10 — Teleconsulta & Funcionalidades Avançadas

### 🎯 Objetivo do Sprint

Demonstrar capacidades avançadas.

### 🔧 Backend — Sprint Backlog

- [ ] Criação de sala de teleconsulta
- [ ] Tokens de acesso
- [ ] Logs de sessão

### 🎨 Frontend — Sprint Backlog

- [ ] Tela de consulta por vídeo
- [ ] Acesso a consultas online

### 📄 Entregável

- ✔ Teleconsulta implementada ou documentada

📌 **Excelente encerramento de projeto**

---

## 🧠 Nota Estratégica

Se o escopo ou tempo se tornar restrito:
👉 Pare no **Sprint 6**  
👉 Tudo depois se torna **trabalho futuro**

Isso ainda entrega uma plataforma de saúde completa e impressionante.
