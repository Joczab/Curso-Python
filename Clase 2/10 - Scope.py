# local

def obtener_un_numero():
    random_number = 50
    print(random_number)
    
    # scope anidado
    
    def obtener_un_letra():
        print(random_number)
        
        #scope global
        global random_letter
        random_letter = 'letra random'
        
        return '1' 
    
    obtener_un_letra()
    
    return 10

# random_number esta en un spoce local(funcion)
# print(random_number)

obtener_un_numero()
print('random letter:',random_letter)
print('--------------------------------------')

# build in 

print()
input()