# Actividades

# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

# print("\nPRECIOS FRUTAS")

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera':2300})

# print("1-",precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# precios_frutas.update({'Banana':1330, 'Manzana': 1700, 'Melón': 2800})
# print("2-",precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

# solo_frutas=list(precios_frutas.keys())
# print("3-",solo_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# print("\nNROS TELEFÓNICOS")

# agenda={}
# for i in range(5):
#     nombre=input("Ingrese el nombre de contacto: ")
#     numero=input("Ingrese el nro de teléfono: ")
#     agenda[nombre]=numero
    
# consulta=input("Ingrese el nombre y obtendrá el número telefónico: ")

# if consulta in agenda:
#     print(agenda[consulta])
# else:
#     print("El contacto no existe")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# print("\nFRASE A SET")

# #El frío es peor que el calor, el invierno es peor que el verano
# #Solicitamos una frase, la convertimos a minúscula, dividimos en palabras según los espacios y la guardamos como lista.
# frase=(input("Ingrese una frase: ")).lower().split()

# #print(f"Frase: {frase}")

# mi_set=set(frase) #Convertimos la lista a set, eliminando elementos repetidos
# print(f"Palabras únicas: {mi_set}")

# diccionario_repeticiones={}
# contador=0

# for palabra in mi_set:
#     for i in range(len(frase)):
#         if frase[i] == palabra:
#             contador+=1
#     diccionario_repeticiones[palabra]=contador
#     contador=0
# print(f"Cuántas veces aparece cada palabra?: {diccionario_repeticiones}")



# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# print("\nNOTAS ALUMNOS")

# dict_alumnos={} #Diccionario con alumnos como clave y tuplas como valor
# lista_notas=[] #Usaremos esta lista para guardar notas y luego la covertimos a tupla.

# for i in range(1,4):
#     alumno_clave=input(f"Ingrese el nombre del {i}° alumno: ") #Ingresamos nombre, será una clave del diccionario
    
#     for j in range(1,4): #Iteramos de 1 a 3 
#         nota=int(input(f"Ingrese la {j}° nota: ")) #Pedimos la nota numero j, convertimos a entero
#         lista_notas.append(nota) # Agregamos la nota a la lista
#     dict_alumnos[alumno_clave]=tuple(lista_notas) #Guardamos la lista convertida a tupla como valor y el nombre del alumno como clave
#     lista_notas=[] #Reiniciamos la lista para reutilizarla con otro alumno.
    
# for alumno in dict_alumnos.keys(): #Iteramos sobre los nombres de los alumnos(las claves)
#     promedio=sum( (dict_alumnos[alumno]) )/3 #Sumamos los valores de la tupla, lo dividimos por 3 y guardamos en 'promedio'
#     print(F"Promedio de {alumno}: {promedio}") #Mostramos el alumno actual y su promedio
    
    
    
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# print("\nAPROBADOS")

# import random

# parcial1_aprobado=set(list(random.sample(range(1,10),5)))
# parcial2_aprobado=set(list(random.sample(range(1,10),5)))

# print(parcial1_aprobado)
# print(parcial2_aprobado)

# for alumno in parcial1_aprobado & parcial2_aprobado: #Intersección, elementos comunes a ambos sets.
#     print(f"{alumno} aprobó los dos parciales.")
    
# for alumno in parcial1_aprobado ^ parcial2_aprobado: #Diferencia simétrica, elementos que sólo estan en uno de los sets.
#     print(f"{alumno} aprobó solo 1 parcial")

# for alumno in parcial1_aprobado | parcial2_aprobado:
#     print(f"{alumno} aprobó al menos 1 parcial.") #Usamos unión de conjuntos, combinamos sin repetir.
    
    
    
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# print("\nPRODUCTOS")

# productos = {"Mouse": 25,"Teclado": 18,"Monitor": 10,"Notebook": 7,"Auriculares": 20}

# consulta=input("Ingrese el nombre del producto: ")
# if consulta in productos:
#     print(f"{consulta}: {productos[consulta]}")
#     try:
#         stock=int(input("Cuantas unidades desea agregar al stock?: "))
#         productos[consulta]+=stock
#         print(f"Nuevo stock: ")
#         print(f"{consulta}: {productos[consulta]}")
#     except ValueError:
#         print("Valor inválido. Sin cambios.")
#         print(f"{consulta}: {productos[consulta]}")
# else:
#     print("El producto no existe. ¿Desea agregarlo?:\n ")
#     opcion=input("Ingrese 's' para AGREGAR, cualquier tecla para SALIR: ")
#     if opcion.lower()=='s':
#         stock=int(input("Ingrese el stock del nuevo producto: "))
#         productos[consulta]=stock
# print(productos)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

# print("\nAGENDA")

# agenda = {
#     ("Lunes", "09:00"): "Reunión de equipo",
#     ("Lunes", "14:00"): "Llamada con cliente",
#     ("Martes", "11:00"): "Entrevista laboral",
#     ("Martes", "16:00"): "Viaje de trabajo",
#     ("Miércoles", "10:00"): "Presentación de proyecto",
#     ("Miércoles", "15:00"): "Capacitación interna",
#     ("Jueves", "13:00"): "Almuerzo de negocios",
#     ("Jueves", "17:00"): "Revisión de informes",
#     ("Viernes", "08:30"): "Desayuno con socio",
#     ("Viernes", "12:00"): "Reunión de cierre de semana"
# }

# consulta=[]
# consulta.append(input("Qué día desea consultar?:  "))
# consulta.append(input("Qué horario desea consultar?(formato HH:MM):  "))
# consulta=tuple(consulta)

# if consulta in agenda.keys():
#     print(f"{consulta[0]} a las {consulta[1]} hs: {agenda[consulta]}")
# else:
#     print("No hay un evento para ese día y horario.")
    
    
    

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# paises_capitales = {
#     "Argentina": "Buenos Aires",
#     "Brasil": "Brasilia",
#     "Chile": "Santiago",
#     "Uruguay": "Montevideo",
#     "Paraguay": "Asunción",
#     "Perú": "Lima",
#     "Colombia": "Bogotá",
#     "Ecuador": "Quito",
#     "Venezuela": "Caracas",
#     "Bolivia": "La Paz"
# }

# paises=list(paises_capitales.keys())
# capitales=list(paises_capitales.values())
# invertidos={}

# for i in range(len(paises)):
#     invertidos[capitales[i]]=paises[i]
    
# print("Recorriendo con for:\n",invertidos,"\n")

# #Otra forma más rápida y simple es con la función zip:
# invertidos2=dict(zip(paises_capitales.values(),paises_capitales.keys()))
# print("Con función zip()\n",invertidos2)