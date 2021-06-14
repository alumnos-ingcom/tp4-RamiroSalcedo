################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_primo(numero):
    
    
    if numero % 1 == 0:
        
        if numero % numero == 0:
            
            if numero % 2 == 0:
                
                return False
            
            else:
                
                return True
                
            

def prueba():
    numero = int(input("ingrese que numero quiere evaluar: "))
    prueba = es_primo(numero)
    print(prueba)
    
        
if __name__ == "__main__":
    prueba()