#3. Faça um programa que leia e valide as seguintes informações:

# # Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
while True:

    nome = input("nome: ")
    if len(nome) > 3:
        break
    else:
        print("Nome precisa ser maior que 3 letras.")
        continue

while True:
    idade = int(input("idade: "))
    if idade >= 0 and idade <= 150:
        break
    else:
        print("Insira uma idade válida.")
        continue

while True:
    salário = float(input("salário: "))
    if salário != 0:
        break
    else:
        print("Insira salário válido.")
        continue

while True:
    sexo = input("sexo (f, m, nb): ")
    if sexo == "f" or sexo == "m" or sexo == "nb":
        break
    else:
        print("Insira sexo válido")
        continue

while True:
    estado_civil = input("estado civil ('s', 'c', 'v', 'd'): ")
    if estado_civil in ["s", "c", "v", "d"]:
        break
    else:
        print("Insira estado civil válido.")
        continue


        