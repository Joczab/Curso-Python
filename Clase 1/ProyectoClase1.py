estudiante1 = {
    'name ':' Jose ',
    'lastname': 'Zabala',
    'cedula': 29691806,
    'nota 1': 10,
    'nota 2': 10,
    'nota 3': 10,
    'promedio': 10
}
estudiante2 = {
    'name ':' Jesus',
    'lastname': 'Leal',
    'cedula': 29999470,
    'nota 1': 10,
    'nota 2': 10,
    'nota 3': 10,
    'promedio': 10    
}
estudiante3 = {
    'name ':' Ruben',
    'lastname': 'Valbuena',
    'cedula': 28123456,
    'nota 1': 10,
    'nota 2': 10,
    'nota 3': 10,
    'promedio': 10
}
estudiantes = [estudiante1,estudiante2,estudiante3]

promedio = estudiante1['nota 1']
print(promedio)

ciclo = True
while ciclo:

    seleccion = int(input('''
                          Gestion de estudiante universitario.
                          Seleccione la seccion:
                          1. Listado de estudiantes.
                          2. Registrar estudiante.
                          3. Actualizar estudiante.
                          4. Eliminar estudiante.
                          5. Salir\n''')) 
    if seleccion == 1:
        print('------------------------------------------')
        print('Listado de estudiantes:\n')
        print (f'\n{estudiante1},\n{estudiante2},\n{estudiante3}')

    elif seleccion == 2 :
        print('------------------------------------------')
        print('Registrar estudiante:') 
        nombre = input('Ingrese nombre')
        estudiantes.append(nombre)
        
    elif seleccion == 3 :
        print('------------------------------------------')
        print('Actualizar estudiante:')
    elif seleccion == 4 :
        print('------------------------------------------')
        print('Eliminar estudiante:')
    elif seleccion == 5 :
        break
    else :
        print('El dato ingresado no esta dentro de las opciones, ingrese otro: ')