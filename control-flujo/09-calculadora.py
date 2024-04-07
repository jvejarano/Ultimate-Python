print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, multi, div y resta")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa la operación a realizar: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa un segundo número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida")
        break

print(f"El resultado es {resultado}")
