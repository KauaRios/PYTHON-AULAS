while True:
    print("voce esta no 1 laço")
    opcao1 = input("Digite 1 para continuar ou 0 para sair: \n") 
    if opcao1 == '0':
        break
    else:
        while True:
            print("voce esta no 2 laço" )
            opcao2 = input("Digite 1 para continuar ou 0 para sair: \n")
            if opcao2 == '0':
                break
        print("Saindo do segundo laço...")
print("Saindo do primeiro laço...")
