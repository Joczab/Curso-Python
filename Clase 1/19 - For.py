numbers = [1,2,3,4,5]

for number in numbers :
    if number == 2:
        break
    
    print(number)
    
    print('sssssssssssss')
    
    
for i  in range (1,10):
    print(i)    
    
for i in range(len(numbers)):
    print(i)
    
for index, value in enumerate(numbers):
    print('INDICE', index, 'VALOR', value)
    
else: 
    print('El ciclo ha terminado ')