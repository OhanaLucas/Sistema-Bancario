saldo, limite, numero_saques = 0, 500, 0
extrato = ""
LIMITE_SAQUES = 3

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

while True:
    option = input(menu)
    match option:
        case "d":
          valor = float(input("Quanto deseja depositar? \n=>"))
          if valor > 0:   
            saldo += valor
            extrato += f"Depósito: R${valor: .2f}\n"
          else:
             print("Operação Falhou! \nO valor informado não é válido.")
        case "s":
          if numero_saques < LIMITE_SAQUES:
            valor = float(input("Quanto deseja sacar? \n=>"))
            if valor > 0:   
                if valor <= limite:
                    if valor < saldo:
                        saldo -= valor
                        extrato += f"Saque: R${valor: .2f}\n"
                        numero_saques += 1
                    else:
                        print(f"Saldo Insuficiente! \nO valor ultrapassa o saldo atual de R$ {saldo: .2f}")
                else:
                    print(f"Limite Excedido! \nO valor ultrapassa o limite atual de R$ {limite: .2f}")
            else:
                print("Operação Falhou! \nO valor informado não é válido.")
          else:
            print("Limite de saques diários excedido!")
        case "e":
          print(' EXTRATO '.center(50,'*'))
          if extrato:
            print(f"{extrato}\nSaldo: R${saldo: .2f}")
          else:
             print(f"Não foram realizadas movimentações.\nSaldo: R${saldo: .2f}")
          print("*"*50)
        case "q":
            break
        case default:
            print("Operação inválida, por favor selecione novamente a operação desejada.")