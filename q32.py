# 32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5

# 5! = 5 . 4 . 3 . 2 . 1 = 120
import math
fatorial = 1
num = int(input("Digite um numero pra realizar fatoração: "))
for i in range(1, num + 1):
    fatorial *= i

print(f"Fatorial: {fatorial}")