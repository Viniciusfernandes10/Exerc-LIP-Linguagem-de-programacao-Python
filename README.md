# Exercícios de Lógica em Python 🐍

Este repositório contém exercícios de lógica de programação resolvidos em Python,
organizados por capítulos.

📘 **Livro base:**  
**Python Básico - Um Guia para Iniciantes e Universitários**  
✍️ Autor: Helton Maia

🔗 Livro virtual:  
https://heltonmaia.com/pythonbook/intro.html

## [Capítulo 1: Introdução à programação em Python](https://heltonmaia.com/pythonbook/chapters/ch1/ch1.html)

### **Lista de exercícios**

## – Exercício 01 –

Arquivo: `capitulo1/ex01.py`

### Enunciado

Escreva um programa que imprima a famosa mensagem do mundo da programação.

Neste exercício, você deve simplesmente exibir uma mensagem na tela.
Não é necessário ler nenhuma entrada do usuário, apenas utilizar o comando `print`.

### Exemplo de saída esperada

**Saída:**
Hello World!

### Resolução

```python
print("Hello World!!")
```

---

## – Exercício 02 –

Arquivo: `capitulo1/ex02.py`

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

Arquivo: `capitulo1/ex03.py`

### Enunciado

Informações de um Pedido. Crie um programa que deve ler quatro entradas do usuário:

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

## [Capítulo 2: Tipos de dados e Estruturas Condicionais](https://heltonmaia.com/pythonbook/chapters/ch2/ch2.html)

### **Lista de exercícios**

## – Exercício 01 –

Arquivo: `capitulo2/ex01.py`

### Enunciado

Escreva um programa que solicita ao usuário dois valores, um do tipo inteiro (`int`) e outro do tipo ponto flutuante (`float`). Após receber esses valores como entrada, o programa deve atribuí-los a duas variáveis distintas e, em seguida, imprimir na tela o resultado das seguintes operações matemáticas:

- Soma dos dois valores.
- Subtração do valor do tipo float pelo valor do tipo inteiro.
- Multiplicação dos dois valores.
- Divisão do valor do tipo inteiro pelo valor do tipo float.

Certifique-se de formatar adequadamente a saída dos resultados.

### Exemplo de saída esperada

**Entrada:**

Ana Souza  
Livro de Python  
1
45.50

**Saída:**

Pedido confirmado: Livro de Python
Valor total: R$ 45.50
Obrigado pela preferência!

### Resolução

```python
def dois_valores():
  a = int(input("Digite um número inteiro: "))
  b = float(input("Digite um número quebrado:  "))
  return a, b

a, b = dois_valores()
print(f"Soma: {a + b} \nSubtração: {b - a} \nMultiplicação: {a * b} \nDivisão: {a / b}")

```

---

## – Exercício 02 –

Arquivo: `capitulo2/ex02.py`

### Enunciado

Escreva um programa que solicite ao usuário que insira uma palavra ou frase. Em seguida, o programa deve imprimir o comprimento da string, a primeira letra da string, a última letra da string e a string invertida.

### Exemplo de saída esperada

## Teste 1

**Entrada:**

A felicidade está nas pequenas coisas 

**Saída:**

37  
A  
s  
sasioc saneuqep san átse edadicilef A  

## Teste 2

**Entrada:**

Entrada: A verdadeira liberdade está em conhecer a si mesmo 

**Saída:**

A  
o  
omsem is a recehnoc me átse edadrebil ariedadrev A  

### Resolução

```python
def palavra_ou_frase():
  frase = input("Digite uma frase: ")
  quant_caracteres = len(frase)
  primeira_letra = frase[0]
  ultima_letra = frase[-1]
  string_invertida = frase[::-1]
  return frase, quant_caracteres, primeira_letra, ultima_letra, string_invertida

frase, quant_caracteres, primeira_letra, ultima_letra, string_invertida = palavra_ou_frase()
print(f"{quant_caracteres} \n{primeira_letra} \n{ultima_letra} \n{string_invertida}")

```

---

## – Exercício 03 –

