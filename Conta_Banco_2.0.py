menu = """
[1] Criar Usuário
[2] Criar Conta Corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Pagar Fatura
[7] Solicitar Cartão de Crédito
[8] Solicitar Empréstimo
[9] Sair

=> """

def pagar_fatura(conta):
    valor = float(input("Informe o valor da fatura a ser paga: "))
    if valor > 0 and valor <= conta["saldo"]:
        conta["saldo"] -= valor
        conta["extrato"] += f"Pagamento de Fatura: R$ {valor:.2f}\n"
        print("Fatura paga com sucesso!")
    else:
        print("Falha no pagamento! Verifique o saldo ou o valor informado.")

def solicitar_cartao_credito(usuario):
    print(f"Solicitação de cartão de crédito para {usuario['nome']} realizada com sucesso!")
    print("Aguarde a análise de crédito.")

def solicitar_emprestimo(conta):
    valor = float(input("Informe o valor do empréstimo desejado: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Empréstimo Recebido: R$ {valor:.2f}\n"
        print("Empréstimo aprovado e valor creditado na conta!")
    else:
        print("Falha na solicitação! O valor informado é inválido.")

# Initialize required variables
usuarios = []
contas = []

# Define missing functions
def criar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário (dd/mm/aaaa): ")
    endereco = input("Informe o endereço do usuário: ")
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

def criar_conta_corrente(usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"numero": numero_conta, "usuario": usuario, "saldo": 0, "extrato": ""})
        print(f"Conta corrente {numero_conta} criada com sucesso!")
    else:
        print("Usuário não encontrado!")

def selecionar_conta(contas):
    numero_conta = int(input("Informe o número da conta: "))
    conta = next((c for c in contas if c["numero"] == numero_conta), None)
    if conta:
        return conta
    else:
        print("Conta não encontrada!")
        return None

def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito!")

def sacar(conta, valor, limite):
    if valor > 0 and valor <= conta["saldo"] and valor <= limite:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
    else:
        print("Falha no saque! Verifique o saldo, limite ou valor informado.")

def exibir_extrato(conta):
    print("\n=== Extrato ===")
    print(conta["extrato"] if conta["extrato"] else "Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("================\n")

while True:
    opcao = input(menu)

    if opcao == "1":
        criar_usuario(usuarios)

    elif opcao == "2":
        criar_conta_corrente(usuarios, contas)

    elif opcao == "3":
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            depositar(conta, valor)

    elif opcao == "4":
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Informe o valor do saque: "))
            sacar(conta, valor, limite=500)

    elif opcao == "5":
        conta = selecionar_conta(contas)
        if conta:
            exibir_extrato(conta)

    elif opcao == "6":
        conta = selecionar_conta(contas)
        if conta:
            pagar_fatura(conta)

    elif opcao == "7":
        cpf = input("Informe o CPF do usuário: ")
        usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
        if usuario:
            solicitar_cartao_credito(usuario)
        else:
            print("Usuário não encontrado!")

    elif opcao == "8":
        conta = selecionar_conta(contas)
        if conta:
            solicitar_emprestimo(conta)

    elif opcao == "9":
        print("Obrigado por utilizar nosso sistema bancário!")
        break

    else:
        print("Operação inválida! Tente novamente.")
