#7. Faça um programa que leia 5 números e informe o maior número.
maior = None
menor =  None

for i in range(5):
    numero = float(input(f"Insira numero {i+1}: "))
    if maior > numero:
        maior == numero
    elif menor < numero:
        menor == numero

print(f"Maior numero é {maior}")
print(f"Maior numero é {menor}")