Arquivo: `capitulo2/ex03.py`

### Enunciado

Escreva um programa que compare duas strings fornecidas pelo usuário, considerando valores booleanos "True" ou "False". O programa deve ignorar diferenças de capitalização (maiúsculas e minúsculas) e imprimir na tela se as strings são iguais ou diferentes.

### Exemplo de saída esperada

**Teste 1**

Entrada:
True  
true  

Saída:
São iguais

**Teste 2**

Entrada:
True  
False  

Saída:
São diferentes

### Resolução

```python
def comparar():
  string1 = input("Escreva True ou False: ").lower()
  string2 = input("Escreva True ou False: ").lower()
  if string1 == string2:
    print("São iguais")
  else:
    print("São diferentes")
  return string1, string2

a, b = comparar()

```

---

## – Exercício 04 –

Arquivo: `capitulo2/ex04.py`

### Enunciado

Faça um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O IMC é calculado dividindo-se o peso da pessoa pela sua altura ao quadrado. O IMC é uma medida da relação entre o peso e a altura de uma pessoa. O programa deve imprimir o IMC da pessoa, classificando-o de acordo com a tabela abaixo:
IMC | Classificação

< 18.5      | Abaixo do peso
18.5 - 24.9 | Saudável
25.0 - 29.9 | Sobrepeso
30.0 - 34.9 | Obesidade grau I
35.0 - 39.9 | Obesidade grau II
>= 40.0     | Obesidade grau III
### Exemplo de saída esperada

## Teste 1 

**Entrada:**

71  
1.70  

Saída: 
Seu IMC é 24.57 (Saudável).

## Teste 2

**Entrada:**

85  
1.60  

**Saída:**

Seu IMC é 33.20 (Obesidade grau I).

### Resolução

```python
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Saudável"
    elif imc <= 29.9:
        classificacao = "Sobrepeso"
    elif imc <= 34.9:
        classificacao = "Obesidade grau I"
    elif imc <= 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return imc, classificacao

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc, classificacao = calcular_imc(peso, altura)
print(f"Seu IMC é {imc:.2f} ({classificacao})")

```

---

## – Exercício 05 –

Arquivo: `capitulo2/ex05.py`

### Enunciado

Crie um programa que solicite ao usuário a inserção de cinco frutas diferentes. Antes da leitura dos dados, crie uma lista vazia chamada frutas. Em seguida, armazene as frutas fornecidas pelo usuário nessa lista e, ao final, imprima a lista completa na tela.

## Teste 1

**Entrada:**

maçã  
banana  
laranja  
pera  
melancia  

Saída: 
Lista de frutas: ['maçã', 'banana', 'laranja', 'pera', 'melancia']

## Teste 2

**Entrada:**

uva  
abacaxi  
morango  
manga  
kiwi  

**Saída:**
Lista de frutas: ['uva', 'abacaxi', 'morango', 'manga', 'kiwi']


### Resolução

```python
def lista_frutas():
    frutas = []

    for i in range(5):
        fruta = input()
        frutas.append(fruta)

    return frutas

frutas = lista_frutas()
print("Lista de frutas:", frutas)

```

---

## – Exercício 06 –

Arquivo: `capitulo2/ex06.py`

### Enunciado

Escreva um programa que solicite ao usuário a inserção de duas coordenadas (x e y). Em seguida, crie uma tupla chamada coordenadas com esses valores e imprima o conteúdo da tupla na tela.

## Teste 1

**Entrada:**

2.5  
3.8  

**Saída:**
Coordenadas: (2.5, 3.8)

## Teste 2

**Entrada:**

-1.0  
0.0  

**Saída:**
Coordenadas: (-1.0, 0.0)


### Resolução

```python
def recebe_coordenadas(x, y):
    coordenadas = (x, y)
    return coordenadas

x = float(input())
y = float(input())

coordenadas = recebe_coordenadas(x, y)

print("Coordenadas:", coordenadas)

```

---

## – Exercício 07 –

Arquivo: `capitulo2/ex07.py`

