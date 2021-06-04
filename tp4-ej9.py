################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_primo(numero):
    
    resto = numero % 2
    
 
    evalua = resto != 0
    
    if evalua:
        """si evalua es true es un numero primo"""
        
    else:
        """si evalua es false no es un numero primo"""
        
    return evalua
    """retorna true o false"""




def prueba():
    numero = int(input("ingrese que numero quiere evaluar: "))
    prueba = es_primo(numero)
    print(prueba)
    
        
if __name__ == "__main__":
    prueba()