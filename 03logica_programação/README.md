# 🧠 Lógica de Programação e Ferramentas de Dev
**Curso:** Desenvolvimento de Sistemas (1° Termo)  
**Assunto:** Python, Clean Code e Versionamento com GitHub

---

## 🐍 1. Lógica com Python
Python é a linguagem ideal para aprender lógica devido à sua sintaxe próxima ao inglês.

### Conceitos Fundamentais:
*   **Variáveis e Tipos:** `str` (texto), `int` (inteiro), `float` (decimal), `bool` (verdadeiro/falso).
*   **Estruturas Condicionais:** `if`, `elif`, `else`.
*   **Estruturas de Repetição:** `while` (enquanto) e `for` (para).
*   **Listas:** Armazenamento de múltiplos valores em uma única variável.

**Exemplo de Código:**
```python
# Verificando se um aluno foi aprovado
media = float(input("Digite a nota: "))

if media >= 6:
    print("Aprovado! 🚀")
else:
    print("Recuperação. 📝")
```

---

## 🧼 2. Clean Code (Código Limpo)
Programar não é apenas fazer o computador entender, mas sim fazer **outros humanos** entenderem seu código.

**Princípios Básicos para Iniciantes:**
1.  **Nomes Significativos:** Em vez de `var x = 10`, use `total_pedidos = 10`.
2.  **Funções Pequenas:** Uma função deve fazer apenas uma coisa e fazê-la bem.
3.  **Comentários Óbvios:** Evite comentar o que o código já diz. Comente o "porquê", não o "quê".
4.  **Indentação:** Mantenha o código organizado (em Python, isso é obrigatório).

---

## 🐙 3. GitHub e Versionamento
O **Git** é o sistema que controla as versões do seu código, e o **GitHub** é a rede social onde você armazena e compartilha seus projetos.

### Comandos Básicos (Terminal):
*   `git init`: Inicia um novo repositório local.
*   `git add .`: Prepara todos os arquivos alterados para serem salvos.
*   `git commit -m "mensagem"`: Salva as alterações com uma descrição do que foi feito.
*   `git push`: Envia suas alterações locais para o servidor do GitHub.
*   `git pull`: Puxa as novidades do servidor para o seu computador.

---

## ⌨️ 4. Comandos Básicos de Terminal (CLI)
Essencial para navegar em diretórios e executar scripts Python:

*   `python nome_do_arquivo.py`: Executa um script Python.
*   `pip install nome_da_lib`: Instala bibliotecas externas.
*   `cd ..`: Volta uma pasta para trás.
*   `clear` (Linux/Mac) ou `cls` (Windows): Limpa a tela do terminal.

---

## 🚀 Desafio de Lógica
Crie um programa em Python que receba uma lista de nomes e salve apenas aqueles que começam com a letra "A" em uma nova lista, aplicando conceitos de **Clean Code** na nomenclatura das variáveis.

---
**Recursos Úteis:**
*   [Guia de Estilo Python (PEP 8)](https://python.org)
*   [Manual do Iniciante no GitHub](https://github.com)
