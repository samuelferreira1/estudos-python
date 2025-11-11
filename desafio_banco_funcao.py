menu= """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def menu_opcoes():
    while True:
        opcao = input(menu).lower().strip()
        return opcao
    
def depositar(saldo, extrato):
    print("Depósito")
    valor_deposito = float(input("Quanto você deseja depositar? "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    print(f"Foi realizado um novo depósito de R$ {valor_deposito:.2f}. Seu saldo atual é R$ {saldo:.2f}")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    print("Saque")  
    valor_saque = float(input("Quanto você deseja sacar? "))
    if saldo >= valor_saque > 0:
        if numero_saques < LIMITE_SAQUES:
            if valor_saque <= limite:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Foi realizado um novo saque de R$ {valor_saque:.2f}. Seu saldo atual é R$ {saldo:.2f}")
            else:
                print("Operação falhou! O valor do saque excede o limite.")
        else:
            print("Operação falhou! Número máximo de saques diários excedido.")
    
def exibir_extrato(extrato):
    print("Extrato")
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)

def sair():
    print("Saindo... Obrigado por usar nosso sistema bancário!")
while True:
    opcao = menu_opcoes()           
    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
    
    elif opcao == "e":
        exibir_extrato(extrato)     

    elif opcao == "q":
        sair()          
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

