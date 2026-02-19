def dois_valores():
  a = int(input("Digite um número inteiro: "))
  b = float(input("Digite um número quebrado:  "))
  return a, b

a, b = dois_valores()
print(f"Soma: {a + b} \nSubtração: {b - a} \nMultiplicação: {a * b} \nDivisão: {a / b}")
