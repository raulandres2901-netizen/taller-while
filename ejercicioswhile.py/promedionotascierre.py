"""

Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99. Muestre la cantidad de notas y
su promedio. El centinela no es una nota y no participa en el cálculo. Si aparece primero, muestre
cantidad cero y «Sin notas» en lugar de un promedio. El flujo siempre contiene -99. El promedio es la
suma de las notas aceptadas dividida entre su cantidad.
Fórmula o relación: Promedio = suma de las notas / cantidad de notas, solo cuando la cantidad sea
positiva.

"""

Cantnotas=0
suma=0
promedio=0

notas = int(input("Digite la nota: "))
Cantnotas=0

if notas !=99:
    while 0<=notas<=100:
        suma=suma+notas
        notas = int(input("Digite la nota: "))
        Cantnotas+=1
        if notas == -99:
            break
    print("cantidad de notas: ",Cantnotas) 
    print("promedio: ",suma/Cantnotas)
else:
    print("cantidad de notas: 0")
    print("sin notas")       