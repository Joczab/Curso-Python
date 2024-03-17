from cmath import isclose


print(1.1+2.0)

x = 3.3
y = 1.1 + 2.2

print (x)
print (y)

print( x==y )

# Forma 1 de solucion

y_str = format(y, '.1f')
print(y_str)

print(str(x) == y_str)

print("----------------------------------")

# Forma 2 de solucion 

y_rounded= round(y,1)
print ('ROUNDED: ', y_rounded)

print( x == y_rounded)

print("----------------------------------")

# Forma 3 

margin = 0.00001

# Valor Absoluto

print(abs(x-y) < margin)

print("----------------------------------")

# Forma 4

print(" ISCLOSE ",isclose(x,y,))
print(" ISCLOSE ",isclose(x,y, abs_tol=margin))
