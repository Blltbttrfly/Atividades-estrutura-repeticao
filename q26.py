
#26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

lula = 0
flavio = 0
padre = 0
opcao = 0
eleitores_total = int(input("Digite o total de eleitores: "))

print("""
NUMEROS DOS CANDIDATOS:
      Lula | 13
      FLavio | 666
      Padre | 999 
""")
for i in range(eleitores_total):
     while True:
        opcao = int(input("Insira na urna o seu voto: "))
        if opcao == 13:
                lula += 1
                break
        elif opcao == 666:
                flavio += 1
                break
        elif opcao == 999:
                padre += 1
                break
        else:
            print("Opcao invalida! Digite novamente.")


print(f"""
| Resultados |
Lula: {lula}
Flavio: {flavio}
padre: {padre}
""")
