# # # 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# # # deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

# # # 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# # # mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# # # mensaje “Desaprobado”.

nota=float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# # # 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# # # número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# # # contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# # # operador de módulo (%) en Python para evaluar si un número es par o impar.

n=int(input("Ingrese un número par: "))

if n%2 ==0: # Verificamos si el resto de dividir el número ingresado entre dos es igual a cero
    print("Ha ingresado un número par")
else: # Si el resto es diferente de cero, el número no es par.
    print("Por favor ingrese un número par.")

# # # 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# # # siguientes categorías pertenece:
# # # ● Niño/a: menor de 12 años.
# # # ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# # # ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# # # ● Adulto/a: mayor o igual que 30 años.

edad=int(input("Ingrese su edad: "))

if edad<12:
    print("Categoría: Niño")
elif 12<=edad<18:
    print("Categoría: Adolescente")
elif 18<= edad <30:
    print("Categoría: Adulto/a joven")
elif edad >=30:
    print("Categoría: Adulto/a")


# # # 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# # # (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# # # pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# # # pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# # # de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# # # como una lista o un string.

key=input("Por favor, ingrese su contraseña: ")

if 8 <= len(key) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# # # 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las
# # # compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# # # Definir la lista numeros_aleatorios de la siguiente forma:
# # # import random
# # # numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

import random
from statistics import mode, median, mean

# Generamos una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media=mean(numeros_aleatorios)
mediana=median(numeros_aleatorios)
moda=mode(numeros_aleatorios)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and mediana > moda:
    print("Sesgo positivo.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")

# # # 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# # # termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# # # pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# # # pantalla.

frase=input("Ingrese una palabra o frase: ")
ul=frase[len(frase)-1].lower() #almacenamos en 'ul' el ultimo caracter de la cadena ingresada
# y lo almacenamos en minúscula para facilitar la comparación en el match-case

# Si es una vocal, concatenamos el signo de exclamación al final de la frase:
match ul:
    case "a":
        frase=frase+"!"
    case "e":
        frase=frase+"!"
    case "i":
        frase=frase+"!"
    case "o":
        frase=frase+"!"
    case "u":
        frase=frase+"!"

print(frase)

# # # 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# # # dependiendo de la opción que desee:
# # # 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# # # 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# # # 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# # # El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# # # usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# # # lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre=input("Ingrese su nombre: ")
nombreNuevo=""

print("Elija una opción (ingrese un número): \n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n"
"2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n"
"3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opt=input(">")

match opt:
    case "1":
        nombreNuevo=nombre.upper()
    case "2":
        nombreNuevo=nombre.lower()
    case "3":
        nombreNuevo=nombre.title()

print(nombreNuevo)

# # # 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# # # magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# # # por pantalla:
# # # ● Menor que 3: "Muy leve" (imperceptible).
# # # ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# # # ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# # # generalmente no causa daños).
# # # ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# # # débiles).
# # # ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# # # ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud=float(input("Ingrese la magnitud del terremoto en escala Richter: "))

match magnitud:
    case n if magnitud<3:
        print("Muy leve (imperceptible).")
    case n if 3<=magnitud<4:
        print("Mayor o igual que 3 y menor que 4: Leve (ligeramente perceptible).")
    case n if 4<=magnitud<5:
        print("Mayor o igual que 4 y menor que 5: Moderado (sentido por personas, pero generalmente no causa daños).")
    case n if 5<=magnitud<6:
        print("Mayor o igual que 5 y menor que 6: Fuerte (puede causar daños en estructuras débiles).")
    case n if 6<=magnitud<7:
        print("Mayor o igual que 6 y menor que 7: Muy Fuerte (puede causar daños significativos).")
    case n if 7<=magnitud:
        print("Mayor o igual que 7: Extremo (puede causar graves daños a gran escala).")

# # # 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# # # del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# # # si el usuario se encuentra en otoño, invierno, primavera o verano.

from datetime import datetime #Importamos la librería datetime para manejar fechas.

# Preguntamos en qué hemisferio se encuentra el usuario para determinar en qué estación se encuentra.
hemi=input("¿En qué hemisferio se encuentra? Ingrese N para Norte o S para Sur:").lower()

# Solicitamos día y mes.
dia=input("Ingrese el dia:")
mes=input("Ingrese el mes (en número):")

# Concatenamos las strings de dia y mes y le damos formato de fecha.
fecha=datetime.strptime((dia+"-"+mes), "%d-%m")

# Seteamos las fechas de inicio y fin de cada estación del hemisferio Norte de acuerdo a la tabla proporcionada.
# Para las estaciones del hemisferio Sur usaremos las mismas fechas de inicio y fin, pero con diferentes estaciones.

invNorInicio=datetime.strptime("21-12", "%d-%m")
# Las fechas por defecto toman el año 1900
# por eso aquí se especifica que el invierno Norte inició el 21-12-1900 y finalizó en marzo del año siguiente
invNorFin=datetime.strptime("20-03-1901", "%d-%m-%Y") 

# En los demas casos no es necesario especificar el año
# ya que las estaciones inician y finalizan dentro del mismo año
priNorInicio=datetime.strptime("21-03", "%d-%m")
priNorFin=datetime.strptime("20-06", "%d-%m")

verNorInicio=datetime.strptime("21-06", "%d-%m")
verNorFin=datetime.strptime("20-09", "%d-%m")

otoNorInicio=datetime.strptime("21-09", "%d-%m")
otoNorFin=datetime.strptime("20-12", "%d-%m")

# Si el hemisferio es 'n' (Norte), muestra por pantalla la estación de acuerdo a la fecha.
if hemi=="n":
    if invNorInicio<=fecha <=invNorFin:
        print("Invierno")
    elif priNorInicio <=fecha<=priNorFin:
        print("Primavera")
    elif verNorInicio <=fecha<=verNorFin:
        print("Verano")
    elif otoNorInicio <=fecha<=otoNorFin:
        print("Otoño")
elif hemi=="s": # Si el hemisferio es "s" (Sur), utilizamos las mismas fechas y las estaciones de acuerdo a la tabla.   
    if invNorInicio<=fecha <=invNorFin:
        print("Verano")
    elif priNorInicio <=fecha<=priNorFin:
        print("Otoño")
    elif verNorInicio <=fecha<=verNorFin:
        print("Invierno")
    elif otoNorInicio <=fecha<=otoNorFin:
        print("Primavera")