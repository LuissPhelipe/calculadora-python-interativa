import math

print("=== CALCULADORA PYTHON ===")

while True:
    # Escolher operação
    print("\nSelecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Saindo da calculadora. Até mais!")
        break

    if opcao not in ['1', '2', '3', '4', '5', '6']:
        print("Opção inválida. Por favor, escolha uma opção entre 0 e 6.")
        continue

    # Receber números
    try:
        num1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue

    num2 = None # Initialize num2
    if opcao != "6": # Only ask for num2 if it's not a square root operation
        try:
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

    # Fazer cálculo
    if opcao == "1":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")

    elif opcao == "2":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")

    elif opcao == "3":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")

    elif opcao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Não é possível dividir por zero.")

    elif opcao == "5":
        resultado = num1 ** num2
        print(f"Resultado: {resultado}")

    elif opcao == "6":
        if num1 >= 0:
            resultado = math.sqrt(num1)
            print(f"Resultado: {resultado}")
        else:
            print("Não é possível calcular a raiz quadrada de um número negativo (em números reais).")
