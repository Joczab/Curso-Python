estudiante = {
    'name':'',
    'lastname': '',
    'cedula': 0 ,
    'nota 1': 0.00,
    'nota 2': 0.00,
    'nota 3': 0.00,
    'promedio': 0.00
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
       # for i in estudiante:
        #    for clave,valor in enumerate(estudiante):
         #       print(f'{clave}:{valor}')
          #  print()
        
        for index,estudiante in enumerate(estudiantes):
            
            print ('\nEstudiante :',index )
            print(f'\nNombre: {estudiante["name"]}\nApellido: {estudiante["lastname"]}\nCedula: {estudiante["cedula"]}\nNota 1: {estudiante["nota 1"]}\nNota 2: {estudiante["nota 2"]}\nNota 3: {estudiante["nota 3"]}\nPromedio: {estudiante["promedio"]}')
            
        

    elif seleccion == '2' :
        print('------------------------------------------')
        print('Registrar estudiante ') 
        
        nombre = input('Ingrese el nombre: ')
       
        apellido = input('Ingrese el apellido: ')
        
        cedula = int(input('Ingrese la cedula: '))
        
        nota_1 = float(input('Ingrese la primera nota: '))
        
        nota_2 = float(input('Ingrese la segunda nota: '))
        
        nota_3 = float(input('Ingrese la tercera nota: '))
        
        promedio = round(float(float( nota_1 + nota_2 + nota_3 )/3),2)
        
        # nuevo diccionario con los datos ingresados
        
        nuevo_estudiante = {'name': nombre,'lastname':apellido,'cedula':cedula,
                            'nota 1': nota_1,'nota 2':nota_2,'nota 3':nota_3, 'promedio':promedio} 
        
        # y agregar el nuevo diccionario a la lista de estudiantes1
        
        estudiantes.append(nuevo_estudiante)
        
    elif seleccion == '3' :
        print('------------------------------------------')
        print('Actualizar estudiante:')
        
        cedulaComp = input('Ingrese la cedula del estudiante: ')
        
        ''' if  estudiantes[estudiante['cedula']]  cedulaComp:
            print('correcto')    
        else :
            print('No coincide la cedula ')
        '''
        # estudiantes[len(estudiantes)-1] = cedulaComp
    elif seleccion == '4' :
        print('------------------------------------------')
        print('Eliminar estudiante:')
    elif seleccion == '5' :
        break
    else :
        print('El dato ingresado no esta dentro de las opciones, ingrese otro: ')