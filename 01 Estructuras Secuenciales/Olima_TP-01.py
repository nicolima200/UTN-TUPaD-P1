###   1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("EJERCICIO 1")

print("Hola mundo!") # muestra por pantalla el mensaje.

print() #   salto de línea

###   2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
###   el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
###   por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
###   realizar la impresión por pantalla.
print("EJERCICIO 2")

# Pide al usuario que ingrese un nombre
nombre=input("Por favor ingrese su nombre: ")

# Muestra por pantalla el nombre ingresado
print(f"Hola {nombre}!!")

print() #   salto de línea

###   3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
###   imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
###   “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
###   años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
###   la impresión por pantalla.
print("EJERCICIO 3")

# Pide al usuario que ingrese su nombre, apellido, edad y lugar de residencia.
nombre=input("Por favor ingrese su nombre: ")
apellido=input("Por favor ingrese su apellido: ")
edad=input("Por favor ingrese su edad: ")
lugar=input("Por favor ingrese su lugar de residencia: ")

# Muestra por pantalla la frase con los datos ingresados.
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

print() #   salto de línea

###   4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
###   su perímetro.

print("EJERCICIO 4")

# Definimos el valor de pi
pi=3.14159

# Se pide al usuario que ingrese el valor del radio
radio=float(input("Ingrese el radio de un círculo: "))

# Se calculan area y perimetro con el valor de pi y el valor ingresado
# por el usuario.
area= pi*radio*radio
perimetro= 2*pi*radio


# Se imprimen por pantalla los resultados.
print(f"Area del círculo de radio {radio}: {area:.2f}")
print(f"Perímetro del círculo de radio {radio}: {perimetro:.2f}")

print() #   salto de línea

###   5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
###   cuántas horas equivale.

print("EJERCICIO 5")

# Se pide al usuario que ingrese una valor en segundos.
segs=int(input("Ingrese segundos: "))

# Se calcula y se muestra por pantalla.
print(f"Equivale a {segs/3600} horas.")

print() #   salto de línea

###   6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
###   multiplicar de dicho número.

print("EJERCICIO 6")

# Se pide al usuario que ingrese un número.
num=int(input("Ingrese un número: "))

# Mediante un for imprimimos el producto entre el número ingresado y el valor
# de la variable de control i.
for i in range(1,11):
    print(f"{num}x{i} = {num*i}")

print() #   salto de línea

###   7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
###   pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("EJERCICIO 7")

# Se pide ingresar dos números enteros.
num1=int(input("Ingrese el primer número entero: "))
num2=int(input("Ingrese el segundo número entero: "))

# Se imprime el resultado de las operaciones entre los
# dos números ingresados.
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")

print() #   salto de línea

###   8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
###   de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
###   modo:
###   𝐼𝑀𝐶 =   𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 /((𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2)"

print("EJERCICIO 8")

# Se pide al usuario que ingrese su altura y su peso.
alt=float(input("Ingrese su altura: "))
peso=float(input("Ingrese su peso: "))

# Calculamos y almacenamos el imc.
imc=peso/(alt**2)

# Se muestra por pantalla el IMC con 2 decimales.
print(f"IMC= {imc:.2f}")

print() #   salto de línea

###   9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
###   pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
###   𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

print("EJERCICIO 9")

# Se pide al usuario que ingrese una temperatura en celsius
# y la almacenamos en la variable t.
t=float(input("Ingrese temperatura en celsius: "))

# Calculamos y convertimos a fahrenheit con la fórmula
# y almacenamos el resultado en f.
f= 9/5* t +32

# Se muestra por pantalla la temperatura en celsius y su equivalente en
# fahrenheit.
print(f"{t:.0f}°C = {f:.0f}°F")

print() #   salto de línea

###   10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
###   dichos números.

print("EJERCICIO 10")

# Se pide al usuario que ingrese 3 números.
n1=float(input("Ingrese el primer número: "))
n2=float(input("Ingrese el segundo número: "))
n3=float(input("Ingrese el tercer número: "))

# Se calcula y se imprime por pantalla.
print(f"PROMEDIO= {(n1+n2+n3)/3}")

print() #   salto de línea

#   prueba git