# 📋 Engenharia de Software: Levantamento de Requisitos
**Curso:** Desenvolvimento de Sistemas (1° Termo)
**Assunto:** Coleta, Análise e Documentação de Necessidades

---

## 🧐 1. O que são Requisitos?
Requisitos são as descrições dos serviços que um sistema deve fornecer e as restrições sob as quais ele deve operar. É a fase onde descobrimos **o que** o sistema deve fazer antes de decidir **como** fazer.

### Classificação Principal:
*   **Requisitos Funcionais (RF):** Descrevem as funções que o software deve realizar (o que o sistema faz).
    *   *Exemplo:* "O sistema deve permitir o cadastro de novos alunos."
*   **Requisitos Não Funcionais (RNF):** Descrevem as características de qualidade ou restrições (como o sistema deve ser).
    *   *Exemplo:* "O sistema deve ser acessível via navegador e carregar em menos de 3 segundos."

---

## 🛠️ 2. Técnicas de Levantamento (Elicitação)
Para extrair informações dos stakeholders (interessados), utilizamos diversas técnicas:

1.  **Entrevistas:** Conversas diretas com os usuários para entender suas dores.
2.  **Questionários:** Úteis para coletar dados de um grande volume de pessoas.
3.  **Observação (Job Shadowing):** Observar o usuário trabalhando para entender o fluxo real de tarefas.
4.  **Brainstorming:** Reuniões criativas para gerar ideias de funcionalidades.
5.  **Prototipagem:** Criar telas simples (mockups) para validar se o entendimento está correto.

---

## 📝 3. Documentação de Requisitos
Um bom requisito deve ser claro, conciso e testável. No 1° termo, costumamos usar a estrutura de identificadores:


| ID | Descrição | Tipo |
|:---:|:---|:---:|
| **RF01** | O sistema deve permitir que o administrador exclua registros. | Funcional |
| **RF02** | O sistema deve emitir um relatório semanal de vendas em PDF. | Funcional |
| **RNF01** | As senhas dos usuários devem ser criptografadas no banco de dados. | Não Funcional |
| **RNF02** | A interface deve ser responsiva (adaptar-se a celulares). | Não Funcional |

---

## 🔄 4. Ciclo de Vida do Requisito
1.  **Elicitação:** Coleta de informações.
2.  **Análise:** Verificar se há conflitos entre o que diferentes usuários pediram.
3.  **Especificação:** Escrita formal no documento.
4.  **Validação:** O cliente lê e confirma: "É isso mesmo que eu preciso".

---

## 💡 Dica para o Aluno (Regra de Ouro)
Um requisito mal levantado no início do projeto custa até **100 vezes mais caro** para ser corrigido após o software estar pronto. Investir tempo aqui evita retrabalho!

---
**Exercício Sugerido:** 
Pense em um aplicativo de delivery (tipo iFood). Liste 3 Requisitos Funcionais e 2 Requisitos Não Funcionais essenciais para o funcionamento dele.
