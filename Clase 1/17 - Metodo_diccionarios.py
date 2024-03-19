developer = {
    'name ':' Jose ',
    'lastname': 'Perez',
    'age' : 30
    
}

# Get
name = developer.get('a')

print (name)


if not name :
    print('No existe')
else: 
    print ('Su existe')
    
    
# Update

developer.update({'name ': 'Alejandro'})
developer.update({'is_senior': True})
print(developer)

# Update agregar

developer.update({'is_senior':False})
print(developer)

# Remover

developer.pop('is_senior')
print(developer)

# popItem (elimina el ultimo valor)

developer.popitem()
print(developer)

# clear : elimina todos los valores
developer.clear()
print(developer)

#SUAS

print ('-------------------------------------------')

person = {
    'name': 'Ronald',
    'lastmane': 'Abu Saleh'
        
}
person1 = person
print(person1)

person1['name'] = 'Leo'
print(person1)
print(person)

print ('-------------------------------------------')

# copy

person2 = person.copy()
person2['name']='Manuel'
print(person)
print(person2)

