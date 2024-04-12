def no_space(texto):  # Recibe el parametro 'texto' y lo reemplaza para que no tenga espcios 'no space'

    nuevo_texto = ""  # Ojo la identacion en este codigo, siempre verificar
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def es_palindromo(texto):
    texto = no_space(texto)
    print(texto)


es_palindromo("Amo la paloma")


# print("Abba", es_palindromo("Abba"))
# print("Reconocer", es_palindromo("Reconocer"))
# print("Amo la paloma", es_palindromo("Amo la paloma"))
# print("Hola mundo", es_palindromo("Hola mundo"))
