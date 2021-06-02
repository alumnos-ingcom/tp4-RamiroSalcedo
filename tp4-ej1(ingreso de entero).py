################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
         
        pass

def recibir_entero():
    
    numero = (input("Ingrese un numero:"))
    try:
                                                            
        entero = int(numero)
        
    except ValueError as err:
        
        numero = int(input("ERROR no ingreso un numero intente nuevamente: "))
        entero = numero
        
              
    return entero

            
def prueba():         
    valor = recibir_entero()
    print(valor)
    pass

if __name__ == "__main__":
      prueba()

