################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    
    if numero > 0:
        print(f"El Numero {numero} es positivo")
        
    elif numero < 0:
        print(f"El Numero {numero} es negativo")
        
    else:
        print(f"El Numero es {numero}")
        

def prueba():
    signo(-3)
    pass

if __name__ == "__main__":
    prueba()