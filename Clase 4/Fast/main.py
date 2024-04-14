from json import load, dump
from operator import getitem
from fastapi import Body, FastAPI, Path, Query, status
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List, Dict, Optional, Union

from pydantic import BaseModel, Field
from logger import logger

app = FastAPI()

app.title = 'Mi primera app con FastAPI'
app.description = 'Descripcion como ejemplo'
app.version = '1.0.0'

# tipado de datos
UserType = Dict[str,Union[str]]
UsersType = List[UserType]

MovieType = Dict[str, Union[str, int, float]]
MoviesType = List[MovieType]

DataBaseType = Dict [str,Union[UsersType, MovieType]]

# Clases de validacion

class Movie(BaseModel):
    
    id: Optional[int]
    title: str = Field(default = 'Titulo de pelicula', min_length = 5, max_length = 20)
    overview: str = Field(default='Descripcion de pelicula', min_length = 5)
    year: int = Field(default=2024, le=2024)
    rating: float = Field(default=9.8, gt=0, le=10)
    category: str = Field(min_length = 5, max_length = 15)
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 20,
                    'title': 'Un titulo de ejemplo',
                    "description": "A very nice Item",
                    "year": 2024,
                    "rating": 3.2,
                    'category': 'Action'
                }
            ]
        }
    }

# rutas

@app.get('/home',tags=['home'])
def home():
    return 'Hola mundo'

@app.get('/html',tags=['html'])
def render_html():
    # primera forma
    # return HTMLResponse(content = '<h1>Hello world</h1>')
    
    with open('index.html','r') as htmlfile:
        html = htmlfile.read()
        
        return HTMLResponse(content=html,status_code=200)
    
@app.get('/movies', tags=['movies'])
def get_movies():
    logger.debug(f'Esto es un mensaje tipo print')
    # obtener las peliculas
    with open('db.json','r') as jsonfile:
        data = load(jsonfile)
        movies = data['movies']
        
        return JSONResponse(content=movies,status_code=status.HTTP_200_OK)
    
@app.get('/movies/{id}',tags=['movies'])
def get_movie(id: int):
    # obtener pelicula por id
    
    with open('db.json','r') as jsonfile:
        data = load(jsonfile)
        movies = data ['movies']
        
        for movie in movies:
            if movie['id'] == id:
                return JSONResponse(content=movies,status_code=status.HTTP_200_OK)
            
        return {}
    
# uso de parametros query (en este caso es category)
@app.get('/movies/', tags= ['movies'])
def get_movie_by_category(category: str = Query(min_length = 5, max_length = 15)):
    # obtener pelicula por categoria
    with open('db.json','r')as jsonfile:
        data = load(jsonfile)
        movies: MoviesType = data['movies']
        
        result = [movie for movie in movies if movie['category'].lower() ==category.lower()]
    return result

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    # logger.debug(type(movie.model_dump()), movie.model_dump())
    
    # id, title = getitem('id','title')(movie.model_dump())
    
    # logger.debug(f'{id} {title}')   
    new_movie = {
        'id': movie.id,
        'title': movie.title,
        'overview': movie.overview,
        'year': movie.year,   
        'rating': movie.rating,
        'category': movie.category
    }
    
    with open ('db.json','r') as jsonfile:
        data: DataBaseType = load(jsonfile)
        
    # insertar pelicula
    data['movies'].append(new_movie)
    
    #guardamos en nuestro db.json
    
    with open('db.json','w') as file:
        dump(data, file, indent=2)
        
    return JSONResponse(content = {'message':'Pelicula creada con exito'},status_code=status.HTTP_200_OK)

@app.put('/movies/{id}',tags=['movies'])
def update_movie(id: int, movie: Movie):
    with open ('db.json','r') as jsonfile:
        data = load(jsonfile)
        
    # actualizar pelicula
    
    for movie in data['movies']:
        if movie['id'] == id:
            movie['title'] = movie.title
            movie['overview'] = movie.overview
            movie['year'] = movie.year
            movie['rating'] = movie.rating
            movie['category'] = movie.category
            
    # guardamos nuestro db.json
    with open('db.json','w') as file:
        dump(data, file, indent = 2)
        
    return JSONResponse(content={'message':'Pelicula actualizada con exito'}, status_code=status.HTTP_200_OK)

@app.delete('/movies/{id}',tags=['movies'])
def delete_movie(id : int):
    
    with open('db.json', 'r') as jsonfile:
        data = load(jsonfile)
        movies = data['movies']
    
    # filtramos las peliculas
    
    result = [movie for movie in movies if movie['id'] != id]
    
    # pasamos las peliculas menos la del id que pasamos por parametro
    
    data ['movies'] = result
    
    with open ('db.json', 'w') as file:
        dump (data, file, indent = 2 )
    
    return f'Pelicula con el id {id} ha sido eliminada con exito'

@app.get('/users', tags=['users'])
def get_users():
    # obtener las peliculas
    with open('db.json','r') as jsonfile:
        data = load(jsonfile)
        
        return JSONResponse(content=data['users'],status_code=status.HTTP_200_OK) 