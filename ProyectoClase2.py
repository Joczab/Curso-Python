'''Proyecto en Python sobre elaborar una aplicación de tareas pendientes que le permita al usuario gestionar sus tareas'''

ciclo = True

while ciclo:
    
    seleccion = input('''
                      Gestor de tareas:

                      1. Lista de tareas
                      2. Filtrar Tareas
                      3. Añadir Tareas
                      4. Actualizar Tareas
                      5. Eliminar Tarea
                      6. Salir\n
                      ''')   
    
    match seleccion:
        case '1':
            print('------------------------------------------')
            print('Listar de Tareas:')
        case '2':
            print('------------------------------------------')
            print('Filtrar Tareas:')
        case '3':
            print('------------------------------------------')
            print('Añadir Tareas:')
        case '4':
            print('------------------------------------------')
            print('Actualizar Tareas:')
        case '5':
            print('------------------------------------------')
            print('Eliminar Tareas:')
        case '6':
            print('------------------------------------------')
            print('Salir')
        case _:
            print('------------------------------------------')
            print('El dato ingresado no esta dentro de las opciones, ingrese otro:\n')