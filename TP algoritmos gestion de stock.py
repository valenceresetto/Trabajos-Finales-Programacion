productos = [[], [], [], [], [], []]  # nombres, cantidades, precios, categoría, marca, id
productos_eliminados = []             
categorias_existentes = ['celulares', 'computadoras', 'monitores', 'teclados', 'mouse']

def mostrar_menu():
    """Presenta las opciones principales del programa, se ejecuta al principio del bucle main ejecutar. las opciones se seleccionan de forma numérica. En el main ejecutar se decide que se realizará según la opción elegida
    Parametros: No requiere parametros.
    Devuelve: El número de la opción elegida en formato entero"""
    print("\nSeleccione una opción:")
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Mostrar productos agrupados por modelo base")
    print("5. Buscar productos por categoría")
    print("6. Buscar variantes por nombre")
    print("7. Mostrar productos eliminados")
    print("8. Editar categorías")
    print("9. Salir")
    while True:
        try:
            opcion = int(input("Ingrese el número de opción: "))
            if 1 <= opcion <= 9:
                return opcion
            else:
                print(" El número ingresado está fuera del rango (1 al 9). Intente nuevamente.")
        except ValueError:
            print(" El valor ingresado no es válido. Debe ingresar un número entero.")




def solicitarNombre():
    """Esta función pide el nombre de un producto, verifica que el nombre este en minusculas, que no este vacío.
    Parámetros: no recibe
    Devuelve: el nombre del producto asegurandose de que está bien escrito.
    """
    nombre = input("Ingrese el nombre del producto (puede incluir variante como talle): ").strip().lower()
    while not nombre.replace(" ", "").isalpha():
        print("El nombre debe contener solo letras (y espacios) y no puede estar vacío.")
        nombre = input("Ingrese un nombre válido para el producto: ").strip().lower()
    return nombre





def solicitarMarca():
    """Se le solicita al usuario la marca del producto. En caso de no querer especificarla, con Enter se omite este paso
    Parámetro: no tiene
    Devuelve: la marca escrita si es que se escribe una marca, caso contrario quedará escrito sin marca dentro de la matriz"""
    marca = input("Ingrese la marca del producto (Enter para omitir este paso): ").strip().lower()
    if marca and not marca.isalpha():
        print("La marca solo debe contener letras. Intente nuevamente.")  #### Revisar!!! Porque el nombre de la marca puede tener números. ####
        return solicitarMarca()
   
    return marca.capitalize() if marca else "Sin marca"


    """Se devuelve la marca ingresada en mayúsculas, usando .capitalize()"""


def generarID(productos):
    """ Se genera un ID para cada producto, va de menor a mayor (001, n); completa con ceros a la izquierda.
    Parámetro: la matriz productos
     Devuelve: un ID único para el producto nuevo que se esté agregando. """
    if not productos[5]:  
        return "001"
    ultimo_id = max(int(i) for i in productos[5])
    nuevo_id = ultimo_id + 1
    return f"{nuevo_id:03d}"




