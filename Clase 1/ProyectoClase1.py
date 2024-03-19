''' este es un ejemplo, para entregar borrar esto 
y el estudiante de la lista de estudiantes'''

estudiante = {
    'name': 'Jose',
    'lastname': 'Zabala',
    'cedula': 123 ,
    'nota 1': 20 ,
    'nota 2': 20 ,
    'nota 3': 20 , 
    'promedio': 20
}

estudiantes = [estudiante]

ciclo = True
while ciclo:

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
            
        1

    elif seleccion == '2' :
        print('------------------------------------------')
        print('Registrar estudiante ') 
        
        nombre = input('Ingrese el nombre: ')
        '''while nombre != str:
            nombre = input('el nombre no es valido, ingreselo nuevamente: ')'''
            
        apellido = input('Ingrese el apellido: ')
        
        cedula = int(input('Ingrese la cedula: '))
        
      
        validacion = False
        validacion2 = False
        validacion3 = False
        
        # Validacion para que los numeros ingresados sean numeros enteros o flotantes, no strings
        
        while validacion == False:
            
            nota_1 = input('Ingrese la primera nota: ')
            is_number = nota_1.replace('.','').isdigit()
            
            if is_number == True:
                
                nota_1 = float(nota_1)
                validacion = True
                
            elif '.' in nota_1:
                
                nota_1 = float(nota_1)
                validacion = True
                is_number = None
                
            elif ',' in nota_1:
                
                nota_1 = float(nota_1)
                validacion = True
                is_number = None
            else:
                
                nota_1 = None
                print('El dato ingresado es incorrecto, vuelva a ingresar: ')
           
        
        while validacion2 == False:
                
            nota_2 = input('Ingrese la segunda nota: ')
            is_number = nota_2.replace('.','').isdigit()
            
            if is_number == True:
                nota_2 = float(nota_2)
                validacion2 = True
                
            elif '.' in nota_2:
                
                    nota_2 = float(nota_2)
                    validacion = True
                    is_number = None
                    
            elif ',' in nota_2:
                
                    nota_2 = float(nota_2)
                    validacion = True
                    is_number = None
            else:   
                    nota_2 = None
                    
                    print('El dato ingresado es incorrecto, vuelva a ingresar: ')
                    
        
        while validacion3 == False:
            nota_3 = input('Ingrese la tercera nota: ')
            
            is_number = nota_3.replace('.','').isdigit()
            
            if is_number == True:
                nota_3 = float(nota_3)
                validacion3 = True
                
            elif '.' in nota_3:
                
                    nota_3 = float(nota_3)
                    validacion = True
                    is_number = None
                    
            elif ',' in nota_3:
                
                    nota_3 = float(nota_3)
                    validacion = True
                    is_number = None
            else:
                    nota_3 = None
                    print('El dato ingresado es incorrecto, vuelva a ingresar: ')
           
        promedio = round(float(float( nota_1 + nota_2 + nota_3 )/3),2)
        
        # nuevo diccionario con los datos ingresados
        
        nuevo_estudiante = {'name': nombre,'lastname':apellido,'cedula':cedula,'nota 1': nota_1,'nota 2':nota_2,'nota 3':nota_3, 'promedio':promedio} 
        
        # y agregar el nuevo diccionario a la lista de estudiantes1
        
        estudiantes.append(nuevo_estudiante)
        
    elif seleccion == '3' :
        print('------------------------------------------')
        print('Actualizar estudiante:')
        
        cedulaComp = int(input('Ingrese la cedula del estudiante: '))
        
        for estudiante in estudiantes:
            if  estudiante['cedula'] ==  cedulaComp:
                print('correcto')    
            elif estudiante ['cedula'] != cedulaComp:
                print('No coincide la cedula ')
                
        # estudiantes[len(estudiantes)-1] = cedulaComp
    elif seleccion == '4' :
        print('------------------------------------------')
        print('Eliminar estudiante:')
    elif seleccion == '5' :
        break
    else :
        print('El dato ingresado no esta dentro de las opciones, ingrese otro: ')