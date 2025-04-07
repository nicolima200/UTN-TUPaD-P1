### ATENCIÓN!!!
### Al final del documento 
### se encuentran las llamadas
### a las funciones


# # # 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# # # (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

def actividad1():
    print("EJERCICIO 1\n")

    for i in range(1,101):
        print(i)

# # # 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# # # dígitos que contiene.

def actividad2():
    print("EJERCICIO 2\n")

    # Solicitamos al usuario que ingrese un número entero.
    num=input("Ingrese un número entero: ")

    try:
        # Intentamos convertir el string num a entero, si es válido, continúa
        # Si no es posible, se da una excepción y termina el programa.
        int(num) 

        if int(num) >= 0: # Verificamos si el número es positivo
            print("El número ingresado tiene ", len(num),"dígitos")
        else: 
            # Si el número es negativo, restamos 1 a la longitud del número, ya que
            # no queremos considerar el símbolo - (menos) como dígito.
            print("El número ingresado tiene ", len(num)-1,"dígitos")

    except ValueError:
        print("El número ingresado no es un número entero.")



# # # 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# # # dados por el usuario, excluyendo esos dos valores.

def actividad3():
    print("EJERCICIO 3\n")

    try:
        menor=int(input("Ingrese un número: "))
        mayor=int(input("Ingrese otro número: "))
        suma=0

        # Verificamos si los valores de las variables coinciden con los nombres
        # para facilitar su uso en el for.

        if menor > mayor:
            menor, mayor = mayor, menor # Si no coinciden, intercambiamos los valores

        for i in range (menor+1, mayor): # Recorremos los números enteros comprendidos entre los dos ingresados.
            suma+=i # Acumulamos la suma.

        print("Suma de los números comprendidos entre {menor} y {mayor}= ", suma)
    except ValueError:
        print("No es un número entero.")



# # # 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# # # secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# # # un 0.

def actividad4():
        
    print("EJERCICIO 4\n")

    suma=0

    try:
        num=int(input("Ingrese un número entero: ")) # Intentamos convertir la cadena ingresada a entero.
        while num != 0: # Se ejecuta mientras el usuario no ingrese 0.
            suma+=num
            num=int(input("Ingrese un número entero: "))
    # Si la conversión de la cadena a entero falla, el programa ejecuta el código de excepción y sale del try
    except ValueError: 
        print("Debe ingresar un número entero")

    print("Acumulado: ", suma)



# # # 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# # # programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

def actividad5():

    import random # Importamos 

    print("EJERCICIO 5\n")

    nAleatorio=random.randint(0,9)
    contador=0
    num=10

    try:
        while num != nAleatorio:
            num=int(input("Adivine el número: "))
            contador+=1

        print("*** ¡ACERTASTE! ***")
        print("El número es: ", nAleatorio)
        print("Intentos ",contador)

    except ValueError:
        print("El valor no es un número entero. Adiós.")



# # # 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# # # entre 0 y 100, en orden decreciente.

def actividad6():
    print("EJERCICIO 6\n")

    for i in range(100,0,-2):
        print(i)



# # # 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# # # número entero positivo indicado por el usuario.

def actividad7():
    print("EJERCICIO 7\n")
    suma=0

    try:
        num=int(input("Ingrese un número: "))
        if num > 0:
            for i in range(0,num):
                suma+=i
            print("Suma: ", suma)
        else:
            print("No es un número positivo.")
    except ValueError:
        print("No es un número entero.")



# # # 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# # # programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# # # negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# # # menor, pero debe estar preparado para procesar 100 números con un solo cambio).

def actividad8():
    print("EJERCICIO 8\n")

    pares=0
    impares=0
    positivos=0
    negativos=0
    cantNumeros=100

    try:
        for i in range(0,cantNumeros):
            num=int(input("Ingrese un número entero: "))
            if num % 2 ==0: # Calculamos módulo de num entre 2 para saber si es par
                pares+=1
            else:
                impares+=1
            if num > 0:
                positivos+=1
            elif num < 0:
                negativos+=1

        print("Pares: ",pares)
        print("Impares: ", impares)
        print("Positivos: ", positivos)
        print("Negativos: ", negativos)
    except ValueError:
        print("No es un entero.")



# # # 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# # # media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# # # poder procesar 100 números cambiando solo un valor).

def actividad9():
    print("EJERCICIO 9\n")

    cantNumeros=100
    suma=0

    try:
        for i in range(0,cantNumeros):
            num=int(input("Ingrese un número entero: "))
            suma+=num
        
        print("PROMEDIO: ", suma/cantNumeros)
    except ValueError:
        print("El número no es un entero. Chau.")



# # # 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# # # usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

def actividad10():
    print("EJERCICIO 10\n")

    try:
        num=input("Ingrese un número: ")

        if float(num):
            print("válido")
            for i in range(len(num)-1, -1, -1):
                print(num[i], end="")
    except ValueError:
        print("Se esperaba un número.")


actividad1()
actividad2()
actividad3()
actividad4()
actividad5()
actividad6()
actividad7()
actividad8()
actividad9()
actividad10()