is_running = True
counter = 0


numbers = []

while is_running == True:
    
    counter = counter + 1
    numbers.append(counter)
    
    print(counter)
    
    if counter == 5:
        
        break
        
        
print(counter)
print(numbers)

print('xxxxxxxxxxxxxxxxxxx')

numbers=[ 1 , 2 , 3 , 4 ]
index = 0

print('Longitud el arreglo> ',len(numbers))

while index < len(numbers):
    number = numbers[index]
    index = index + 1
    
    if number == 2: 
     continue
    
    
    print(number)
   
    
    
    