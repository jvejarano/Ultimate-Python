def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    # OJO la identacion de este "print" si hay un tab + sumaria mal, OJO
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