### Enunciado

Crie um dicionário chamado contato. Solicite ao usuário que forneça os dados correspondentes às chaves "nome", "telefone" e "endereco". Em seguida, imprima o conteúdo completo do dicionário.

## Teste 1

*Entrada:*

Python da Silva  
8499999999  
Rua da Programação, 123  

**Saída:**
Nome: Python da Silva, Telefone: 8499999999, Endereço: Rua da Programação, 123.

## Teste 2

*Entrada:*

João da Silva  
9876543210  
Avenida dos Códigos, 456  

*Saída:*
Nome: João da Silva, Telefone: 9876543210, Endereço: Avenida dos Códigos, 456.


### Resolução

```python
def dict_contato(nome, telefone, endereco):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "endereco": endereco
    }
    return contato


nome = input()
telefone = input()
endereco = input()

contato = dict_contato(nome, telefone, endereco)

print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Endereço: {contato['endereco']}.")

```

---

## – Exercício 08 –

Arquivo: `capitulo2/ex08.py`

### Enunciado

Crie, antes da leitura dos números, um conjunto vazio chamado numeros utilizando a função set(). Em seguida, armazene os valores fornecidos pelo usuário nesse conjunto, utilizando o método .add(). Ao final, exiba o conjunto completo na saída.

# Teste 1

*Entrada:*

3  
5  
7  
9  
11  

Saída: 
{3, 5, 7, 9, 11}

## Teste 2

*Entrada:*

-2  
0  
4  
6  
8  

Saída: 
{0, 4, 6, 8, -2}


### Resolução

```python
def conjunto_numeros():
    numeros = set()  

    for i in range(5):
        valor = int(input())
        numeros.add(valor)

    return numeros

numeros = conjunto_numeros()
print(numeros)

```

---

## – Exercício 09 –

Arquivo: `capitulo2/ex09.py`

### Enunciado

Faça um programa que solicite ao usuário a inserção de três números inteiros distintos para cada conjunto. Os conjuntos conjunto_a e conjunto_b devem ser criados utilizando a função set() e preenchidos com os números fornecidos pelo usuário, utilizando o método .add(). Em seguida, realize as seguintes operações e imprima os resultados:

União: combinar os elementos únicos de ambos os conjuntos.

Interseção: encontrar os elementos que estão presentes em ambos os conjuntos.

Diferença: identificar os elementos que estão em conjunto_a, mas não em conjunto_b.

## Teste 1

*Entrada:*

3  
5  
7  
7  
9  
11  

*Saída:*

União: {3, 5, 7, 9, 11}  
Interseção: {7}  
Diferença: {3, 5}  

## Teste 2

*Entrada:*

1  
2  
3  
4  
5  
1  

*Saída:*

União: {1, 2, 3, 4, 5}  
Interseção: {1}  
Diferença: {2, 3}  

### Resolução

```python
def verificar_conjuntos():
  conjunto_a = set()
  conjunto_b = set()

  for i in range(3):
    num = int(input())
    conjunto_a.add(num)

  for i in range(3):
    num = int(input())
    conjunto_b.add(num)

  uniao = conjunto_a | conjunto_b
  intersecao = conjunto_a & conjunto_b
  diferenca = conjunto_a - conjunto_b
  
  return uniao, intersecao, diferenca

uniao, intersecao, diferenca = verificar_conjuntos()
print(f"União: {uniao}")
print(f"Interseção: {intersecao}")
print(f"Diferença: {diferenca}")

```

---

## – Exercício 10 –

Arquivo: `capitulo2/ex10.py`

### Enunciado

Dada duas strings fornecidas pelo usuário, realize as seguintes operações e imprima os resultados:

Transformar em maiúsculas: converta toda a primeira string para letras maiúsculas.

Transformar em minúsculas: converta toda a segunda string para letras minúsculas.

Concatenar as strings: combine a primeira e a segunda string em uma única string.

Imprimir o resultado: exiba a string concatenada na tela.

## Teste 1

**Entrada:**

Olá, mundo.  
Mundo  

