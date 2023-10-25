# Elabore un algoritmo que reciba del usuario dos numeros y le indique si el primero numero es divisible por el segundo numero.

numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))

if numeroUno % numeroDos == 0:
    print("El primer numero es divisible por el segundo numero.")
else:
    print("El primer numero no es divisible por el segundo numero.")
