def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de dois números."""
    if b == 0:
        return "Divisão por zero não é permitida."
    return a / b

def main():
    #Exibe as oções da Calculadora em loop até o usuário querer sair.
    while True:
        print ("\nCalculadora Simples")
        print ("1- Soma")
        print ("2- Subtração")
        print ("3- Multiplicação")
        print ("4- Divisão")
        print ("0- Sair\n")
    
        escolha = input("Digite o número da operação desejada ou '0' se desaja sair: ")
    
        if escolha == '0':
            print("\nDesligando a Calculadora. Até mais!\n")
            break
        a = float(input("\nDigite o primeiro valor: "))
        b = float(input("\nDigite o segundo valor: "))
    
        match escolha:
            case '1':
                resultado = soma(a,b)
                print(f"Resultado: {a} + {b} = {resultado}")
            case '2':
                resultado = subtracao(a,b)
                print(f"Resultado: {a} - {b} = {resultado}")
            case '3':
                resultado = multiplicacao(a,b)
                print(f"Resultado: {a} * {b} = {resultado}")
            case '4':
                resultado = divisao(a,b)
                print(f"Resultado: {a} / {b} = {resultado}")
            case _:
                print("Opção invalida. Por favor, escolha uma das opção validas.")

if __name__ == "__main__":
    main()
# Isso é uma calculadora simples utilizando 'match case' que permite realizar operações básicas como soma, subtração, multiplicação e divisão.
# O usuário escolhe a operação e insere os números, e o programa exibe o resultado.
    