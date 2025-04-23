w = float(input("Ingrese la carga uniformemente distribuida en kN/m: "))
l = float(input("Ingrese la alongitud de la viga en metros: "))
M=w*(pow(l, 2))/8
fc=float(input("Ingrese la resistencia a la flexion del ormigon: "))
fy=float(input("Ingrese el acero de refuerzo: "))
b=300 
d=(M/(0.9*fc*b))**0.5
As=M/(0.9*d*fy)
print("Profundidad requerida (d):", d)
print("Área requerida (As):", As)