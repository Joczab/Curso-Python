'''Proyecto en Python para Gestionar estudiantes universitarios por medio de consola '''

estudiantes = []
ciclo = True

while ciclo:
    
    validacion  = False
    validacion2 = False
    validacion3 = False
    valCedula   = False
    valNombre   = False
    valApellido = False
    is_number = None
    
    seleccion = input('''
                          Gestion de estudiante universitario.
                          Seleccione la seccion:
                          1. Listado de estudiantes.
                          2. Registrar estudiante.
                          3. Actualizar estudiante.
                          4. Eliminar estudiante.
                          5. Salir\n''')
    
    if seleccion == '1':
        
        print('------------------------------------------')
        print('Listado de estudiantes:\n')
    
        for index,estudiante in enumerate(estudiantes,1):
            
            print ('\nEstudiante :',index )
            print(f'\nNombre: {estudiante["name"]}\nApellido: {estudiante["lastname"]}\nCedula: {estudiante["cedula"]}\nNota 1: {estudiante["nota 1"]}\nNota 2: {estudiante["nota 2"]}\nNota 3: {estudiante["nota 3"]}\nPromedio: {estudiante["promedio"]}')
            
    elif seleccion == '2' :
        
        print('------------------------------------------')
        print('Registrar estudiante\n') 
        
        while valNombre == False:
             
            nombre = input('Ingrese el nombre:\n')
            
            if len(nombre) == 0:
                
                print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                
            else:
                valNombre = True
        
        while valApellido == False:
            
            apellido = input('Ingrese el apellido:\n')
            
            if len(apellido)==0:
                
                print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                
            else:
                
                valApellido=True
        
        while valCedula == False:
            
            cedula = input('Ingrese la cedula:\n')
            is_number= cedula.replace('.','').isdigit()
            
            if is_number == True:
                
                cedula = int(cedula)
                valCedula = True
            else:
                cedula = None
                print('El dato ingresado es incorrecto, vuelva a ingresar\n')
           
        
        # Validaciones para que los numeros ingresados sean numeros enteros o flotantes con '.' , no strings
        
        while validacion == False:
            
            nota_1 = input('Ingrese la primera nota:\n')
            is_number = nota_1.replace('.','').isdigit()
            
            if is_number == True:
                
                nota_1 = float(nota_1)
                validacion = True
                
            elif '.' in nota_1:
                
                nota_1 = float(nota_1)
                validacion = True
                is_number = None
                
            elif ',' in nota_1:
                nota_1 = nota_1.replace(',','.')
                nota_1 = float(nota_1)
                validacion = True
                is_number = None
                
            else:
                
                nota_1 = None
                print('El dato ingresado es incorrecto, vuelva a ingresar\n')
           
        
        while validacion2 == False:
                
            nota_2 = input('Ingrese la segunda nota:\n')
            is_number = nota_2.replace('.','').isdigit()
            
            if is_number == True:
                
                nota_2 = float(nota_2)
                validacion2 = True
                
            elif '.' in nota_2:
                
                    nota_2 = float(nota_2)
                    validacion2 = True
                    is_number = None
                    
            elif ',' in nota_2:
                
                    nota_2 = nota_2.replace(',','.')
                    nota_2 = float(nota_2)
                    validacion2 = True
                    is_number = None
            else:   
                
                    nota_2 = None
                    print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                    
        
        while validacion3 == False:
            
            nota_3 = input('Ingrese la tercera nota:\n')
            
            is_number = nota_3.replace('.','').isdigit()
            
            if is_number == True:
                
                nota_3 = float(nota_3)
                validacion3 = True
                
            elif '.' in nota_3:
                
                    nota_3 = float(nota_3)
                    validacion3 = True
                    is_number = None
                    
            elif ',' in nota_3:
                
                    nota_3 = nota_3.replace(',','.')
                    nota_3 = float(nota_3)
                    validacion3 = True
                    is_number = None
                    
            else:
                
                    nota_3 = None
                    print('El dato ingresado es incorrecto, vuelva a ingresar\n')
           
        promedio = round(float(float( nota_1 + nota_2 + nota_3 )/3),2)
        
        # nuevo diccionario con los datos ingresados
        
        nuevo_estudiante = {'name': nombre,'lastname':apellido,'cedula':cedula,'nota 1': nota_1,'nota 2':nota_2,'nota 3':nota_3, 'promedio':promedio} 
        
        # y agregar el nuevo diccionario a la lista de estudiantes1
        
        estudiantes.append(nuevo_estudiante)
        
    elif seleccion == '3' :
        
        print('------------------------------------------')
        print('Actualizar estudiante:\n')

        while valCedula == False:
            
            cedulaComp = input('Ingrese la cedula del estudiante:\n')
            is_number= cedulaComp.replace('.','').isdigit()
            
            if is_number == True:
                
                cedulaComp = int(cedulaComp)
                valCedula = True
                
            else:
                
                cedulaComp = None
                print('El dato ingresado es incorrecto, vuelva a ingresar\n')
        
        for estudiante in estudiantes:
        
            if  estudiante['cedula'] ==  cedulaComp:
                
                print('Coincide la cedula\n')
                
                
                while valNombre == False:
             
                    nombre_Act = input('Ingrese el nombre:\n')
                
                    if len(nombre_Act) == 0:
                    
                        print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                    
                    else:
                        valNombre = True
                
                while valApellido == False:
                
                    apellido_Act = input('Ingrese el apellido:\n')
                
                    if len(apellido_Act) == 0:
                    
                        print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                    
                    else:
                        valApellido = True
                
                valCedula = False
                
                while valCedula == False:
                    
                    cedula_Act = input('Ingrese la cedula:\n')
                    is_number = cedula_Act.replace('.','').isdigit()
                    
                    if is_number == True:
                        
                        cedula_Act  = int(cedula_Act)
                        valCedula = True
                        
                    else:
                        
                        cedula_Act  = None
                        print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                
                
                # Validacion para que los numeros ingresados sean numeros enteros o flotantes, no strings
                
                while validacion == False: 
                    
                    nota_1_Act  = input('Ingrese la primera nota:\n')
                    is_number = nota_1_Act.replace('.','').isdigit()
                    
                    if is_number == True:
                        
                        nota_1_Act = float(nota_1_Act)
                        validacion = True
                        
                    elif '.' in nota_1_Act:
                        
                        nota_1_Act = float(nota_1_Act)
                        validacion = True
                        is_number = None
                        
                    elif ',' in nota_1_Act:
                        
                        nota_1_Act = nota_1_Act.replace(',','.')
                        nota_1_Act = float(nota_1_Act)
                        validacion = True
                        is_number = None
                        
                    else:
                        
                        nota_1_Act = None
                        print('El dato ingresado es incorrecto, vuelva a ingresar:\n')
                
                
                while validacion2 == False:
                        
                    nota_2_Act = input('Ingrese la segunda nota:\n')
                    is_number = nota_2_Act.replace('.','').isdigit()
                    
                    if is_number == True:
                        
                        nota_2_Act = float(nota_2_Act)
                        validacion2 = True
                        
                    elif '.' in nota_2_Act:
                        
                            nota_2_Act = float(nota_2_Act)
                            validacion2 = True
                            is_number = None
                            
                    elif ',' in nota_2_Act:
                        
                            nota_2_Act = nota_2_Act.replace(',','.')
                            nota_2_Act = float(nota_2_Act)
                            validacion2 = True
                            is_number = None
                    else:   
                        
                            nota_2_Act = None
                            print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                    
        
                while validacion3 == False:
            
                    nota_3_Act = input('Ingrese la tercera nota:\n')
                
                    is_number = nota_3_Act.replace('.','').isdigit()
                
                    if is_number == True:
                    
                        nota_3_Act = float(nota_3_Act)
                        validacion3 = True
                    
                    elif '.' in nota_3_Act:
                        
                        nota_3_Act = float(nota_3_Act)
                        validacion3 = True
                        is_number = None
                            
                    elif ',' in nota_3_Act:
                        
                        nota_3_Act = nota_3_Act.replace(',','.')
                        nota_3_Act = float(nota_3_Act)
                        validacion3 = True
                        is_number = None
                            
                    else:
                        
                            nota_3_Act = None
                            print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                
                promedio_Act = round(float(float( nota_1_Act + nota_2_Act + nota_3_Act )/3),2)
            
                # nuevo diccionario con los datos ingresados
            
                nuevo_estudiante_Act = {'name': nombre_Act,'lastname':apellido_Act,'cedula':cedula_Act,'nota 1': nota_1_Act,'nota 2':nota_2_Act,'nota 3':nota_3_Act, 'promedio':promedio_Act} 
                nuevo_estudiante.update(nuevo_estudiante_Act)
                
                # y agregar el nuevo diccionario a la lista de estudiantes
                
                break
            
            else:
                
                pass
                
        
    elif seleccion == '4' :
        
        confimacion = True
        conf = ''
        print('------------------------------------------')
        print('Eliminar estudiante:\n')
        
        while valCedula == False:
            
            cedulaComp = input('Ingrese la cedula del estudiante:\n')
            is_number= cedulaComp.replace(' ','').isdigit()
            
            if is_number == True:
                
                cedulaComp = int(cedulaComp)
                valCedula = True
                
            else:
                
                cedulaComp = None
                print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                
        while confimacion:
            
            conf=input('Seguro que lo quiere eliminar? Escriba Y o N para confirmar\n')
            
            if conf== 'Y':
                for estudiante in estudiantes:
        
                    if  estudiante['cedula'] ==  cedulaComp:
                
                        int(cedulaComp)
                        estudiantes.remove(estudiante)
                        print ( f' Estudiante {cedulaComp} fue eliminado\n')
                        confimacion=False
                
            elif conf == 'N':
                
                break
            
            else:
                
                conf = None
                print('El dato ingresado es incorrecto, vuelva a ingresar\n')
                
                    
        
                
    elif seleccion == '5' :
        
        break
    
    else :
        print('El dato ingresado no esta dentro de las opciones, ingrese otro:\n')
        
        