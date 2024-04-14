from threading import Thread
from time import sleep
import threading
import os

def get_users():
    sleep(2)
    
    print('ID de procesos del hilo get_users ',os.getpid())
    print('Nombre del proceso del hilo get_users ', threading.current_thread().name)
    print('Usuarios obtenidos: ')
    # return ['User 1','User 2']

def get_products():
    sleep(5)
    
    print('ID de procesos del hilo get_products ',os.getpid())
    print('Nombre del proceso del hilo get_products ', threading.current_thread().name)
    print('Productos obtenidos: ')    
    # return ['Product 1', 'Product 2']

def complex_calculation(x: int, y: int):
    global result
    result = x + y

thread1 = Thread(target=get_users, args=(),name = 'Get users')
thread1.start()

thread2 = Thread(target=get_products, args=(),name = 'Get products')
thread2.start()

thread3 = Thread(target=complex_calculation,args=(10,20),name = 'Complex Calculations')
thread3.start()
thread3.join()


print('Termino el proceso.', os.getpid())

print('Resultado de calculo complejo: ',result)

if __name__ == '__main__':
    
    print('ID del proceso principal.',os.getpid())
    
