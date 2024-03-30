ini = 1
valo_conta = []
while ini == 1:
    
    print("BANCO PYTHON")
    print("------------")
    op = int(input("Digite a opção desejada:\n[1] SACAR\n[2] DEPOSITAR\n[3] SAIR\n>> "))
    if op == 1:
        valor_saque = float(input("Digite o valor desejado para saque: "))
        if valor_saque > sum(valo_conta):
            print("Você não possui esse valor em conta!\n Valor disponivel: R$ {}".format(sum(valo_conta))) 
        else:
            novo_total = sum(valo_conta) - valor_saque
            valo_conta.clear()
            valo_conta.append(novo_total)
            print('Saque realizado com sucesso!')
            print("Seu saldo agora é de R$ {}".format(sum(valo_conta)))
            
    elif op == 2:
        valor_deposito = float(input("Digite o valor do deposito!"))
        val_deposit = sum(valo_conta) + valor_deposito
        valo_conta.clear()
        valo_conta.append(val_deposit)
        print("Seu saldo agora é de: R$ {}".format(sum(valo_conta)))
    elif op == 3:
        print("Volte sempre!")
        ini = 0
    else:
        print("Opção inválida!")
   
            
        