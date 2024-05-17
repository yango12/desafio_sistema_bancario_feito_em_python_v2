import desafio_do_banco

def menu():
    menu = """\n
    ================Menu=====================
    [d]\tDepositar
    [s]\tSacar
    [c]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(desafio_do_banco.dedent(menu))
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\nAKZ {valor:.2f}\n"
        print("\nDepósito feito com sucesso!")
    else:
        print("\nValor inválido!")
    
    return saldo, extrato
    
def sacar(* ,saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque > limite_saque
    
    if excedeu_saldo:
        print("\nOperação falhou!Você não tem Saldo insuficiente!")
    
    elif excedeu_limite:
        print("\nOperação falhou! Número máximo de saques excedido.")
    
    elif excedeu_saques:
        print("\nOperação falhou! Limite de saques excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tAKZ {valor:.2f}\n"
    
    else:
    
        print("\nValor inválido!")
    
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n==========Extrato==========")
    print("Não foram realizadas movimentação." if not extrato else extrato)
    print(f"\nSaldo:\t\tAKZ {saldo:.2f}")
    print("===========================================")
def criar_usuario(usuario):
    BI = input("Informe o teu B.I: ")
    usuario = filtrar_usuario(BI,usuario)
    
    if usuario:
        print("\nJá existe usuario com esse BI: ")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço:  ")
    
    usuario.append({'nome': nome, 'data de nascimento': data_nascimento, 'BI': BI, 'Endereço': endereco})
    
    print("Usuário criado com sucesso!")

def filtrar_usuario(BI,usuario):
    usuario_filtrados = [usuario for usuario in usuarios if usuarios['BI'] == BI]
    return usuario_filtrados[0] if usuario_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    BI = input("Informe O BI: ")
    usuario = filtrar_usuario(BI, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {'agencia': agencia, 'numero_de_conta': numero_conta, 'usuario': usuario}
    print("\nUsuario não encontrado, fluxo de criação de conta encerrada!")
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agencia:\t{conta['agencia']}
        c/c:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" + 100)
        print(desafio_do_banco.dedent(linha))
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":""
        
        elif opcao == "s":""
        
        elif opcao == "e": ""
        
        elif opcao == "nu":
            criar_usuario(usuario)
        elif opcao == "nc": 
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                
        
        elif opcao == "lc": 
            listar_contas(contas)
        
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operações desejada.")

main()