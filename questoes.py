#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome_de_usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

    if nome_de_usuario == senha:
        print("ERRO: usuario e senha nao podem ser os mesmos.")
        continue

    print("Voce esta cadastrado!")
    break


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



#8. Faça um programa que leia 5 números e informe a soma e a média dos números.

#9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

#4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

#5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

#26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

#31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# #Lojas Tabajara

# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00

