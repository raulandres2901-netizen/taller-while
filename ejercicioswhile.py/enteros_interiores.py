"""

Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores».
Fórmula o relación: Cada entero consecutivo difiere del anterior en 1.

"""

A=int(input("Digite el entero A:"))
B=int(input("Digite el entero B:"))

while A < B:
    for i in range(A+1, B):
        print(i)
    break

while A+1 == B:
    print("No hay enteros interiores")
    break