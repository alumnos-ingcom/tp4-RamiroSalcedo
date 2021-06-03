################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    
    if numero > 0:
        
        
        signo = '+'
        
    elif numero < 0:
        
        
        signo = '-'
        
    else:
        
        
        signo = 'neutro'
        
    return signo

def prueba():
    numero = int(input("Ingrese numero que quiera evaluar "))
    resultado = signo(numero)
    print(resultado)
    

if __name__ == "__main__":
    prueba()