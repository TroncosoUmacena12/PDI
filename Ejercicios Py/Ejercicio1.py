cintura = float(input("Ingrese la circunferencia de la cintura:"))
cadera = float(input("La cadera debe ser positiva. Intente de nuevo:"))
if cintura> 0 and cadera >0: 
    icc = cintura / cadera
    if icc < 0.90:
            riesgo_hombre = "Riesgo bajo"
    elif icc >= 0.90 and icc<= 0.99:
            riesgo_hombre = "Riesgo moderado"
    elif icc > 1.0:
            riesgo_hombre = "Riesgo alto"
    icc = cintura / cadera
    if icc < 0.80:
            riesgo_mujer = "Riesgo bajo"
    elif icc >= 0.80 and icc<= 0.89:
            riesgo_mujer = "Riesgo moderado"
    elif icc > 0.90:
            riesgo_mujer = "Riesgo alto"
genero = input("Ingrese su género (Hombre/Mujer): ").lower()
if genero== "hombre": 
       print(cintura,cadera,icc,riesgo_hombre)
elif genero== "mujer":
       print(cintura,cadera,icc,riesgo_mujer)
else:
       print("Los valores de cadera y cintura tienen que ser positivos")