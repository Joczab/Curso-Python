'''Proyecto en Python sobre elaborar una aplicación de tareas pendientes que le permita al usuario gestionar sus tareas'''
from datetime import date

dic_tareas = [
    {
        'codigo': '123',
        'titulo':'Aprender Python',
        'descripcion': 'Prueba de los diccionarios',
        'status' : 'Completado' , #status = Completada o Pendiente        
        'fecha_de_creacion' : date(2003,4,27) #DD-MM-YYYY
    },
    {
        'codigo': '456',
        'titulo':'Aprender un libro',
        'descripcion': 'Prueba de los diccionarios',
        'status' : 'Pendiente' , #status = Completada o Pendiente     
        'fecha_de_creacion' : date(2003,1,23) #DD-MM-YYYY
    }
]

ciclo = True

#funcion de tareas completadas
def lista_tareas_completadas():
    print('------------------------------------------')
    print('Tareas Completadas:')
    tareas_completadas = [tarea for tarea in dic_tareas if tarea['status'] == 'Completado']
    for index, tarea in enumerate(tareas_completadas,1):
        print('------------------------------------------')
        print(f'Tarea N: {index}.')
        print()
        for key, value in tarea.items():
            print (f'{key.capitalize()}: {value}')
    print('------------------------------------------')
    print()
        
#funcion de tareas pendientes
def lista_tareas_pendientes():
    print('------------------------------------------')
    print('Tareas Pendientes:')
    tareas_pendientes = [tarea for tarea in dic_tareas if tarea['status'] == 'Pendiente']
    for index, tarea in enumerate(tareas_pendientes,1):
        print('------------------------------------------')
        print(f'Tarea N: {index}.')
        print()
        for key, value in tarea.items():
            print (f'{key.capitalize()}: {value}')
    print('------------------------------------------')
    print()
        
#funcion de filtrado por codigo
def lista_tareas_codigo(num):
    print('------------------------------------------')
    print('Tareas por Codigo:')
    tareas_codigo = [codigo for codigo in dic_tareas if codigo['codigo'] == num ]
    for index,codigo in enumerate(tareas_codigo,1):
        print('------------------------------------------')
        print(f'Tarea N: {index}.')
        print()
        for key, value in codigo.items():
            print(f'{key.capitalize()}: {value}')
    print('------------------------------------------')
    print()

#funcion de filtrado por titulo
def lista_tareas_titulo(titulo):
    print('------------------------------------------')
    print('Tareas por Título:')
    tareas_titulo =  list(filter(lambda tarea: tarea if titulo_seleccionado.capitalize() in tarea['titulo'].capitalize() else False,dic_tareas))
    
    if tareas_titulo is not None:
        for index,tarea in enumerate(tareas_titulo,1):
            print('\nTarea N:',index)
            for key,value in tarea.items():
                print(f'{key.capitalize()}:{value}')
        print('------------------------------------------')
        print()
                
    else:
        print('No se han encontrado tareas que coincidan.')

#funcion de filtrado por fecha
def lista_tareas_fecha():
    
    tareas_fecha = [fecha for fecha in dic_tareas if fecha['fecha_de_creacion'] == fecha_seleccionada]
    for index,fecha in enumerate(tareas_fecha,1):
        print('------------------------------------------')
        print(f'Tarea N: {index}.')
        print()
        for key,value in fecha.items():
            print(f'{key.capitalize()}: {value}')
    print('------------------------------------------')
    print()

#funcion para validar que sea un numero
def validar_numero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False       
    
#funcion para validar que la fecha sea numerica 
def ingresar_fecha():
    while True:
        
        dia = input("Ingrese el día: ")
        mes = input("Ingrese el mes: ")
        año = input("Ingrese el año: ")
        
        if validar_numero(dia) and validar_numero(mes) and validar_numero(año):
            return  date(int(año), int(mes), int(dia))
        else:
            print("Por favor, ingrese valores numéricos para día, mes y año.")
        
        
    

        
#funcion para que el codigo no sea repetido
def codigo_no_rep(codigo): # creo q es asi
    codigo_val = lambda codigo: False if codigo == ['codigo'] else True
    return codigo_val

#funcion para que el titulo sea vacio
def titulo_no_vacio(titulo):
        
    if len(titulo.strip()) > 0 and len(titulo) <= 20:
        return True                 
    else:
        titulo = input('El Título ingresado no es valido, vuelva a ingresar:\n')
    

#funcion para verificar que la id no se repita
def validar_codigo(codigo):
    pass
    

while ciclo:
    
    esmanzana = True
    filtro = None
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
            print('Lista de Tareas:\n')
            
            while esmanzana:
                
                filtro = input('Para filtrar las tareas seleccione \n1 Completadas \n2 Ausentes \n3 Menu Principal\n ')
            
                match filtro:
                    case '1':
                        lista_tareas_completadas()
                    case '2':
                        lista_tareas_pendientes()
                    case '3':
                        esmanzana = False
                    case _:
                        print('------------------------------------------')
                        print('El dato ingresado no esta dentro de las opciones, ingrese otro:\n')
                        
        case '2':
            
            print('------------------------------------------')
            print('Filtrar Tareas:')
            
            while esmanzana:
                
                filtro = input('Para filtrar las tareas seleccione \n1 Por Código \n2 Por Título \n3 Por Fecha(Ingresar: Día-Mes-Año)\n4 Menu Principal\n')
                print()
                
                match filtro:
                    
                    case '1':
                        valCodigo = True
                        while valCodigo:
                            
                            print('Filtrar Por Código\n')
                            codigo_seleccionado = input('Ingrese El Código:\n')    
                            
                            if validar_numero(codigo_seleccionado) == True:
                                lista_tareas_codigo(codigo_seleccionado)
                                print()
                                valCodigo = False
                            else:
                                pass
                            
                            
                            
                    case '2':
                        
                            
                            print('Filtrar Por Título\n')
                            titulo_seleccionado = input('Ingrese el Título:\n')
                            
                            titulo_no_vacio(titulo_seleccionado)
                                
                            lista_tareas_titulo(titulo_seleccionado)
                            
                                
                    case '3':
                        
                            print('Filtrar Por Fecha:')
                            
                            fecha_seleccionada = ingresar_fecha()
                            lista_tareas_fecha()
                            
                    case '4':
                        esmanzana = False
                    case _:
                        print('------------------------------------------')
                        print('El dato ingresado no esta dentro de las opciones, ingrese otro:\n')
            
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
            print('Finalizando el programa')
            ciclo = False
        case _:
            print('------------------------------------------')
            print('El dato ingresado no esta dentro de las opciones, ingrese otro:\n')