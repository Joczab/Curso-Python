car = {
    'model': 'X-1500',
    'brand': 'Tesla',
}

car2 = car
car2 ['owner']= 'Ryan'


print(car,car2)

print('--------------------------------------------')

# Copy

car3 = car.copy()

car3['owner'] = 'Carlojavier'
print(car)
print(car3)

print('--------------------------------------------')

# Spread (dicccionarios )

car4 = {**car,'owner': 'Jesudavi'}

print(car4)

# Spread (listas)

numbers = list(range(0, 6))
print(numbers)

numbers.append(7)
print(numbers)

print(id(numbers))

numbers = [*numbers,10,20,30]
print('con un spread',numbers)

print(id(numbers))
