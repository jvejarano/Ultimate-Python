def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


# es_palindromo("amo la paloma")
# es_palindromo("hola mundo")

# Es palindromo o no???? #
print(es_palindromo("Amo la Paloma"))
print(es_palindromo("Hola Mundo"))
print(es_palindromo("Reconocer"))
print(es_palindromo("Isaac no ronca asi"))


# print("Abba", es_palindromo("Abba"))
# print("Reconocer", es_palindromo("Reconocer"))
# print("Amo la paloma", es_palindromo("Amo la paloma"))
# print("Hola mundo", es_palindromo("Hola mundo"))
