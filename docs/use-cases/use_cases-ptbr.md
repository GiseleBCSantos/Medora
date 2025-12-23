# 📌 Casos de Uso — Medora

_(Organizados por Função de Usuário)_

Este documento descreve os principais casos de uso da plataforma Medora,
organizados por perfil de usuário e alinhados com o modelo RBAC.

---

## 👤 Paciente — Casos de Uso

### UC-01 — Criar Conta de Paciente

**Ator:** Paciente

**Descrição:**  
Permite que um novo paciente crie uma conta no sistema.

**Fluxo Principal:**

1. Paciente fornece nome, email, senha e CPF
2. Sistema valida os dados
3. Sistema cria um Usuário com função PACIENTE
4. Sistema cria um perfil Paciente vinculado ao Usuário

**Regras de Negócio:**

- CPF e email devem ser únicos
- Conta inicia como ativa

---

### UC-02 — Pesquisar Profissional ou Clínica

**Ator:** Paciente

**Descrição:**  
Permite pesquisar profissionais ou clínicas disponíveis.

**Filtros:**

- Especialidade
- Modalidade (presencial / teleconsulta)
- Seguro aceito
- Preço
- Dias disponíveis

---

### UC-03 — Solicitar Consulta

**Ator:** Paciente

**Descrição:**  
Solicita uma consulta ou procedimento.

**Fluxo Principal:**

1. Seleciona profissional ou procedimento
2. Escolhe data e horário disponível
3. Seleciona tipo de atendimento (PARTICULAR / SEGURO)
4. Sistema valida limites de política de atendimento
5. Sistema cria consulta com status PENDENTE

**Fluxo Alternativo:**

- Se limite de seguro for excedido → solicitação é bloqueada

---

### UC-04 — Realizar Pagamento

**Ator:** Paciente

**Descrição:**  
Realiza pagamento via PIX.

**Pós-condição:**

- Status da consulta atualizado para PAGA

---

### UC-05 — Realizar Check-in

**Ator:** Paciente

**Descrição:**  
Confirma presença usando QR Code.

---

### UC-06 — Entrar em Teleconsulta

**Ator:** Paciente

**Pré-condição:**  
Consulta confirmada

**Descrição:**  
Entra na sala de consulta virtual no horário agendado.

---

### UC-07 — Visualizar Documentos Médicos

**Ator:** Paciente

**Descrição:**  
Baixa prescrições, relatórios e certificados emitidos para suas consultas.

---

### UC-08 — Avaliar Consulta

**Ator:** Paciente

**Pré-condição:**  
Consulta finalizada

**Descrição:**  
Avalia e comenta o profissional e a clínica.

---

## 🧑‍⚕️ Médico — Casos de Uso

### UC-09 — Visualizar Agenda Diária

**Ator:** Médico

**Descrição:**  
Visualiza consultas diárias organizadas por horário.

---

### UC-10 — Iniciar Consulta

**Ator:** Médico

**Descrição:**  
Inicia consulta presencial ou teleconsulta.

---

### UC-11 — Registrar Prontuário

**Ator:** Médico

**Descrição:**  
Registra evolução clínica, diagnóstico e conduta.

**Fluxo Opcional de IA:**

- Sistema sugere resumo ou código CID-10

---

### UC-12 — Emitir Documento Médico

**Ator:** Médico

**Descrição:**  
Emite:

- Receita
- Relatório médico
- Atestado
- Declaração

**Pós-condição:**

- PDF gerado com QR Code de validação

---

### UC-13 — Encerrar Consulta

**Ator:** Médico

**Descrição:**  
Finaliza consulta e libera documentos ao paciente.

---

### UC-14 — Visualizar Avaliações

**Ator:** Médico

**Descrição:**  
Visualiza feedbacks recebidos de pacientes.

---

## 🧑‍💼 Secretário — Casos de Uso

### UC-15 — Criar Agenda Médica

**Ator:** Secretário

**Descrição:**  
Define dias e horários de trabalho semanais para um médico.

---

### UC-16 — Gerar Agenda Diária

**Ator:** Sistema (acionado pelo Secretário)

**Descrição:**  
Gera automaticamente agenda diária baseada em regras semanais.

---

### UC-17 — Aprovar ou Rejeitar Consulta

**Ator:** Secretário  
**Ator Secundário:** Sistema de Pagamento

**Descrição:**  
Aprova ou rejeita solicitações de consulta, lidando com pagamentos se necessário.

**Fluxo Principal (Aprovação):**

1. Secretário revisa consulta pendente
2. Sistema valida disponibilidade
3. Status da consulta definido como CONFIRMADA
4. Paciente é notificado

**Fluxo Alternativo A — Rejeição sem pagamento:**

- Status definido como REJEITADA
- Paciente notificado

**Fluxo Alternativo B — Rejeição com pagamento:**

- Consulta definida como REJEITADA
- Registro de reembolso criado
- Processo de reembolso iniciado
- Paciente notificado

**Regras de Negócio:**

- Todos os pagamentos devem permanecer rastreáveis
- Reembolsos não deletam registros financeiros

---

### UC-18 — Ajustar Slots Diários

**Ator:** Secretário

**Descrição:**  
Ajusta o número de slots disponíveis para um dia específico.

**Fluxo Principal:**

1. Secretário atualiza limite de slots
2. Sistema valida consultas existentes
3. Nova configuração é salva
4. Log de auditoria é criado

**Fluxo Alternativo:**

- Se novo limite < consultas confirmadas:
  - Sistema bloqueia mudança
  - Secretário deve reagendar ou cancelar consultas
  - Cancelamentos pagos acionam reembolsos

---

### UC-19 — Confirmar Pagamento

**Ator:** Secretário

**Descrição:**  
Confirma manualmente um pagamento em casos excepcionais.

---

### UC-20 — Realizar Check-in Manual

**Ator:** Secretário

**Descrição:**  
Registra presença do paciente manualmente.

---

### UC-21 — Bloquear Agenda

**Ator:** Secretário

**Descrição:**  
Bloqueia datas de agenda devido a férias ou indisponibilidade.

---

## 🧑‍💻 Administrador — Casos de Uso

### UC-22 — Gerenciar Usuários

**Ator:** Admin

**Descrição:**  
Cria, edita e desativa usuários.

---

### UC-23 — Configurar Procedimentos

**Ator:** Admin

**Descrição:**  
Define preço, duração e modalidade do procedimento.

---

### UC-24 — Configurar Provedores de Seguro

**Ator:** Admin

**Descrição:**  
Registra provedores de seguro aceitos.

---

### UC-25 — Definir Políticas de Atendimento

**Ator:** Admin

**Descrição:**  
Define limites de consultas por tipo de atendimento:

- Particular
- Seguro
- Gratuito

---

### UC-26 — Visualizar Relatórios

**Ator:** Admin

**Descrição:**  
Acessa:

- Relatórios financeiros
- Ocupação de agenda
- Consultas por tipo de atendimento

---
