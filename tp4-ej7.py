################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def division_lenta(dividendo, divisor):
    
    cociente = float(0)
    
    while dividendo >= divisor:
        
        dividendo = dividendo - divisor
        
        cociente = cociente + 1
        
        
    print(f"El cociente es: {cociente}")
    print(f"El resto es: {dividendo}") 
    return dividendo, cociente



def prueba():
    
    division_lenta(55, 3)
    pass

if __name__ == "__main__":
    prueba()