total = 0
i = 1
print("# Lojas tabajara!")
while True:

    
    preco_prod = float(input(f"Produto {i}: R$ "))
    total += preco_prod

    if preco_prod == 0:
        print(f"Total: R$ {total}")
              
        dinheiro = float(input("Dinheiro: R$ "))
        if dinheiro < total:
            print("Vai lavar louça!")
            break
        troco = dinheiro - total
        print(f"Troco: R$ {troco}")
        break
    else:
        i += 1