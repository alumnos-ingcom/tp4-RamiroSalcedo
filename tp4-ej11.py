################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_palindromo(texto):
    
    cadena = texto.lower()
    cadena = cadena.replace(' ', '')

    
    if str(cadena) == str(cadena)[::-1]:
        palindromo = True
        
    else:
        palindromo = False
            
    return palindromo 





def prueba():
    texto = str(input("Ingrese frase o palabra: "))  
    condicion = es_palindromo(texto)
    print(condicion)
    
    

if __name__ == "__main__":
    prueba()
