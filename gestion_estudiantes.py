'''
Proyecto I.
Programa en consola para la gestión de estudiantes universitarios.
Alumno: Jesus Zabala.
Curso: Python | Desarrollo BackEnd.
'''

lista_estudiantes = []
no_valido = True
is_number = None


while True:
    opcion = input(''' Gestion de estudiantes.
 1.- Listado de estudiantes.
 2.- Registrar estudiante.
 3.- Actualizar estudiante.
 4.- Eliminar estudiante.
 5.- Salir. 
 Seleccione una seccion: ''')
    if opcion == "1":
        print('---------- LISTADO DE ESTUDIANTES ----------')
        for i, estudiante in enumerate(lista_estudiantes, 1):
            print(f'Estudiante {i}:')
            for key, value in estudiante.items():
                print(f'{key}: {value}')
            print()
        print('--------------------------------------------')
    elif opcion == "2":
        print('---------- REGISTRAR ESTUDIANTE ----------')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        cedula = input('Cedula: ')

        ''' Se validan de las notas, para comprobar que se ingresa un 
        numero entero o flotante para evitar errores en el calculo del 
        promedio. '''

        no_valido = True
        while no_valido:
            nota1 = input('Nota 1: ')
            is_number = nota1.replace('.', '').isdigit()
            if is_number:
                if '.' in nota1:
                    nota1 = float(nota1)
                    no_valido = False
                    is_number = None
                elif '.' not in nota1:
                    nota1 = int(nota1)
                    no_valido = False
                    is_number = None
            else:
                print()
                print('Nota no valida. Vuelva a ingresar la nota.')
                print()
                
        no_valido = True

        while no_valido:
            nota2 = input('Nota 2: ')
            is_number = nota2.replace('.', '').isdigit()
            if is_number:
                if '.' in nota2:
                    nota2 = float(nota2)
                    no_valido = False
                    is_number = None
                elif '.' not in nota2:
                    nota2 = int(nota2)
                    no_valido = False
                    is_number = None
            else:
                print()
                print('Nota no valida. Vuelva a ingresar la nota.')
                print()
        
        no_valido = True
        while no_valido:
            nota3 = input('Nota 3: ')
            is_number = nota3.replace('.', '').isdigit()
            if is_number:
                if '.' in nota3:
                    nota3 = float(nota3)
                    no_valido = False
                    is_number = None
                elif '.' not in nota3:
                    nota3 = int(nota3)
                    no_valido = False
                    is_number = None
            else:
                print()
                print('Nota no valida. Vuelva a ingresar la nota.')
                print()

        # Se calcula el promedio del estudiante
        promedio = round(((nota1+nota2+nota3) / 3), 2)

        # Se llena el diccionario con los datos del estudiante
        estudiante = {
            'Nombre': nombre,
            'Apellido': apellido,
            'Cedula': cedula,
            'Nota 1': nota1,
            'Nota 2': nota2,
            'Nota 3': nota3,
            'Promedio': promedio
        }

        # Se añade el estudiante a la lista
        lista_estudiantes.append(estudiante)
        print('Estudiante registrado exitosamente.')
        print('------------------------------------------')
    elif opcion == "3":
        print('-------------- ACTUALIZAR ESTUDIANTE --------------')
        cedula_estudiante = input('Introduce la cedula del estudiante a actualizar: ')
        longitud_lista_estudiantes = len(lista_estudiantes)

        ''' Se verifica que al momento de actualizar datos de un estudiante, primero existan dentro de la lista
        estudiantes registrados, si existen estudiantes registrados se procede a la busqueda mediante su 
        numero de cedula, esto permite controlar los errores y fallos del sistema. '''

        if longitud_lista_estudiantes != 0:
            for estudiante in lista_estudiantes:
                if estudiante['Cedula'] == cedula_estudiante:
                    nuevo_nombre = input('Nuevo nombre estudiante: ')
                    nuevo_apellido = input('Nuevo apellido estudiante: ')
                    nueva_cedula = input('Nueva cedula estudiante: ')

                    ''' Se validan las notas, para comprobar que se ingresa un 
                    numero entero o flotante para evitar errores en el calculo del 
                    promedio. '''
                    no_valido = True
                    while no_valido:
                        nueva_nota1 = input('Nueva Nota 1: ')
                        is_number = nueva_nota1.replace('.', '').isdigit()
                        if is_number:
                            if '.' in nueva_nota1:
                                nueva_nota1 = float(nueva_nota1)
                                no_valido = False
                                is_number = None
                            elif '.' not in nueva_nota1:
                                nueva_nota1 = int(nueva_nota1)
                                no_valido = False
                                is_number = None
                        else:
                            print()
                            print('Nota no valida. Vuelva a ingresar la nota.')
                            print()

                    no_valido = True
                    while no_valido:
                        nueva_nota2 = input('Nueva Nota 2: ')
                        is_number = nueva_nota2.replace('.', '').isdigit()
                        if is_number:
                            if '.' in nueva_nota2:
                                nueva_nota2 = float(nueva_nota2)
                                no_valido = False
                                is_number = None
                            elif '.' not in nueva_nota2:
                                nueva_nota2 = int(nueva_nota2)
                                no_valido = False
                                is_number = None
                        else:
                            print()
                            print('Nota no valida. Vuelva a ingresar la nota.')
                            print()


                    no_valido = True
                    while no_valido:
                        nueva_nota3 = input('Nueva Nota 3: ')
                        is_number = nueva_nota3.replace('.', '').isdigit()
                        if is_number:
                            if '.' in nueva_nota3:
                                nueva_nota3 = float(nueva_nota3)
                                no_valido = False
                                is_number = None
                            elif '.' not in nueva_nota3:
                                nueva_nota3 = int(nueva_nota3)
                                no_valido = False
                                is_number = None
                        else:
                            print()
                            print('Nota no valida. Vuelva a ingresar la nota.')
                            print()

                    # Se calcula el promedio del estudiante
                    nuevo_promedio = round(((nueva_nota1+nueva_nota2+nueva_nota3) / 3), 2)

                    # Se actualizan los datos del estudiante.
                    estudiante.update({
                        'Nombre': nuevo_nombre,
                        'Apellido': nuevo_apellido,
                        'Cedula': nueva_cedula,
                        'Nota 1': nueva_nota1,
                        'Nota 2': nueva_nota2,
                        'Nota 3': nueva_nota3,
                        'Promedio': nuevo_promedio
                    })
                    print('Datos del estudiante actualizados exitosamente.')
                else:
                    print('Error. Estudiante no registrado')
        else:
            print()
            print('No existen estudiantes registrados en el sistema, no se pueden actualizar datos.')
            print()

        print('----------------------------------------------------')
    elif opcion == "4":
        print('---------------- ELIMINAR ESTUDIANTE ----------------')
        cedula_estudiante = input('Cedula del estudiante a eliminar: ')
        longitud_lista_estudiantes = len(lista_estudiantes)

        ''' Se verifica que al momento de eliminar un estudiante, primero existan dentro de la lista
        estudiantes registrados, si existen estudiantes registrados se procede a la busqueda mediante su 
        numero de cedula y por ultimo se eliminan sus datos, esto permite controlar los errores y fallos 
        del sistema. '''

        if longitud_lista_estudiantes != 0:
            for estudiante in lista_estudiantes:
                if estudiante['Cedula'] == cedula_estudiante:
                    index_student = lista_estudiantes.index(estudiante)
                    print('Datos del estudiantes a eliminar: ')
                    print(lista_estudiantes[index_student])
                    lista_estudiantes.pop(index_student)
                    print('Estudiante eliminado exitosamente.')
                else:
                    print('Error. Estudiante no existente.')
                    break
        else:
            print()
            print('No existen estudiantes registrados en el sistema, no se pueden actualizar datos.')
            print()
        print('----------------------------------------------------')
    elif opcion == "5":
        break
    else:
        print('----------------------------------------------------')
        print('Error, opcion no valida. Intente de nuevo.')
        print('----------------------------------------------------')