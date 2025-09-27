def deposito(conta):
    """
    Efetua um depósito ao saldo de uma conta e salva a operação efetuada no extrato.

    Args:
        conta (dict): Dict dados da conta

    Returns:
        bool: True operação realizada com sucesso, False falha
    """
    entrada = input("Digite o valor para depósito:").strip().lower()

    # verifica se entrada é cancelar
    if entrada == 'c':
        print(f"Operação cancelada")
        return False

    # prepara a entrada para verificação das condições.
    VALOR_MINIMO = 0.01
    entrada = entrada.replace(',', '.') # substitui virgula por ponto.
    valor_deposito = float(entrada)
    valor_deposito = round(valor_deposito, 2) # arredonda para 2 casas decimais.

    # verifica se o valor é valido.
    if valor_deposito >= VALOR_MINIMO:
        # atualiza o saldo da conta
        conta["saldo"] += valor_deposito
        # registra a operação
        conta["extrato"] += f"Depósito R${valor_deposito:.2f}\n"
        return True
    else:
        print(f"valor inválido")
        return False

def saque(conta):
    """
    Efetua um saque da conta informada
    verificação para efetuar o saque:
    - valor deve ser positivo e maior que zero.
    - valor deve ser menor ou igual ao limite de ooperação.
    - saques disponiveis deve ser maior que zero.

    Args:
        conta (dict): Dict dados da conta

    Returns:
        bool: True operação realizada com sucesso, False falha
    """
    # solicita o valor para a operação saque.
    entrada = input("Digite o valor para saque:").strip().lower()

    # verifica se entrada é cancelar
    if entrada == 'c':
        print(f"Operação cancelada")
        return False

    # prepara a entrada para verificação das condições.
    VALOR_MINIMO = 0.01
    entrada = entrada.replace(',', '.') # substitui virgula por ponto.
    valor_saque = float(entrada)
    valor_saque = round(valor_saque, 2) # arredonda para 2 casas decimais.

    # verifica se o valor é valido.
    if valor_saque >= VALOR_MINIMO:
        # verifica se há saques disponiveis.
        if conta["saques"]:
            # verifica se o valor de saque é menor ou igual ao limite de saque permitido.
            if valor_saque > conta["limite"]:
                print(f"Valor de saque maior que o limite permitido!")
                return False
            
            # verifica se o valor de saldo é suficiente para a efetuar a operação saque.
            conta_saldo = conta["saldo"]
            if conta_saldo < valor_saque:
                print(f"Saldo insuficiente!")
                return False
            
            # desconta o valor de saque do saldo em conta.
            conta_saldo -= valor_saque
            
            # registra a operação e atualiza o contador de saques.
            conta["extrato"] += f"Saque R${valor_saque:.2f}\n"
            conta["saldo"] = conta_saldo
            conta["saques"] -= 1

            # informa a operação realizada.
            print(f"Saque efetuado R$:{valor_saque}")
        else:
            print(f"Quantidade de saques esgotados")
            return False
    else:
        print(f"valor inválido")
        return False

def extrato(conta):
    """
    Exibe o extrato de transações efetuadas na conta

    Args:
        conta (dict): Dict dados da conta
    """
    print(f"\n=========EXTRATO=========")
    print(f"{conta["extrato"]}")
    print(f"Saldo:{conta["saldo"]:.2f}")
    print(f"===========FIM===========")
    return

if __name__ == "__main__":
    menu = """\n[d:Depósito, s:Sacar, e:Extrato, q:sair] :"""
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_UNICO = 500
    conta = {"saldo":0, "saques":LIMITE_SAQUES, "limite":LIMITE_SAQUE_UNICO, "extrato":""}
    
    while True:

        opcao = input(menu)
        if opcao == "d":
            deposito(conta)

        elif opcao == "s":
            saque(conta)

        elif opcao == "e":
            extrato(conta)

        elif opcao == "q":
            print("Sair")
            break