def solicitarEnteroPositivo(mensaje):
    """ Esta función solicita un numero entero que sea positivo, debe ser mayor a 0, caso ctontrario lo vuelve a pedir.
    Parámetros: recibe un mensaje, el cuál será el numero ingresado.
    Devuelve: el numero (variable valor) verificado ( que sea positivo)
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                raise ValueError("El valor no puede ser negativo.")
            return valor
        except ValueError:
            print("\u274c Entrada inválida. Ingrese un número entero positivo.")


def solicitarCaracteristicas(operacion, actuales=None):  
    """Recibe un numero de operación, 0 para agregar un nuevo producto en la misma categoria, 1 para agregar un nuevo producto y en una categoria distinta a la anterior, 2 para agregar solo cantidad de un producto ya existente  3 para solicitar caracteristicas al editar.
     Parametros: numero de operacion(0,1,2,3), actuales(registro temporal del producto con las propiedades actuales del producto, se usa a la hora de editarlo )
     Devuelve: depende los requeriemientos: cantidad, precio, marca, id_producto
       """
    if operacion == 0:
        cantidad = solicitarEnteroPositivo("Ingrese cantidad: ")
        precio = solicitarEnteroPositivo("Ingrese precio: ")
        marca = solicitarMarca()
        id_producto = generarID(productos)
        return cantidad, precio, marca, id_producto 
   
    elif operacion == 1:
        categoria = solicitarCategoria()
        cantidad = solicitarEnteroPositivo("Ingrese cantidad: ")
        precio = solicitarEnteroPositivo("Ingrese precio: ")
        marca = solicitarMarca()
        id_producto = generarID(productos)
        return cantidad, precio, categoria, marca, id_producto


    elif operacion == 2:
        cantidad = solicitarEnteroPositivo("Ingrese cantidad a agregar: ")
        return cantidad


    elif operacion == 3 and actuales:
        try:
            precio_input = input(f"Ingrese nuevo precio (actual: {actuales[0]}): ")
            precio = int(precio_input) if precio_input.strip() else actuales[0]
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")


            categoria_input = input(f"Ingrese nueva categoría (actual: {actuales[1]}): ")
            categoria = categoria_input.lower().strip() if categoria_input.strip() else actuales[1]
            if categoria_input and not categoria.isalpha():
                raise ValueError("La categoría solo debe contener letras.")


            marca_input = input(f"Ingrese nueva marca (actual: {actuales[2]}): ")
            marca = marca_input.capitalize().strip() if marca_input.strip() else actuales[2]
            if marca_input and not marca.isalpha():
                raise ValueError("La marca solo debe contener letras.")

            return precio, categoria, marca, actuales[3]
        except ValueError as e:
            print(f"Error: {e}\nDebe ingresar los datos nuevamente.")
            return solicitarCaracteristicas(3, actuales)


def buscarProductos(nombre, productos):
    """ Recibe el nombre del producto con el que se este trabajando para encontrar un indice específico e identificarlo de forma totalmente certera a través de su número de indice en todas las filas de la matriz. Consulta el id del producto en cuestion para asegurarse. Si no se encuentran coincidencias devuelve un -2 directamente.
    Parámetros: recibe la variable nombre (del producto) y la lista de productos.
    Devuelve: el índice del producto especifico buscado por el id.
    """
    nombre = nombre.strip().lower()
    coincidencias = [i for i, prod in enumerate(productos[0]) if nombre in prod.lower()]  
    if coincidencias:
        print("\nCoincidencias encontradas:")
        for i in coincidencias:
            print(f" - {productos[0][i].capitalize()} (ID: {productos[5][i]}) | Marca: {productos[4][i]} | Cantidad: {productos[1][i]} | Precio: ${productos[2][i]} | Categoría: {productos[3][i]}")
        seleccion = (input("Ingrese el ID exacto del producto a seleccionar (Enter para agregar un producto con ID nuevo): "))
        if seleccion in productos[5]:
            return productos[5].index(seleccion)
        elif seleccion == '':
            return -2
    else:
        return -2


def buscarPorCategoria(productos):
    """ Muestra los productos que se encuentran en una categoría específica, que el usuario solicita ver.
    Parámetros: lista de productos.
    Devuelve: se imprimen todos los productos de la categoría, con sus especificaciones correspondientes (ID, marca, cantidad, etc.)
    """
    categorias_existentes = sorted(set(productos[3]))
    if not categorias_existentes:
        print("No hay categorías registradas.")
        return
    print("\nCategorías disponibles:")
    for cat in categorias_existentes:
        print(f" - {cat.capitalize()}")
    categoria = input("Ingrese la categoría a buscar: ").strip().lower()
    encontrados = [i for i in range(len(productos[0])) if productos[3][i].strip().lower() == categoria]
    if encontrados:
        print(f"\nProductos en la categoría '{categoria}':")
        for i in encontrados:
            print(f" - {productos[0][i].capitalize()} (ID: {productos[5][i]}) | Marca: {productos[4][i]} | Cantidad: {productos[1][i]} | Precio: ${productos[2][i]}")
    else:
        print("No se encontraron productos en esa categoría.")


def buscarVariantesPorNombre(productos):
    """ Esta función le pide que ingrese al menos una parte del nombre del producto para poder buscarlo parcialmente.
    Parámetros: recibe la matriz de productos.
    Devuelve: se muestran los productos que coinciden con el fragmento de nombre ingresado. Si no existe, se lo informa.
    """
    fragmento = input("Ingrese el nombre o parte del nombre del producto: ").strip().lower()
    encontrados = [i for i in range(len(productos[0])) if fragmento in productos[0][i].lower()]
    if encontrados:
        print(f"\nVariantes encontradas para '{fragmento}':")
        for i in encontrados:
            print(f" - {productos[0][i].capitalize()} (ID: {productos[5][i]}) | Marca: {productos[4][i]} | Cantidad: {productos[1][i]} | Precio: ${productos[2][i]} | Categoría: {productos[3][i]}")
    else:
        print("No se encontraron productos con ese nombre.")


def agregarProducto(productos):
    seguir_agregando = -1
    while seguir_agregando <= 2:
        nombre = solicitarNombre()
        indice = buscarProductos(nombre, productos)
        if indice == -2:
            # Producto nuevo
            caracteristicas = solicitarCaracteristicas(1)
            datos = [nombre] + list(caracteristicas)
            for i in range(len(productos)):
                productos[i].append(datos[i])
            print(f"\nProducto '{nombre}' agregado correctamente.")
            print('Desea seguir agregando productos? (1: misma categoría, 2: otra categoría, 3: no)')
            seguir_agregando = int(input(''))
            while seguir_agregando == 1:
                categoria_actual = caracteristicas[2]
                nombre = solicitarNombre()
                caracteristicas = solicitarCaracteristicas(0)
                datos = [nombre, caracteristicas[0], caracteristicas[1], categoria_actual, caracteristicas[2], caracteristicas[3]]
                for i in range(len(productos)):
                    productos[i].append(datos[i])
                print(f"\nProducto '{nombre}' agregado correctamente.")
                print('Desea seguir agregando productos? (1: misma categoría, 2: otra categoría, 3: no)')
                seguir_agregando = int(input(''))
        else:
            # Producto existente: agregar cantidad
            cantidad_extra = solicitarCaracteristicas(2)
            productos[1][indice] += cantidad_extra
            print(f"\nSe agregó {cantidad_extra} unidades al producto '{nombre}' (ID: {productos[5][indice]}).")
            print ('¿Desea modificar otro producto existente? (sino se agrega como nuevo) 1 para sí, 2 para no')
            seguir_agregando = int(input(''))
            if seguir_agregando == 2:
                break
    return productos





def editarProducto(nombre, productos, indice):
    """Edita las caracteristicas de un producto
    Parametros: recibe el nombre del producto (nombre) la lista con los datos (productos) y la posición del producto que se va a editar (indice)
    Devuelve: Los productos con los datos actualizados"""
   
    actuales = [productos[2][indice], productos[3][indice], productos[4][indice]]
    nuevos = solicitarCaracteristicas(3, actuales)
    productos[2][indice] = nuevos[0]  # precio
    productos[3][indice] = nuevos[1]  # categoría  
    productos[4][indice] = nuevos[2]  # marca  
    print(f"\nProducto '{nombre}' editado correctamente.")
    return productos


def eliminarProducto(nombre, productos, indice, productos_eliminados):
    """Esta funcion elimina una cantidad especifica de un producto del inventario
    Parametros: Recibe el nombre del producto (nombre), lista del inventario (productos), el (indice) indicando la posicion del producto y recibe los productos que fueron facturados (productos_facturados)
    Devuelve: la lista actualizada de los productos y los facturados"""
    cantidad_actual = productos[1][indice]
    print(f"Cantidad actual de {nombre}: {cantidad_actual}")
    try:
        cantidad_eliminar = int(input("Cantidad a eliminar: "))
        if 0 <= cantidad_eliminar <= cantidad_actual:
            productos[1][indice] -= cantidad_eliminar
            productos_eliminados.append((nombre, cantidad_actual, cantidad_eliminar, productos[1][indice], productos[2][indice]))
            print(f"\nSe eliminaron {cantidad_eliminar} unidades de '{nombre}'.")
            if productos[1][indice] == 0:
                print(f" Producto '{nombre}' agotado.")
        else:
            print("Cantidad inválida. La operación fue cancelada.")
    except ValueError:
        print(" Entrada inválida. Debe ingresar un número entero. Intente nuevamente: ")
    return productos, productos_eliminados


def mostrarProductosPorCategoria(productos): 
    """Muestra todos los productos agrupados por categoría si es que hay productos cargados.
