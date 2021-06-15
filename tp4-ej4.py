################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(numero, otro_numero):
    
    """condiciones"""
    if numero < otro_numero:
        valor_retorno = -1
        
        
    elif numero > otro_numero:
        valor_retorno = 1
        
        
    else:
        valor_retorno = 0
        
        
    return valor_retorno
    
    
    
def prueba():
    numero = int(input("ingrese primer numero a comparar "))
    otro_numero = int(input("ingrese segundo numero a comparar "))
    retorno = compara(numero, otro_numero)
    print(retorno)
    

if __name__ == "__main__":
    prueba()