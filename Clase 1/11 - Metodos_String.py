

quote = 'Aprendiendo python '

# index 

print(quote.index('A'))
index_y = quote.index('y')
print(' INDEX Y', index_y )
print(' VALOR Y', quote[index_y] )

print("----------------------------------")
# find

index_y_find = quote.find('1')
print ('INDEX Y FIND', index_y_find)

print("----------------------------------")

# upper

print('Hello world'.upper())

print("----------------------------------")

# lowwer

print('Hello fweuqy'.lower())

print("----------------------------------")

# count

print ('Aprendiendo Python'.count('o'))

print("----------------------------------")

# Swapcase

print('Hello World'.swapcase())

print("----------------------------------")

# startswith

print('video/*'.startswith('video'))

print("----------------------------------")

# endswith

print('video/*'.endswith('/*'))

print("----------------------------------")

# title

print('welcome to the island'.title())

print("----------------------------------")

# isdigit

print('IS DIGIT','625.4'.isdigit())

print("----------------------------------")

# replace

value = input('elija un numero: ')
is_number = value.replace('.','').isdigit()

if is_number == True:
        
    print('Si es un valor numerico')
    
    if '.' in value:
        value =  float(value)
    else:
        value = int(value)
        
print(value)
print(type(value))

'''
print ('Replace','654.10'.replace('.','').isdigit())

flotante = '654.10'

if '.' in flotante :
    flotante = float(flotante)
else:
    flotante = int(flotante)
      '''

print("----------------------------------")

# Slicing

print(quote[1])

print (len(quote))

print ( quote [ len(quote) - 1 ])
