#8. Faça um programa que leia 5 números e informe a soma e a média dos números.


soma = 0
media = 0
numero = 0

for i in range(4):
    if i == 0:
       numero = float(input("Professora que conta é essa? "))
    else:
        numero = float(input(f"mais "))
    soma += numero

print(f"Ai é muito facil professora é {soma}")

# (serio agora)
for i in range(5):
    numero = float(input(f"Digite o numero {i+1}: "))
    soma += numero
    media = soma / 5 

print(f"Sua soma é: {soma}")
print(f"Sua média é: {media}")
