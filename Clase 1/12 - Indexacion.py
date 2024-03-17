quote = 'Soy desarrollador'

print ('LONGITUD ',len(quote))
print("POSICION 2",quote[1])

# Forma 1 de obtener la ultima posicion

print(' ULTIMA POSICION',quote[len(quote)-1])

print("----------------------------------")

# Forma 2

print(quote[-1])

# Slicing (cortes de string)

print(quote[4::2])

index_d = quote.index('d')
print (index_d)

print(quote[index_d:8])
