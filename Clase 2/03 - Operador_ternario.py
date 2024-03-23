x = 10
y = 15
text = ''
text2 = ''
if y>x:
    text = 'y > x'
else:
    text = 'x > y'
    
print(text)

print('--------------------------------------------')

# Condicional con ternarios

text2= 'y > x' if y > x else 'x > y'

print(text2)

print(text == text2)