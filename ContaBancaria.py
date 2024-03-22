import time
from datetime import datetime
contas = []
data = datetime.now()
data_formatada = data.strftime("%d/%m/%y - %H:%M")
while True:
    opcao = int(input("1 - Criar Conta\n2 - Acessar Conta\n"))
    
    if opcao == 1:
        cad_nome = input("\nInforme seu nome. Para cancelar digite 0 : ")
        if cad_nome == '0':
            continue
        
        cad_cpf = input("\nInforme seu CPF: ")
        
        verif_cpf = False
        
        for conta in contas:
            if conta['cpf'] == cad_cpf:
                verif_cpf = True
                break
        if verif_cpf:
            print("CPF ja cadastrado. Por favor, insira um CPF diferente.\n")
            continue
        
        if len(cad_cpf) != 11 or not cad_cpf.isdigit():
            print("CPF inválido. Por favor, insira um CPF válido\n")
            continue
        while True:
                cad_senha1 = input("Crie sua senha: ")
                cad_senha2 = input("Confirme sua senha: ")

                if cad_senha1 == cad_senha2:
                    cad_senha = cad_senha1
                    break
                else:
                    print("As senhas não correspondem. Por favor, tente novamente.\n")

        contas.append({"nome": cad_nome, "cpf": cad_cpf, "senha": cad_senha, "operacoes":[], "saldo": [], "data": data_formatada})
        time.sleep(1)
        print("Conta criada com sucesso!\n")
        time.sleep(0.5)
        

    elif opcao == 2:
        inf_cpf = input("Informe Seu cpf: ")
        time.sleep(0.5)

        buscar_conta = None
        for conta in contas:
            if conta["cpf"] == inf_cpf:
                buscar_conta = conta
                break
            
        if buscar_conta is None:
            print("CPF não encontrado. Por favor, abra uma conta.")
            continue
        
        while True:
            buscar_senha = None
            inf_senha = input("Isira sua senha: ")

            for senha in contas:
                if conta['senha'] == inf_senha:
                    buscar_senha = conta
                    break
            if buscar_senha is None:
                    print("Senha inválida!!!\n")
            else:
                print("\nAcesso autorizado!\n")
                time.sleep(0.8)
                break

        while True:
                saldo_anterior = 0
                print(f"Olá Sr(a). {buscar_conta['nome'].title()}\n") 
                new_option = int(input("1 - Deposito\n2 - Saque\n3 - Saldo\n4 - Extrato\n5 - Voltar\n"))

                if new_option == 1:
                    deposito = float(input("\nInsira o valor do deposito R$"))
                    saldo_anterior -= deposito
                    time.sleep(1)
                    buscar_conta["operacoes"].append(f"{data_formatada}------------------ +R${deposito:.2f}")
                    buscar_conta['saldo'].append(deposito) 
                    print(f"\nDeposito de R${deposito:.2f} realizado com sucesso!\n")
                    time.sleep(0.5)

                elif new_option == 2:
                    print(f"\nSaldo atual: R${sum(buscar_conta['saldo']):.2f}\n\n")
                    saque = float(input("\nValor do saque R$"))
                    saldo_anterior += deposito
                    time.sleep(1)
                    
                    if sum(buscar_conta['saldo']) >= saque:
                        
                        buscar_conta["operacoes"].append(f"{data_formatada}------------------ -R${saque:.2f}")
                        buscar_conta['saldo'].append (-saque)
                        time.sleep(1)
                        print(f"\nSaque de R${saque:.2f} realizado com sucesso!")
                        time.sleep(0.5)                        
                        
                    else:
                        print("\nSaldo insuficiente para realizar o saque\n")
                        time.sleep(0.5)

                elif new_option == 3:
                    print(f"Saldo atual: R${sum(buscar_conta['saldo']):.2f}\n")

                elif new_option == 4:
                    print("\n-------\nExtrato:\n-------\n")
                    print(f"Saldo anterior:     R${saldo_anterior:.2f}\n")
                    
                    for i in buscar_conta["operacoes"]:
                        print(i)
                    print(f"\nSaldo atual: ------ R${sum(buscar_conta['saldo']):.2f}\n")
                    print("----------------------------------------------------------")
                
                elif new_option == 5:
                    break
                
                else: 
                    print("\nEntrada Inválida!\n")
    else:
        print("\nOpção inválida. Por favor, escolha entre as opções 1 ou 2.\n")
