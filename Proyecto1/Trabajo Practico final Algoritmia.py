def buscar_producto(p):

    i = 0

    while (i < len(lista_productos)) and (lista_productos[i] != p):

        i = i + 1

    return i





#opcion 1 



def agregar_o_actualizar_producto():

    producto = str(input('Ingrese el nombre del producto: '))

    producto = producto.lower()

    indice_producto = buscar_producto(producto)

    

    unidades = int(input("¿Cuántas unidades?: "))

    longitud = len(lista_productos)

    



    if (indice_producto < longitud):

        lista_entradas[indice_producto] = lista_entradas[indice_producto] + unidades

    else:

        precio = float(input("Ingrese el precio por unidad del producto: "))

        agregar_producto(producto,precio,unidades)







def agregar_producto (producto,precio,unidades):

    lista_productos.append(producto)

    lista_precios.append(precio)

    lista_entradas.append(unidades)

    lista_salidas.append(0)

    lista_stocktotal.append(0)



def stock_ordenado_de_menor_a_mayor():         #ordenado SEGUN EL STOCK de menor a mayor

    n=len(lista_stocktotal)

    for i in range (n-1):

        for j in range(0, n-i-1):

            if lista_stocktotal[j] > lista_stocktotal[j+1]:

                lista_stocktotal[j], lista_stocktotal[j+1] = lista_stocktotal[j+1], lista_stocktotal[j]

                lista_productos[j], lista_productos[j+1] = lista_productos[j+1], lista_productos[j]

                lista_precios[j], lista_precios[j+1] = lista_precios [j+1], lista_precios[j]

                lista_entradas[j], lista_entradas[j+1] = lista_entradas[j+1], lista_entradas[j]

                lista_salidas[j], lista_salidas[j+1] = lista_salidas[j+1], lista_salidas[j]



def recalcular_stock ():

    for i in range(len(lista_productos)):

        lista_stocktotal[i] = (lista_entradas[i] - lista_salidas[i])

    stock_ordenado_de_menor_a_mayor()

    for i in range (len(lista_productos)):

        print(f'\n El producto {lista_productos[i]} tiene un precio por unidad de ${lista_precios[i]} y tiene un stock de {lista_stocktotal[i]}')

    print()

        

#opcion 2 



def registrar_salida_producto():

    if lista_productos != []:

        producto = str(input('ingrese el producto a retirar: '))

        producto = producto.lower()

        indice_producto = buscar_producto(producto)

        while (indice_producto == len(lista_productos)):

            producto = str(input('Ese producto no existe, ingrese el producto a retirar: '))

            producto = producto.lower()

            indice_producto = buscar_producto(producto)

        cant_salida = int(input('ingrese la cantidad de producto a retirar: '))

        while ((lista_entradas[indice_producto] - lista_salidas[indice_producto]) < cant_salida ):

            cant_salida = int(input('no hay suficiente stock, ingrese un número menor: ')) 



        lista_salidas[indice_producto] = lista_salidas[indice_producto] + cant_salida

    else:

        print('Aún no hay productos, debe añadir uno para poder retirar ;)')

        pass





#main

    

lista_productos = []

lista_precios = []

lista_entradas = []

lista_salidas = []

lista_stocktotal = []    



terminar = False



accion = int(input('que acción derea ejecutar?. 1 actualizar o agregar, 2 retirar, 3 mostrar stock ordenado, 4 salir: '))



while (accion != 4) and (terminar == False):

    while (accion < 1) or (accion > 5):

        accion = int(input('que acción derea ejecutar?. 1 actualizar o agregar, 2 retirar, 3 mostrar stock ordenado, 4 salir: '))

    if accion == 1:

        agregar_o_actualizar_producto()

    elif accion == 2:

        registrar_salida_producto()

    elif accion == 3:

        recalcular_stock()

    elif accion == 4:

        terminar = True

    if (terminar == False):

        accion = int(input('que acción derea ejecutar?. 1 actualizar o agregar, 2 retirar, 3 mostrar stock ordenado, 4 salir: '))



recalcular_stock()



print('El sistema a finalizado')
