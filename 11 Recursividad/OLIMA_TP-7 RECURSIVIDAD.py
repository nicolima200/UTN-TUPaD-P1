# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# print("CALCULADORA FACTORIALES DESDE 1 HASTA 'n':\n")

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# n=int(input("Ingrese el valor de 'n':"))
# for i in range(1,n+1):
#     print(f"{i}! = ",factorial(i))

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

# print("\nCALCULADORA FIBONACCI:")

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# n=int(input("Ingrese una posición de la serie Fibonacci: "))

# for i in range(n+1):
#     print(f"Posición {i} =",fibonacci(i))

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛 ^(𝑚−1).
# Prueba esta función en un algoritmo general.

# print("\nPOTENCIA RECURSIVA UTILIZANDO 𝑛^𝑚 = 𝑛 ∗ 𝑛 ^(𝑚−1)")

# def potencia_recursiva(n,m):
#     if n==0:
#         return 0
#     elif m==0:
#         return 1
#     else:
#         return n*potencia_recursiva(n,m-1)
    
# print(potencia_recursiva(5,3))

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

# print("\nDECIMAL A BINARIO COMO STRING")

# def dec_a_bin(n):
#     if n==1:
#         return "1"
#     if n==0:
#         return "0"
#     else:
#         return dec_a_bin(n//2) + str(n%2)
        
# print(str(dec_a_bin(10)))

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# print("\nPALÍNDROMO")

# def es_palindromo(palabra):
#     if len(palabra)<=1:
#         return True
#     if palabra[0]!=palabra[-1]: # Compara el primer elemento contra el último
#         return False # Si son diferentes, no es palíndromo.
#     else: # De lo contrario, retorna la cadena sin los caracteres ya comparados, para continuar con
            # los siguientes caracteres.
#         return es_palindromo(palabra[1:-1])

# print(es_palindromo("anilina"))

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

# print("\nSUMA DÍGITOS")

# def suma_digitos(n):
#     if n<10:
#         return n
#     else:
#         return suma_digitos(n//10)+n%10 # Al hacer n%10, separamos la parte de unidades del número.
                                          # Al hacer n//10 obtenemos las decenas restantes para seguir operando.
# n=int(input("Ingrese un número entero positivo: "))
# print(suma_digitos(n))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# print("\nCONTAR BLOQUES")

# def contar_bloques(n):
#     if n==1:
#         return 1
#     else:
#         return contar_bloques(n-1)+n # Sumamos cada vez la cantidad de bloques menos 1.

# n=int(input("Ingrese el número de bloques del nivel más bajo de la pirámide: "))
# print("Cantidad de bloques necesarios: ", contar_bloques(n))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0 

print("\nCONTAR DIGITO")

def contar_digito(n,d):
    if n==d: # Si el dígito es igual al número, aparece 1 vez.
        return 1
    if n//10 == 0: # Si la operacion es igual a cero, significa que el dígito es menor a 10. Por lo que solo se necesita una comprobación, que ya fue hecha en el condicional anterior.
        return 0
    else:
        #print(f"n//10 = {n//10} \nn % 10= {n%10}")
        #print(f"(n%10) == d = {(n%10) == d}")
        return contar_digito(n//10,d)+ (1 if ((n%10) == d) else 0) # El resto de dividir por 10 nos da una cifra para comparar con el dígito ingresado.
    
n=int(input("Ingrese un número: "))
d=int(input("Ingrese un dígito: "))

print(f"El dígito {d} aparece ", contar_digito(n,d),f"veces en el número {n}")