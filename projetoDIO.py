menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
        opcao = input(menu)

        if opcao == 'd':
                print ("Depósito")
                valor_positivo = input( "Digite o valor desejado para depósito: ")    
                if int(valor_positivo) >= 0: 
                        print ('Depósito Realizado')
                        saldo += int(valor_positivo)
                        extrato += f"Depósito: R$ {valor_positivo}\n"
                else:
                        print ('Depósito Invalido')



        elif opcao == 's':
                
                print ('Saque')
                valor_saque = float(input( "Digite o valor desejado para sacar: ")  )
                limite_valor = int(valor_saque) > limite
                valor_saldo = int(valor_saque) > saldo 
                limite_diario = numero_saque >= LIMITE_SAQUES


                if limite_valor :
                        print("O limite para saques é de 500 reais, saque não realizado")

                elif valor_saldo:
                        print ("Valor não disponivel na conta, saque não realizado")

                elif limite_diario:
                        print ("Você atingiu seu limite diario de saques, saque não realizado")
                elif valor_saque > 0:
                        saldo -= int(valor_saque)
                        extrato += f"Saque: R$ {valor_saque:.2f}\n"
                        numero_saque += 1
                else:
                        print ("Saque não realizado")
                        

        elif opcao == 'e' :
                print ("Não foram realizadas movimentações." if not extrato else extrato ) 
                print (f'Seu é extrato: {extrato}')
                       
        elif opcao == 'q':
                break
        else:
                print ('Operação inválida, por favor selecione novamente a operação desejada')
