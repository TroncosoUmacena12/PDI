ccadena = input("Ingresa una cadena: ")
contador = 0
suma = 0
digitos = []
for caracter in ccadena:
    if caracter.isdigit():
        digito = int(caracter)
        contador += 1
        digitos.append(digito)
        suma += digito
if contador > 0:
    print("Cantidad de dígitos =", contador)
    print("Dígitos =", " ".join(str(d) for d in digitos))
    print("Suma =", suma)
else:
    print("No existen dígitos")