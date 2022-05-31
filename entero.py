from math import factorial


print("---------------------------------------")
print("----------calcular factorial-----------")
print("---------------------------------------")


#Input

X = int(input("Ingrese el numero: "))
Y = X

#Procesing

if X <0:
    print("El numero ingresado es negativo, ingrese uno positivo.")

else: 

    N = 1
    while X != 0:
        N = N * X
        X = X -1

#Output

    print("El numero factorial del entero positivo es: " + str(N) + (" y el numero ingresado es: " + str(Y))) 