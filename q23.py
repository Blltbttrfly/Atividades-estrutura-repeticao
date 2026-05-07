# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.


# numeroN = int(input("Digite um número N: "))
# operacoes = 0
# for i in range(2, numeroN + 1):
#     primo = True

#     for j in range(2, i//2):
#         operacoes += 1
#         if i % j == 0:
#             primo = False
#             break
    
#     if primo:
#         print(i)
# print(operacoes)





# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input("Digite um número inteiro: "))
operacoes = 0

for n in range(1, numero+1):
    primo = True

    for i in range(2, int(i**0.5) + 1):
        operacoes += 1
        if n % i == 0:
            primo = False
            break
    
    if primo:
        print(f"{n} é primo!")
    else:
        print(f"{n} não é primo!")


print(f"FORAM USADAS {operacoes} operações")