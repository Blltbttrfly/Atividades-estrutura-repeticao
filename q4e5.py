
#4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.



cidade_a = float(input("Digite a população inicial da cidadade a: "))
cidade_b = float(input("Digite a população inicial da cidadade b: "))
taxa_a = float(input("Digite a taxa da cidade a (decimal): "))
taxa_b = float(input("Digite a taxa da cidade b (decimal): "))
anos = 0

while True:
    if cidade_a >= cidade_b:
        anos += 1
        print(anos)
        print(cidade_a, cidade_b)
        break
    else:
        cidade_a += cidade_a * taxa_a
        cidade_b += cidade_b * taxa_b
    anos += 1
