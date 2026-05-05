# 45. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A

# 02 - B

# 03 - C

# 04 - D

# 05 - E

# 06 - E

# 07 - D

# 08 - C

# 09 - B

# 10 - A

questoes_certas= 0
maior_acertos = float("inf")
nome_maior_acertos = ""
menor_acertos = float("inf")

while True:

    questoes_certas = 0
    nome = input("Digite sue nome: ")

    q1 = input("Digite a resposta da questao (A, B, C, D ou E): ")
    if q1 == "A":
        questoes_certas += 1

    q2 = input("Digite a resposta da questao (A, B, C, D ou E): ")
    if q2 == "B":
        questoes_certas += 1

    q3 = input("Digite a resposta da questao (A, B, C, D ou E): ")
    if q3 == "C":
        questoes_certas += 1

    q4 = input("Digite a resposta da questao (A, B, C, D ou E): ")
    if q4 == "D":
        questoes_certas += 1

    q5 = input("Digite a resposta da questao (A, B, C, D ou E): ")
    if q5 == "E":
        questoes_certas += 1
    
    print(f"Total de acertos: {questoes_certas}")
    print(f"Nota: {((questoes_certas/5) * 10):.1f}")






