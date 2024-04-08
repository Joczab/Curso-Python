# instalar despues py -m pip install request 

import requests
import json

def obtener_personajes():
    request = requests.get(url=('https://rickandmortyapi.com/api'))
    print(request)
    
    if request.status_code == 404:
        print ('La URL no existe')
        
    data = request.json()
    
    crear_json(data)
    return data

def crear_json(data): 
    
    with open('./rick_and_morty.json','w',encoding='utf-8') as jsonfile:
        
        json.dump(data, jsonfile,indent=4)
        
if __name__ == '__main__':
    
    data = obtener_personajes()
    print(data)
    