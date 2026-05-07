# 40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

#     Código da cidade;
#     Número de veículos de passeio (em 1999);
#     Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#     Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#     Qual a média de veículos nas cinco cidades juntas;
#     Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.


maior_indice = 0
menor_indice = 0

media_veiculos = 0
media_acidentes = 0
soma_veiculos = 0
soma_acidentes = 0
codigo_maior = 0
codigo_menor = 0

for i in range(5):
    codigo = int(input(f"Digite o código da cidade {i+1}: "))

    numero_veiculos = int(input(f"Digite o numero de veículos da cidade {i+1}: "))
    soma_veiculos += numero_veiculos
    numero_acidentes = int(input(f"Digite o numero de acidentes da cidade {i+1}: "))
    
    soma_acidentes += numero_acidentes
    if i == 0:
        maior_indice = numero_acidentes
        menor_indice = numero_acidentes 
        codigo_maior = codigo
        codigo_menor = codigo


    if numero_acidentes > maior_indice:
        maior_indice = numero_acidentes
        codigo_maior = codigo
    
    elif numero_acidentes < menor_indice:
        menor_indice = numero_acidentes
        codigo_menor = codigo

    if i == 4:

        media_veiculos = soma_veiculos / 5
        media_acidentes = soma_acidentes / 5

print(f"Maior indice: {maior_indice} da cidade {codigo_maior}")
print(f"Menor indice: {menor_indice} da cidade {codigo_menor}")


print(f"Media veiculos: {media_veiculos}")
print(f"Media acidentes: {media_acidentes}")