**Saída:**

OLÁ, MUNDO.  
mundo  
OLÁ, MUNDO. mundo  

## Teste 2

**Entrada:**

A Verdade Está Lá Fora, Neo.  
Mas Você Tem Que Escolher Se Quer Vê-la.  

**Saída:**

A VERDADE ESTÁ LÁ FORA, NEO.  
mas você tem que escolher se quer vê-la.  
A VERDADE ESTÁ LÁ FORA, NEO. mas você tem que escolher se quer vê-la.  

### Resolução

```python
def transformar_string():
    string1 = input()
    string2 = input()

    print(string1.upper())
    print(string2.lower())
    print(string1.upper() + " " + string2.lower())


transformar_string()

```

---

## – Exercício 11 –

Arquivo: `capitulo2/ex11.py`

### Enunciado

Você deve criar um programa que verifica se os números em uma lista são pares ou ímpares.  
A lista possui tamanho 5 e será fornecida pelo usuário.  
Cada número deve ser avaliado individualmente, sem o uso de estruturas de repetição (loops).  
O programa deve exibir na tela se cada número é par ou ímpar.

### Teste 1

**Entrada:**

4  
9  
12  
17  
6  

**Saída:**

O número 4 é par.  
O número 9 é ímpar.  
O número 12 é par.  
O número 17 é ímpar.  
O número 6 é par.  

### Teste 2

**Entrada:**

5  
6  
7  
1  
2  

**Saída:**

O número 5 é ímpar.  
O número 6 é par.  
O número 7 é ímpar.  
O número 1 é ímpar.  
O número 2 é par.  

### Resolução

```python
def par_ou_impar():
    numero1 = int(input())
    numero2 = int(input())
    numero3 = int(input())
    numero4 = int(input())
    numero5 = int(input())

    if numero1 % 2 == 0:
        print(f"O número {numero1} é par.")
    else:
        print(f"O número {numero1} é ímpar.")

    if numero2 % 2 == 0:
        print(f"O número {numero2} é par.")
    else:
        print(f"O número {numero2} é ímpar.")

    if numero3 % 2 == 0:
        print(f"O número {numero3} é par.")
    else:
        print(f"O número {numero3} é ímpar.")

    if numero4 % 2 == 0:
        print(f"O número {numero4} é par.")
    else:
        print(f"O número {numero4} é ímpar.")

    if numero5 % 2 == 0:
        print(f"O número {numero5} é par.")
    else:
        print(f"O número {numero5} é ímpar.")

par_ou_impar()
```
---

## – Exercício 12 –

Arquivo: `capitulo2/ex12.py`

### Enunciado

Escreva um programa para coletar informações de um aluno. Utilizando um dicionário denominado “aluno”, solicite ao usuário as seguintes informações:

Nome do aluno.  
Matrícula do aluno.  
Três notas do aluno.  

Posteriormente, exiba na tela os dados registrados, incluindo o nome, matrícula e a média das três notas do aluno. Utilize somente os métodos especiais dos dicionários para inserir e acessar os dados.

### Teste 1

**Entrada:**

Linus Benedict Torvalds  
12345  
8.5  
7.2  
9.0  

**Saída:**

Nome: Linus Benedict Torvalds  
Matrícula: 12345  
Média: 8.23  

### Teste 2

**Entrada:**

Ada Lovelace  
67890  
9.8  
8.7  
10.0  

**Saída:**

Nome: Ada Lovelace  
Matrícula: 67890  
Média: 9.5   

### Resolução

```python
def dicionario_aluno():

  nome = input()
  matricula = int(input())
  nota1 = float(input())
  nota2 = float(input())
  nota3 = float(input())

  media = (nota1 + nota2 + nota3) / 3

  aluno ={
    "Nome": nome,
    "Matrícula": matricula,
    "Média": media
  }

  return aluno

aluno = dicionario_aluno()
print(f"Nome: {aluno['Nome']}")
print(f"Matrícula: {aluno['Matrícula']}")
print(f"Média: {aluno['Média']:.2f}")
```
---
