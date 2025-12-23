# 🎨 Telas de UI por Função — Medora

Este documento descreve as telas da aplicação organizadas por **função de usuário**.
Serve como referência para **desenvolvimento frontend, design UX e validação de funcionalidades**.

---

## 👤 Telas do Paciente

### 🏠 Início / Catálogo de Profissionais

**Objetivo:** Descoberta de serviços

**Componentes:**

- Pesquisa por especialidade
- Filtros:
  - Cidade / Teleconsulta
  - Seguro aceito
  - Preço
  - Disponibilidade
- Lista de profissionais e clínicas

---

### 👨‍⚕️ Página de Perfil do Profissional

**Componentes:**

- Informações do médico
- Especialidade
- Avaliações e comentários
- Procedimentos oferecidos
- **Botão Agendar Consulta**

---

### 📅 Agendamento de Consulta

**Componentes:**

- Calendário com horários disponíveis
- Opções de seleção:
  - Tipo de atendimento (PARTICULAR / SEGURO)
  - Modalidade (ONLINE / PRESENCIAL)
- Upload de documentos (se necessário)

---

### 💳 Tela de Pagamento

**Componentes:**

- QR Code PIX
- Status do pagamento
- Instruções e tempo de expiração

---

### 📋 Minhas Consultas

**Descrição:**  
Lista de consultas agrupadas por status.

**Status:**

- Pendente
- Confirmada
- Paga
- Concluída

**Ações:**

- Cancelar
- Reagendar
- Fazer check-in
- Entrar em teleconsulta

---

### 📲 Check-in

**Componentes:**

- QR Code da consulta
- Confirmação de status de presença

---

### 💬 Chat da Consulta

**Descrição:**  
Mensagens relacionadas a uma consulta específica.

**Funcionalidades:**

- Enviar perguntas pré-consulta
- Receber documentos e instruções

---

### 📄 Documentos & Relatórios

**Componentes:**

- Lista cronológica de documentos
- Download de PDF
- Validação por QR Code

---

### ⭐ Avaliação da Consulta

**Componentes:**

- Classificação (estrelas)
- Feedback escrito

---

## 🧑‍⚕️ Telas do Médico / Profissional de Saúde

### 🏠 Dashboard do Profissional

**Visão geral:**

- Consultas agendadas para o dia
- Consultas em andamento
- Indicadores básicos de desempenho

---

### 📅 Agenda Diária

**Componentes:**

- Lista de pacientes
- Horários
- Status:
  - Aguardando
  - Em andamento
  - Concluída

---

### 🩺 Tela da Consulta

**Componentes:**

- Dados básicos do paciente
- Resumo do histórico clínico
- **Ação Iniciar Consulta**

---

### 📘 Prontuário Digital

**Componentes:**

- Evolução clínica
- Diagnóstico
- Conduta
- Upload de exames
- Sugestões de IA (opcional)

---

### 📄 Emissão de Documento Médico

**Componentes:**

- Seleção de tipo de documento:
  - Receita
  - Relatório médico
  - Atestado
- Pré-visualização de PDF
- Assinatura digital

---

### 📹 Teleconsulta

**Componentes:**

- Chamada de vídeo
- Chat
- Ação de encerrar consulta

---

### ⭐ Avaliações Recebidas

**Componentes:**

- Lista de feedbacks de pacientes
- Classificação média

---

## 🧑‍💼 Telas do Secretário / Atendente

### 🏠 Dashboard Operacional

**Visão geral:**

- Resumo da agenda diária
- Aprovações pendentes
- Pagamentos
- Alertas críticos

---

### 🗓️ Gerenciamento de Agenda Médica

**Componentes:**

- Configuração semanal
- Dias de trabalho
- Faixas de horário
- Duração dos slots

---

### 📆 Gerenciamento de Agenda Diária

**Componentes:**

- Total de slots
- Slots ocupados
- Ajustar limites de slots

---

### 📋 Gerenciamento de Consultas

**Listas:**

- Pendente
- Paga
- Confirmada

**Ações:**

- Aprovar
- Rejeitar
- Reagendar
- Cancelar

---

### 💳 Gerenciamento de Pagamentos

**Componentes:**

- Lista de pagamentos
- Confirmação manual
- Status de reembolso

---

### ⛔ Bloqueios de Agenda

**Componentes:**

- Criar bloqueios
- Editar ou remover bloqueios

---

### 🔔 Notificações

**Componentes:**

- Enviar notificações para pacientes

---

## 🧑‍💻 Telas do Administrador

### 🏠 Dashboard Administrativo

**Indicadores:**

- Receita
- Ocupação de agenda
- Consultas por tipo de atendimento

---

### 👥 Gerenciamento de Usuários

**Ações:**

- Criar médicos
- Criar secretários
- Ativar / desativar usuários

---

### 🏥 Gerenciamento de Clínica

**Componentes:**

- Dados da clínica
- Configurações gerais

---

### 🩺 Gerenciamento de Procedimentos

**Componentes:**

- Criar / editar procedimentos
- Preços
- Modalidade

---

### 💼 Gerenciamento de Seguros

**Componentes:**

- Cadastro de seguros
- Regras de aceitação

---

### 📊 Políticas de Atendimento

**Componentes:**

- Limites por tipo de atendimento:
  - Particular
  - Seguro
- Percentuais máximos
- Escopo por médico ou procedimento

---

### 📈 Relatórios

**Tipos:**

- Financeiro
- Utilização de agenda
- Consultas
- Reembolsos

---

## 🧭 Mapa de Telas (Alto Nível)

### Paciente

- Início
- Perfil do Profissional
- Consulta
- Pagamento
- Check-in
- Teleconsulta
- Documentos
- Avaliação

### Médico

- Dashboard
- Agenda Diária
- Consulta
- Prontuário
- Documentos
- Avaliações

### Secretário

- Dashboard
- Agenda Médica
- Agenda Diária
- Consultas
- Pagamentos
- Bloqueios de Agenda

### Admin

- Dashboard
- Usuários
- Clínica
- Procedimentos
- Seguros
- Políticas de Atendimento
- Relatórios
