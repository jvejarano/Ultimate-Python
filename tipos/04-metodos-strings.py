# definimos la variable "animal" y le asignamos un string
animal = " chanCHIto feliz "
# Método upper para que todo el string se muestre en Mayúsculas
print(animal.upper())
# Método lower para que todo el string se muestre en minúsculas
print(animal.lower())
print(animal.strip().capitalize())  # Método capitalize para que
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("CH"))
print(animal.replace("nCH", "j"))
print("nCH" in animal)
print("nCH" not in animal)
