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