Parámetros: recibe la matriz de productos
Devuelve: Hace un print de los productos ordenados por categorías."""

    if not productos[0]:
        print("No hay productos cargados.")
        return  

    categorias = {}
    for i in range(len(productos[0])):
        categoria = productos[3][i]  # Aquí usamos la categoría real
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(i)


    for categoria in sorted(categorias):
        print(f"\nCategoría: {categoria.capitalize()}")
        for i in categorias[categoria]:
            print(f" - {productos[0][i].capitalize()} (ID: {productos[5][i]}) | Marca: {productos[4][i]} | Cantidad: {productos[1][i]} | Precio: ${productos[2][i]}")


def muestra_productos_eliminados(productos_despachados):
    """Muestra los productos eliminados 
       Parámetros: lista de tuplas con los productos        
       eliminados
       Devuelve: Imprime una lista de productos eliminados, incluyendo las cantidades y precios de los productos eliminados"""
    if productos_despachados:
        print("\nFactura de productos eliminados:")
        for nombre, cant_inicial, cant_eliminada, cant_restante, precio in productos_despachados:
            print(f"{nombre.capitalize()}: Eliminados {cant_eliminada} unidades. Precio Unitario: ${precio}")
    else:
        print("No se eliminaron productos.")


def ejecutar():
    """ El usuario ingresa la operación (opción) que desea ejecutar, dependiendo cuál sea, llama a la función correspondiente.
    Parámetros: no recibe.
    Devuelve: se ejecuta la operación solicitada, llamando a la función correspondiente.
    """
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            agregarProducto(productos)
        elif opcion == 2:
            nombre = solicitarNombre()
            indice = buscarProductos(nombre, productos)
            if indice != -2:
                editarProducto(nombre, productos, indice)
            else:
                print("Producto no encontrado.")
        elif opcion == 3:
            nombre = solicitarNombre()
            indice = buscarProductos(nombre, productos)
            if indice != -2:
                eliminarProducto(nombre, productos, indice, productos_eliminados)
            else:
                print("Producto no encontrado.")
        elif opcion == 4:
            mostrarProductosPorCategoria(productos)
        elif opcion == 5:
            buscarPorCategoria(productos)
        elif opcion == 6:
            buscarVariantesPorNombre(productos)
        elif opcion == 7:
            muestra_productos_eliminados(productos_eliminados)
        elif opcion == 8:
            editarCategorias(categorias_existentes, productos)
        elif opcion == 9:
            print("\n¡Gracias por usar el sistema de inventario!")
            break



def editarCategorias(categorias, productos):
    print("Estas son las categorías existentes:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")

    print("\n¿Qué acción desea realizar?")
    print("1. Eliminar categoría")
    print("2. Agregar categoría")
    print("3. Editar nombre de una categoría existente")

    while True:
        try:
            accion = int(input("Seleccione una opción: ")) 
            assert accion in {1, 2, 3}, "Elija entre una de las operaciones disponibles"

            if accion in {1, 3}:
                eleccion_categoria = int(input("Elija el número de la categoría a editar: "))
                assert 1 <= eleccion_categoria <= len(categorias), "Debe seleccionar un número válido de categoría"
                nombre_categoria = categorias[eleccion_categoria - 1]

            if accion == 1:
                while True:
                    try:
                        print(f"\nEliminar la categoría '{nombre_categoria}' requiere eliminar todos los productos dentro de la misma.")
                        opcion = input("¿Está seguro de que desea eliminarla?\n1. SÍ\n2. NO\nSeleccione: ").strip()

                        if opcion not in {"1", "2"}:
                            print("No seleccionó una opción válida.")
                            continue

                        if opcion == "1":
                            # Eliminar productos que pertenecen a esta categoría
                            indices_a_eliminar = [i for i, categoria in enumerate(productos[3]) if categoria == nombre_categoria]
                            for i in sorted(indices_a_eliminar, reverse=True):
                                for fila in productos:
                                    fila.pop(i)

                            # Eliminar la categoría
                            categorias.pop(eleccion_categoria - 1)
                            print("Categoría eliminada exitosamente.")
                        else:
                            print("Operación cancelada.")
                        break

                    except Exception as e:
                        print("Error al eliminar la categoría:", e)

            elif accion == 2:
                nueva_categoria = input("Ingrese el nombre de la nueva categoría: ").strip().lower()
                while not nueva_categoria.isalpha() or nueva_categoria in categorias:
                    if not nueva_categoria.isalpha():
                        print("La categoría solo debe contener letras.")
                    else:
                        print("Esa categoría ya existe.")
                    nueva_categoria = input("Ingrese el nombre de la nueva categoría: ").strip().lower()
                categorias.append(nueva_categoria)
                print("Categoría agregada exitosamente.")

            elif accion == 3:
                nuevo_nombre = input(f"Ingrese el nuevo nombre para la categoría '{nombre_categoria}': ").strip().lower()
                while not nuevo_nombre.isalpha() or nuevo_nombre in categorias:
                    if not nuevo_nombre.isalpha():
                        print("El nombre debe contener solo letras.")
                    else:
                        print("Ya existe una categoría con ese nombre.")
                    nuevo_nombre = input("Ingrese un nombre diferente: ").strip().lower()

                # Reemplazar nombre en la lista de categorías
                categorias[eleccion_categoria - 1] = nuevo_nombre

                # Reemplazar también en los productos
                productos[3] = [nuevo_nombre if cat == nombre_categoria else cat for cat in productos[3]]

                print("Categoría renombrada exitosamente.")

            break

        except ValueError:
            print("Error: debe ingresar un número válido.")
        except AssertionError as e: 
            print("Error:", e)

    return categorias

    


def solicitarCategoria():
    """
    Esta función le solicita al usuario la categoría cuando sea requerido. Primero muestra la lista de las categorias presentes y luego espera la entrada de la categoria. En caso de que no exista, puede crearse una nueva eligiendo 0, solo se aceptan caracteres letras.
    Parámetros: no tiene
    Devuelve: el nombre de la caracteristica elegida vieja o nueva para su uso posterior
    """
    while True:
        try:
            print("Para agregar un producto elija el numero entre las categorias presentes o ingrese 0 para crear una nueva categoria")
            [print(i+1, " ", categorias_existentes[i]) for i in range(len(categorias_existentes))]
            eleccion_categoria = int(input("Elija el número de opción de la categoria: "))    
            assert 0 <= eleccion_categoria <= len(categorias_existentes)                                                
            break
        except (ValueError):
            print("No seleccionó un número de categoria, Por favor vuelva a intentar: ")
        except AssertionError:
            print("El número de categoría que seleccionó no existe, por favor ingrese una categoría válida: ")
           

    if eleccion_categoria == 0:
       
        categoria = input("Ingrese categoría del producto: ").strip().lower()
        while not categoria.isalpha():
           print("La categoría solo debe contener letras. Intente nuevamente.")
           categoria = input("Ingrese categoría del producto: ").strip().lower()
        categorias_existentes.append(categoria)
    else:
        categoria = categorias_existentes[eleccion_categoria - 1]
    return categoria


# Ejecutar programa
ejecutar()