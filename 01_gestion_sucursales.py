# # # Gestión de Sucursales en Python

# Crea un programa en Python que maneje dos estructuras paralelas:
#  -  Una lista de nombres de productos.
#  -  Una matriz de precios donde cada fila representa un producto y cada columna representa el precio
# en diferentes tiendas (Tienda1, Tienda2 y Tienda3).

# El programa debe mostrar un Menú con las siguientes Opciones:
# 1. Solicitar al usuario una Tienda y Listar los productos con los nombres y precios correspondientes.
# 1. Mostrar el producto con el precio más alto y el más bajo de todas las tiendas.
# 2. Mostrar los productos ordenados por su precio promedio de menor a mayor.

# El programa debe funcionar de manera paralela, es decir, la lista de nombres de productos y la matriz de
# precios deben mantenerse sincronizadas en todo momento.
# Nota: Pueden utilizarse funciones propias.
# Todo ingreso de dato debe ser validado.
# Todo debe estar claramente comentado/documentado.
# Debe respetar las reglas de estilo¡


# ----------------------------------------------------------------------------------------------------------
### GENERAL
def menu_opciones():
    "Funcion que muestra las opciones del menu"
    print("--------------------- Menu de inventario ----------------------------")
    print("")
    print("1. Solicitar al usuario una Tienda y Listar los productos con los nombres y precios correspondientes.")
    print("2. Mostrar el producto con el precio más alto y el más bajo de todas las tiendas.")
    print("3. Mostrar los productos ordenados por su precio promedio de menor a mayor.")
    print("4. Salir\n")

def opcion_validada(desde:int,hasta:int)->int:
    "Funcion que recibe por parametros dos numeros y pide por consola un numero y lo validad que este dentro del rango de los parametros"
    opcion = int(input(f"> Ingrese una opcion desde ({desde} a {hasta}): "))
    while opcion > hasta  or opcion < desde:
            print("Error ingrese una opcion valida")
            opcion = int(input(f"> Ingrese una opcion desde ({desde} a {hasta}): "))
    return opcion

# ----------------------------------------------------------------------------------------------------------
### 1
def solicitar_opcion_tienda():
    "Funcion que solocita un numero al usuario y lo verifica que este en un rango y antes de retornarlo le resta uno para que quede listo para selecionar en unalista"
    print("-------------TIENDAS----------------")
    print("1. Tienda 1")
    print("2. Tienda 2")
    print("3. Tienda 3")
    opcion = opcion_validada(1, 3)
    opcion -= 1
    return opcion
# ----------------------------------------------------------------------------------------------------------
### 2
def buscar_numero_mayor_o_menor_lista(lista:list,opcion:str)->int:
    "Función que recibe una lista anidada de números y un parámetro de opción (una palabra). Itera para encontrar el número mayor y menor dentro de toda la estructura, y devuelve el valor correspondiente según la opción seleccionada." 
    mayor = lista[0][0]
    menor = lista[0][0]
    res = mayor
    for fila in lista:
        for i  in fila:
            if mayor < i:
                mayor = i
            if menor > i:
                menor = i
    if opcion == "mayor":
        res =  mayor
    elif opcion == "menor":
        res = menor    
    return res
def buscar_palbra_en_list_anida_extraer_indices(lista:list,palabra)->list:
    "Funcion que recibe por parametro una lista y una palabra la cual la buscaremos en la lista y guardaremos en una nueva lista y la retornamos"
    indices = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if palabra == lista[i][j]:
                indices.append([i,j])
    return indices

def mostrar_datos_indices(lista_A:list,lista_B:list,indices:list, titulo:str):
    "Funcion que recibe dos listas con datos y otra con indices de ubicacion que son los que vamos a buscar y un titulo que lo utilizaremos para mostar antes de los datos"
    print(f"---------- Producto {titulo} precio --------------")
    for i in indices:
        print("{:<15} $ {:<15}".format(lista_A[i[0]], lista_B[i[0]][i[1]]))
    print("")

# ----------------------------------------------------------------------------------------------------------
### 3

def promedios(lista:list)->list:
    "Función que recibe una lista y calcula el promedio para cada producto en la lista anidada y devuelve una lista con esos promedios."
    promedios = []
    for fila in lista:
        suma = 0
        for numero in fila:
            suma += numero
        promedios.append(round(suma / len(fila)))
    return promedios

def unir_listas(lista_a:list, lista_b:list)->list:
    "Funcion que recibe dos listas relacionadas  y las une a traves de su indice y devuelve la lista"
    nueva_lista = []
    for i in range(len(lista_a)):
        nueva_lista.append([lista_a[i],lista_b[i]])
    return nueva_lista

def ordenar_listas(lista:list)->list:
    "Funcion que recibe una lista  y la ordena de menor a mayor y la retorna"
    for i in range(len(lista) - 1):
        for j in range(i, len(lista)):
            if lista[i][1] > lista[j][1]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def mostrar_productos(lista:list):
    "Funcion que muestra  una lista con datos relacionados"
    print("--------------- Productos ------------")
    for i in lista:
        print("{:<10}  $ {:<10}".format(i[0], i[1]))

# ----------------------------------------------------------------------------------------------------------
productos = ["Arroz", "Fideos", "Aceite", "Azucar"]
# Matriz de precios por tienda (cada fila es un producto y cada columna es una tienda)
precios = [
    [120, 115, 130],  # Arroz
    [80, 85, 78],  # Fideos
    [200, 210, 190],  # Aceite
    [95, 100, 90]  # Azúcar
]
inicio = True
#Iincio
while inicio:
    menu_opciones()
    opcion = opcion_validada(1,4)
    #lOGICA
    if opcion == 1:
        ### 1. Solicitar al usuario una Tienda y Listar los productos con los nombres y precios correspondientes.
        #Le mostramos y le pedimos una opcion al usuario
        tienda = solicitar_opcion_tienda()
        #Mostramos
        print("-------- Productos --------")
        for i in range(len(productos)):
            print("{:<15}  $ {:<15}".format(productos[i], precios[i][tienda]))
        print("")
    elif opcion == 2:
        # 2. Mostrar el producto con el precio más alto y el más bajo de todas las tiendas.
        #Buscamos numero mayor y menor
        num_mayor = buscar_numero_mayor_o_menor_lista(precios,"mayor")
        num_menor = buscar_numero_mayor_o_menor_lista(precios,"menor")
        #Indices de los numeros mayore y menores
        list_indices_mayor = buscar_palbra_en_list_anida_extraer_indices(precios,num_mayor)
        list_indices_menor = buscar_palbra_en_list_anida_extraer_indices(precios,num_menor)
        #Modtramos productio
        mostrar_datos_indices(productos, precios, list_indices_mayor, "mayor")
        mostrar_datos_indices(productos, precios, list_indices_menor, "menor")
    elif opcion == 3:
        ### 3. Mostrar los productos ordenados por su precio promedio de menor a mayor.
        #Obtenemos los promedios
        lista_promedios = promedios(precios)
        #Unimos los datos
        lista_datos = unir_listas(productos,lista_promedios)
        #Ordenamos menor a mayor
        lista_ordenada = ordenar_listas(lista_datos)
        #Mostramos
        mostrar_productos(lista_ordenada)
    elif opcion == 4:
        print("Saliendo")
        inicio = False













