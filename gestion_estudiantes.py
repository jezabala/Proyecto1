'''
Proyecto I.
Programa en consola para la gestión de estudiantes universitarios.
Alumno: Jesus Zabala.
Curso: Python | Desarrollo BackEnd.
'''

lista_estudiantes = []
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

        no_valido = True
        while no_valido:
            nombre = input('Nombre: ')
            len_nombre = len(nombre.replace(' ', '')) > 0
            if len_nombre:
                no_valido = False
            else:
                print('Nombre vacio, ingrese nuevamente el nombre.')

        no_valido = True
        while no_valido:
            apellido = input('Apellido: ')
            len_apellido = len(apellido.replace(' ', '')) > 0
            if len_apellido:
                no_valido = False
            else:
                print('Apellido vacio, ingrese nuevamente el apellido.')
        
        

        no_valido = True
        while no_valido:
            cedula = input('Cedula: ')
            cedula_valida = len(cedula.replace(' ','')) > 0

            '''
                Se verifica que la cedula ingresada no corresponda a otro estudiante ya existente,
                para evitar errores de funcionamiento del programa.
            '''

            estudiante_existe = False
            if len(lista_estudiantes) > 0:
                for estudiante in lista_estudiantes:
                    if estudiante['Cedula'] == cedula:
                        estudiante_existe = True
                        break


            if cedula_valida and not estudiante_existe:
                cedula = cedula
                no_valido = False
            else:
                print('La cedula ingresada coincide con la de otro estudiante. Introduce nuevamente la cedula')

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
        print('---------- ACTUALIZAR ESTUDIANTE ----------')
        cedula_valida = False
        while not cedula_valida:
            cedula_ingresada = input('Introduce la cedula del estudiante a actualizar: ')
            validar_cedula = len(cedula_ingresada.replace(' ', '')) > 0
            if validar_cedula:
                cedula_ingresada = cedula_ingresada
                cedula_valida = True
            else:
                print('Cedula no valida, ingrese nuevamente la cedula.')
        
        '''
            Se verifica que el estudiante exista dentro de la lista, para luego
            cambiar sus datos.
        '''
        estudiante_existente = False
        longitud_lista_estudiantes = len(lista_estudiantes)
        if longitud_lista_estudiantes > 0:
            for estudiante in lista_estudiantes:
                if estudiante['Cedula'] == cedula_ingresada:
                    estudiante_existente = True
                    break
        else:
            print('No se puede buscar el estudiante debido a que la lista esta vacia.')
        
        if estudiante_existente:
            no_valido = True
            while no_valido:
                nuevo_nombre = input('Nuevo nombre estudiante: ')
                len_nombre = len(nuevo_nombre.replace(' ', '')) > 0
                if len_nombre > 0:
                    no_valido = False
                else:
                    print('Nombre vacio, ingrese nuevamente el nombre.')
                        
            no_valido = True
            while no_valido:
                nuevo_apellido = input('Nuevo apellido estudiante: ')
                len_nombre = len(nuevo_apellido.replace(' ', '')) > 0
                if len_apellido > 0:
                    no_valido = False
                else:
                    print('Apellido vacio, ingrese nuevamente el apellido.')
            
            
            no_valido = True
            cedula_valida = None
            while no_valido:
                nueva_cedula = input('Nueva cedula estudiante: ')
                cedula_valida = len(nueva_cedula.replace(' ', '')) > 0


                ''' Se verifica que la cedula ingresada no corresponda a otro estudiante ya existente,
                    o que el estudiante ingrese la misma cedula con la que se registro para realizar
                    cambios en sus datos y evitar errores de funcionamiento del programa. '''
                

                coincide = False
                for e in lista_estudiantes:
                    if e != estudiante and e['Cedula'] == nueva_cedula:
                        coincide = True
                        break         

                if cedula_valida and not coincide:
                    estudiante['Cedula'] == nueva_cedula or estudiante['Cedula']
                    no_valido = False
                elif coincide:
                    print('Error. La cedula coincide con otro estudiante.')
                else:
                    print('Cedula incorrecta, ingrese nuevamente la cedula.')


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
            print('Estudiante no encontrado.')
        print('----------------------------------------------------')
    elif opcion == "4":
        print('---------------- ELIMINAR ESTUDIANTE ----------------')
        cedula_valida = False
        while not cedula_valida:
            cedula_estudiante = input('Cedula del estudiante a eliminar: ')
            validar_cedula = len(cedula_estudiante.replace(' ', '')) > 0
            if validar_cedula:
                cedula_valida = True
            else:
                print('Cedula no valida, ingrese nuevamente la cedula.')

        
        longitud_lista_estudiantes = len(lista_estudiantes)

        ''' Se verifica que al momento de eliminar un estudiante, primero existan dentro de la lista
        estudiantes registrados, si existen estudiantes registrados se procede a la busqueda mediante su 
        numero de cedula y por ultimo se eliminan sus datos, esto permite controlar los errores y fallos 
        del sistema. '''

        if longitud_lista_estudiantes > 0:
            for estudiante in lista_estudiantes:
                if estudiante['Cedula'] == cedula_estudiante:
                    index_student = lista_estudiantes.index(estudiante)
                    print('Datos del estudiantes a eliminar: ')
                    print(lista_estudiantes[index_student])
                    lista_estudiantes.pop(index_student)
                    print('Estudiante eliminado exitosamente.')
                    break
        else:
            print()
            print('No existen estudiantes registrados en el sistema, no se pueden eliminar datos.')
            print()
        print('----------------------------------------------------')
    elif opcion == "5":
        break
    else:
        print('----------------------------------------------------')
        print('Error, opcion no valida. Intente de nuevo.')
        print('----------------------------------------------------')