# Exercícios de Lógica em Python 🐍

Este repositório contém exercícios de lógica de programação resolvidos em Python,
organizados por capítulos 1 e 2.

📘 **Livro base:**  
**Python Básico - Um Guia para Iniciantes e Universitários**  
✍️ Autor: Helton Maia

🔗 Livro virtual:  
https://heltonmaia.com/pythonbook/intro.html

## Capítulo 1 – Introdução à programação em Python

### **Lista de exercícios**

## – Exercício 01 –

Arquivo: `lista1_ex01.py`

### Enunciado

Escreva um programa que imprima a famosa mensagem do mundo da programação.

Neste exercício, você deve simplesmente exibir uma mensagem na tela.
Não é necessário ler nenhuma entrada do usuário, apenas utilizar o comando `print`.

### Exemplo de saída esperada

Hello World!

### Resolução

```python
print("Hello World!!")
```

---

## – Exercício 02 –

Arquivo: `lista1_ex02.py`

### Enunciado

Neste exercício, você deve ler duas entradas: o nome de um aluno e sua matrícula. Em seguida, exiba uma mensagem de boas-vindas formatada com esses dados.

### Exemplo de saída esperada

**Entrada:**

Python da Silva

2024123456

**Saída:**

Olá Python da Silva Matrícula: 2024123456 Seja bem vindo!

### Resolução

```python
def informacao():
    nome = input("Digite seu nome: ")
    matricula = input("Digite sua matrícula: ")
    return nome, matricula

nome, matricula = informacao()
print(f"Olá {nome} Matrícula: {matricula} Seja bem-vindo!")
```

---

## – Exercício 03 –

Arquivo: `lista1_ex03.py`

### Enunciado

1. Informações de um Pedido. Crie um programa que deve ler quatro entradas do usuário:

- Nome do cliente
- Produto comprado
- Quantidade adquirida
- Valor unitário do produto

Em seguida, exiba uma mensagem formatada informando os detalhes da compra, incluindo o valor total.

### Exemplo de saída esperada

**Entrada:**

Ana Souza  
Livro de Python  
1
45.50

Saída:

Pedido confirmado: Livro de Python
Valor total: R$ 45.50
Obrigado pela preferência!

### Resolução

```python
def pedido():
  nome = input("Digite seu nome: ")
  produto = input("Digite o produto solicitado: ")
  quantidade = int(input("Digite a quantidade: "))
  valor = float(input("Digite o valor do produto: "))
  return nome, produto, quantidade, valor

nome, produto, quantidade, valor = pedido()
print(f"Pedido confirmado: {produto} \nValor total: R${valor * quantidade:.2f} \nObrigado pela preferência {nome}!")

```

---
