################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    
    total = numero + otro_numero
    
    if numero >= otro_numero:
        
        contador = otro_numero
        
        while contador <= total:
            
            print(f"{contador} + 1 ") 
            contador = contador + 1
    else:
        
        contador = numero
        
        while contador <= total:
            
            print(f"{contador} + 1 ")
            contador = contador + 1
           
    print(f"= {total}")
    
    
    
def prueba():
    
    suma_lenta(2, 42)
    pass

if __name__ == "__main__":
    prueba()