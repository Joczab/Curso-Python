from json import dump, load
from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from main import DataBaseType, Movie, MoviesType

movies_routes = APIRouter()

@movies_routes.get('/movies/', tags= ['movies'])
def get_movie_by_category(category: str = Query(min_length = 5, max_length = 15)):
    # obtener pelicula por categoria
    with open('db.json','r')as jsonfile:
        data = load(jsonfile)
        movies: MoviesType = data['movies']
        
        result = [movie for movie in movies if movie['category'].lower() ==category.lower()]
    return result

@movies_routes.post('/movies', tags=['movies'])
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

@movies_routes.put('/movies/{id}',tags=['movies'])
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

@movies_routes.delete('/movies/{id}',tags=['movies'])
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

@movies_routes.get('/users', tags=['users'])
def get_users():
    # obtener las peliculas
    with open('db.json','r') as jsonfile:
        data = load(jsonfile)
        
        return JSONResponse(content=data['users'],status_code=status.HTTP_200_OK) 