#Definición de la función para sumar valores
def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

#LLamada de la función
print(sumar_valores(3,5,9))


#Definición de la función para multiplicar valores
def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

#LLamada de la función
print(multiplicar_valores(3,5,15))

#Definición de la función para restar valores
def restar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado -= numero
    return resultado

#LLamada de la función
print(restar_valores(30,2,1))

#Definición de la función para dividir valores
def dividir_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado /= numero
    return resultado

#LLamada de la función
print(dividir_valores(3,5,15))