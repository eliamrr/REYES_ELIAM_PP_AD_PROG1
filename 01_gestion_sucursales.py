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

productos = ["Arroz", "Fideos", "Aceite", "Azucar"]
# Matriz de precios por tienda (cada fila es un producto y cada columna es una tienda)
precios = [
    [120, 115, 130],  # Arroz
    [80, 85, 78],  # Fideos
    [200, 210, 190],  # Aceite
    [95, 100, 90]  # Azúcar
]
#90
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
    for fila in lista:
        for i  in fila:
            if mayor < i:
                mayor = i
            if menor > i:
                menor = i
    if opcion == "mayor":
        return mayor
    elif opcion == "menor":
        return menor    

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





# Inicio del program
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
    # 3. Mostrar los productos ordenados por su precio promedio de menor a mayor.


    lista_promedios = promedios(precios)
    indices_ordenados = ordemar_lista(lista_promedios)
    lista_promedios = promedios(precios)
    mostra_una_lista(productos, lista_promedios,indices_ordenados)





