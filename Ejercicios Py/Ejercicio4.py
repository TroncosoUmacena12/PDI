m = int(input("Ingrese el valor entero de m: "))
A = 0
for i in range(1, m + 1):
    A += 2 ** (-i)
print(f"A = {A:.2f}")

p = int(input("Ingrese el valor entero de p: "))
AA = 0
if p <= m:
 print("Error: p debe ser mayor que m.")
else:
    for i in range(1, m + 1):
        for j in range(m + 1, p + 1):
            valor = 2 * (-i) + 2 * j
            AA += valor
print("AA =", AA)

q = int(input("Ingrese el valor entero de q: "))
AAA = 0
if q <= p:
    print("Error: q debe ser mayor que p.")
else:
    for i in range(1, m + 1):
        for j in range(m + 1, p + 1):
            for k in range(p + 1, q + 1):
                valor = 2 * (-i) - 2 * j + k
                AAA += valor
print(f"AAA = {AAA:.3f}")