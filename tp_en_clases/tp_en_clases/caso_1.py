# --- Parcial I - Biblioteca  ---
#


# se reserva espacio para 100 libros
titulos = [""] * 100
ejemplares = [0] * 100

cantidad_libros = 0   # cuántos libros hay 
opcion = ""

while opcion != "9":
    print("--- MENÚ BIBLIOTECA ---")
    print("1- Ingresar lista de títulos")
    print("2- Ingresar lista de ejemplares disponibles")
    print("3- Mostrar catálogo con stock")
    print("4- Consultar disponibilidad de un título")
    print("5- Lista agotados (0 ejemplares)")
    print("6- Agregar título")
    print("7- Actualizar ejemplares (préstamo / devolución)")
    print("8- Ver catálogo")
    print("9- Salir")

    opcion = input("Elegí una opción: ")

    # Ingresar lista de títulos

    if opcion == "1":
        cant = input("¿Cuántos títulos vas a cargar? ")
        if cant.isdigit():
            cant = int(cant)
            for i in range(cant):
                if cantidad_libros < len(titulos):
                    titulo = input("Título del libro: ").strip()
                    if titulo != "":
                        titulos[cantidad_libros] = titulo
                        ejemplares[cantidad_libros] = 0
                        cantidad_libros += 1
                    else:
                        print("El título no puede estar vacío.")
                else:
                    print("No hay más espacio en el catálogo.")
        else:
            print("Ingrese un número valido.")

    # Ingresar ejemplares por título

    elif opcion == "2":
        if cantidad_libros == 0:
            print("No hay títulos cargados.")
        else:
            for i in range(cantidad_libros):
                cant = input(f"Copias para '{titulos[i]}': ")
                if cant.isdigit():
                    ejemplares[i] = int(cant)
                else:
                    print("Valor inválido, se deja en 0.")

    # Mostrar catálogo con stock

    elif opcion == "3":
        if cantidad_libros == 0:
            print("Catálogo vacío.")
        else:
            for i in range(cantidad_libros):
                print(titulos[i], ":", ejemplares[i], "copias")

    # Consultar disponibilidad
    elif opcion == "4":
        buscar = input("Título a consultar: ").strip()
        encontrado = False
        for i in range(cantidad_libros):
            if titulos[i].lower() == buscar.lower():
                print("Disponibles:", ejemplares[i], "copias")
                encontrado = True
        if not encontrado:
            print("Título no encontrado.")

    # Listar agotados

    elif opcion == "5":
        agotados = False
        for i in range(cantidad_libros):
            if ejemplares[i] == 0:
                print("Agotado:", titulos[i])
                agotados = True
        if not agotados:
            print("No hay libros agotados.")

    # Agregar título

    elif opcion == "6":
        if cantidad_libros >= len(titulos):
            print("No hay espacio para más libros.")
        else:
            nuevo = input("Nuevo título: ").strip()
            if nuevo == "":
                print("El título no puede estar vacío.")
            else:
                repetido = False
                for i in range(cantidad_libros):
                    if titulos[i].lower() == nuevo.lower():
                        repetido = True
                if repetido:
                    print("Ese título ya existe.")
                else:
                    copias = input("Cantidad de ejemplares: ")
                    if copias.isdigit():
                        titulos[cantidad_libros] = nuevo
                        ejemplares[cantidad_libros] = int(copias)
                        cantidad_libros += 1
                    else:
                        print("Número inválido, no se agregó.")

    # Actualizar ejemplares (préstamo / devolución)

    elif opcion == "7":
        titulo_act = input("Título a actualizar: ").strip()
        indice = -1
        for i in range(cantidad_libros):
            if titulos[i].lower() == titulo_act.lower():
                indice = i
        if indice == -1:
            print("Título no encontrado.")
        else:
            print("Ejemplares actuales:", ejemplares[indice])
            accion = input("¿Préstamo (p) o devolución (d)? ").lower()
            cant = input("Cantidad: ")
            if cant.isdigit():
                cant = int(cant)
                if accion == "p":
                    if cant > 0 and cant <= ejemplares[indice]:
                        ejemplares[indice] -= cant
                        print("Préstamo registrado.")
                    else:
                        print("No hay suficientes copias.")
                elif accion == "d":
                    if cant >= 1:
                        ejemplares[indice] += cant
                        print("Devolución registrada.")
                    else:
                        print("La cantidad debe ser mayor o igual a 1.")
                else:
                    print("Opción inválida.")
            else:
                print("Ingresá un número válido.")

    # Ver catálogo
    elif opcion == "8":
        if cantidad_libros == 0:
            print("Catálogo vacío.")
        else:
            for i in range(cantidad_libros):
                print(f"{titulos[i]} ({ejemplares[i]} copias)")

    #  Salir
    elif opcion == "9":
        print(" Gracias por usar el sistema")

    else:
        print("Opción no válida, intente otra vez.")