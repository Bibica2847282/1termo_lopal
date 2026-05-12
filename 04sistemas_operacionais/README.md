# 🖥️ Sistemas Operacionais (SO)
**Curso:** Desenvolvimento de Sistemas (1° Termo)  
**Assunto:** Fundamentos, Tipos e Gerenciamento de Recursos

---

## 🏗️ 1. O que é um Sistema Operacional?
O SO é o software fundamental que atua como uma **camada intermediária** entre o hardware (partes físicas) e o usuário/aplicativos.

**Principais funções:**
*   **Gerenciamento de Processos:** Controlar o que a CPU está processando.
*   **Gerenciamento de Memória:** Decidir onde os dados ficam guardados enquanto o PC está ligado (RAM).
*   **Sistema de Arquivos:** Organizar como os dados são salvos no HD/SSD.
*   **Interface:** Fornecer um meio para o usuário interagir (Gráfica ou Linha de Comando).

---

## 📂 2. Principais Ecossistemas

### 🪟 Windows (Microsoft)
*   **Características:** Interface amigável (GUI), focado em produtividade e jogos.
*   **Arquitetura:** Baseada no Kernel NT.
*   **Uso em Dev:** Muito usado para desenvolvimento .NET, C# e ambientes corporativos.

### 🐧 Linux (Open Source)
*   **Características:** Código aberto, altamente personalizável e gratuito.
*   **Distribuições (Distros):** Ubuntu, Debian, Fedora, Arch.
*   **Uso em Dev:** É o padrão para servidores e infraestrutura (Backend, Docker, Nuvem). Essencial dominar o **Terminal (Bash)**.

### 🍎 macOS e iOS (Apple)
*   **macOS:** Baseado em Unix. Estável e preferido por muitos desenvolvedores pela integração hardware-software.
*   **iOS:** Sistema fechado para dispositivos móveis Apple.
*   **Uso em Dev:** Necessário para desenvolver aplicativos nativos para o ecossistema Apple (Swift/Objective-C).

### 🤖 Android (Google)
*   **Características:** Baseado no Kernel Linux. É o SO móvel mais usado no mundo.
*   **Uso em Dev:** Desenvolvimento mobile (Java, Kotlin, Flutter).

---

## 🛠️ 3. Diferenças Técnicas Essenciais


| Característica | Windows | Linux | macOS |
|:---|:---|:---|:---|
| **Núcleo (Kernel)** | Híbrido (NT) | Monolítico | XNU (Unix-like) |
| **Código** | Fechado | Aberto | Fechado |
| **Caminho de Arquivos** | `C:\Users\Nome` | `/home/nome` | `/Users/nome` |
| **Terminal Principal** | PowerShell / CMD | Bash / Zsh | Zsh |

---

## ⌨️ 4. A Linha de Comando (CLI)
Para um desenvolvedor, o sistema operacional é acessado prioritariamente pelo terminal. Comandos básicos comuns em Linux/macOS:

*   `ls`: Listar arquivos.
*   `cd`: Mudar de diretório (pasta).
*   `mkdir`: Criar uma nova pasta.
*   `rm`: Remover arquivos.

---

## 💡 Conceito Importante: Virtualização e Containers
No 1º termo, é importante entender que podemos rodar um SO dentro de outro:
1.  **Máquinas Virtuais (VM):** Simulam um hardware completo (ex: VirtualBox).
2.  **WSL (Windows Subsystem for Linux):** Permite rodar Linux dentro do Windows nativamente para desenvolvimento.

---
**Exercício de Fixação:**
Abra o terminal do seu computador e tente descobrir qual a versão do Kernel instalada e quanto de memória RAM o sistema está consumindo no momento.
