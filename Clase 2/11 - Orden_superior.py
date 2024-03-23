def sumar(x, y):
    return x+y
def multiplicar(x, y):
    return x * y
def restar(x,y):
    return x-y
def dividir(x,y):
    return x/y

'''Esta es la funcion de orden superior porque recibe una funcion como parametro '''

def calculadora(operacion, numero1, numero2):
    resultado = operacion(numero1,numero2)
    return resultado

resultado_sumar = calculadora(sumar,15,5)
print('Sumar:',resultado_sumar)
print('------------------------------')
resultado_multiplicar = calculadora(multiplicar,15,2)
print('Multiplicar:',resultado_multiplicar)
print('------------------------------')
resultado_restar = calculadora(restar,15,5)
print('Restar:',resultado_restar)
print('------------------------------')
resultado_dividir = calculadora(dividir,20,2)
print('Dividir:',resultado_dividir)


# Funcion de orden superior que devuelve una funcion

def funcion_principal(numero1):
    
    def funcion_secundaria(numero2):
        return numero1 + numero2
    return funcion_secundaria

#resultado1 es funcion
print('------------------------------')
resultado1 = funcion_principal(25)
print(resultado1)
print(resultado1(30))

