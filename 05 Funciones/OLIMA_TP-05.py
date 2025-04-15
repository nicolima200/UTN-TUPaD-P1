# # # 1. Crear una función llamada imprimir_hola_mundo que imprima por
# # # pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# # # programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")

# # # 2. Crear una función llamada saludar_usuario(nombre) que reciba
# # # como parámetro un nombre y devuelva un saludo personalizado.
# # # Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# # # principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# # # 3. Crear una función llamada informacion_personal(nombre, apellido,
# # # edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# # # [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# # # 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    pi=3.1416 #Guardamos el valor del número pi en una variable y utilizamos 4 decimales.
    area= pi * radio ** 2 #Fórmula para calcular el área de un círculo
    print(f"El área es: {area}")

def calcular_perimetro_circulo(radio):
    pi=3.1416
    perimetro = 2 * pi * radio #Fórmula para calcular perímetro
    print(f"El perímetro es: {perimetro}")

# # # 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# # # una cantidad de segundos como parámetro y devuelva la cantidad
# # # de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    print(f"Equivale a {segundos /3600:.2f} horas") #Dividimos los segundos por 3600, que es la cantidad de segundos que contiene 1 hora.
    
# # # 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# # # número como parámetro y imprima la tabla de multiplicar de ese
# # # número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

# # # 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# # # dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma=a+b
    resta=a-b
    multi=a*b
    div=a/b
    resultados=(suma,resta,multi,div)
    
    print(f"{a} + {b} = {resultados[0]}")
    print(f"{a} - {b} = {resultados[1]}")
    print(f"{a} * {b} = {resultados[2]}")
    print(f"{a} / {b} = {resultados[3]}")

# # # 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# # # peso en kilogramos y la altura en metros, y devuelva el índice de
# # # masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc=peso/(altura**2) #Fórmula de cálculo del Indice de Masa Corporal
    print(f"Su índice de masa corporal es: {imc:.2f}")

# # # 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# # # una temperatura en grados Celsius y devuelva su equivalente en
# # # Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# # # resultado usando la función.

def celsius_a_fahrenheit(celsius):
    f=(celsius * 9/5) + 32 #Fórmula de conversión de celsuis a fahrenheit.
    print(f"{celsius}°C equivalen a {f}°F")

# # # 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# # # tres números como parámetros y devuelva el promedio de ellos.
# # # Solicitar los números al usuario y mostrar el resultado usando esta
# # # función.

def calcular_promedio(a, b, c):
    print(f"{(a+b+c)/3:.2f}")

#1)
imprimir_hola_mundo()
print("")

#2)
nombre=input("Ingrese su nombre: ")
saludar_usuario(nombre)
print("")

#3
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su lugar de residencia: ")

informacion_personal(nombre,apellido,edad,residencia)
print("")

#4)
radio=float(input("Ingrese un radio: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
print("")

#5)
segundos=int(input("Ingrese los segundos: "))

segundos_a_horas(segundos)
print("")

#6)
numero=int(input("Ingrese un número: "))
tabla_multiplicar(numero)
print("")

#7)

numA=float(input("Ingrese un número: "))
numB=float(input("Ingrese otro número: "))

operaciones_basicas(numA,numB)
print("")

#8)
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

calcular_imc(peso,altura)
print("")

#9)
celsius=float(input("Ingrese la temperatura en grados celsius: "))

celsius_a_fahrenheit(celsius)
print("")

#10)
a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
c=float(input("Ingrese el tercer número: "))

print("El promedio es: ")
calcular_promedio(a,b,c)