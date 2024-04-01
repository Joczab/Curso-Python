from datetime import date
from datetime import datetime

today = date(2024,4,27)
print('Hoy',today)




 while valcodigo:
                            
                            print('Filtrar Por Código\n')
                            codigo_seleccionado = input('Ingrese El Código:\n')
                            is_number = codigo_seleccionado.isdigit()
                                
                            if is_number == True:
                                    
                                    codigo_seleccionado == int(codigo_seleccionado)
                                    lista_tareas_codigo(codigo_seleccionado)
                                    print()
                                    valcodigo = False
                                    
                            else:
                                    
                                    codigo_seleccionado = None
                                    print('El dato ingresado es incorrecto, vuelva a ingresar\n')
    
    

now = datetime.now()
print('Ahora',now)