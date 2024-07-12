def q1():
    contador = 0
    numero = int(input(""))
    for i in range(1, numero + 1):
        if (numero % i == 0) and (i % 3 == 0):
                contador += 1
    if contador == 0:
        print(f'O número não possui divisores multiplos de 3')
    else:
        print(f'Quantidade de divisores divisiveis por 3:', contador)

def q2():
    menor = int(input(""))
    maior = int(input(""))
    soma = 0
    if menor > maior:
        n1 = menor
        menor = maior
        maior = n1
    for i in range(menor, maior + 1):
        if i > 0 :
            soma += i
    print(soma)


def q3():
    
    pass

def q4():
    pass