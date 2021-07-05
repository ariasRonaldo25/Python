#esto es un comentario
print ("hola soy Ronaldo Arias")

"""
esto es un comentario multlinea.
"""

#variables

nombre="Ronaldo" 
altura= 180
year= 2021

print(f"{nombre} - {altura} - {str(year)} ")
#print( nombre +  " - "  +  altura  + " - " + str(year))

#entrada por teclado
sitioWeb = input("¿ cual es tú sitio web?")
print("El sitio web del usuario es: " + sitioWeb)

#condicionales
""""
altura= int(input("cual es tú altura"))

if( altura>=180):
    print("Eres una persona alta!!")
else:
    print("Eres una persona bajita!!")    
"""
#funciones
var_altura= int(input("cual es tú altura"))
def mostrarAltura(altura):
    altura= int(input("cual es tú altura"))

    resultado=""

    if( altura>=180):
       resultado="Eres una persona alta!!"
    else:
        resultado="Eres una persona bajita!!"
    return resultado

    
print(mostrarAltura(var_altura))


#listas

personas= [ "Ronaldo", "Rafael", "José"]
print(personas [0]) 

for persona in personas:
 print("-" + persona)

