'''
Obtener una lista de diccionario desde un csv y determinar la cantidad de hombres y mujeres que hay en la lista
'''

from os.path import dirname
from pathlib import Path
import csv


def read_csv(path):
    with open(path, 'r' )as csvfile:
        reader_v2 = csv.DictReader(csvfile)
        #creamos un lector de achivos csv
        #reader = csv.reader(csvfile)
        return list(reader_v2)
        
        # extraer primera linea(nombres de columnas)
        
        #header = next(reader)
        
        #contendra todos los diccionarios del csv
        #data = []
        
        # print(header)
        
        #lee de la linea 2 en adelante por que se uso next en header
        #for row in reader:
         #   iterable = zip(header,row)
            
         #  user_dict = {key:value for (key,value)in iterable}
            
         #   data.append(user_dict)
            
            #print(user_dict)
            #print(list(iterable))
            
         #   return data
  
    

if __name__ == '__main__':
    
    # Extraer el path del csv
    path = Path(dirname(__file__) + '/data.csv').resolve()
    
    data = read_csv(path)
    #print(data[0])
    
    #counters
    male_counter = 0
    female_counter = 0
    for item in data:
        if item['gender'] == 'male': 
            male_counter += 1
        else: 
            female_counter += 1
            
    print('Numero de hombres: ',male_counter)
    print('Numero de mujeres: ',female_counter)
    #manejo de zip
    
    #a = [1,2,3]
    #b = [4,5,6]
    
    #c = zip(a , b)
    #print(list(c))
    