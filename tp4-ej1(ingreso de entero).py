################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
         
        pass

def ingreso_entero(mensaje):
    
    numero = (input(mensaje + ":"))
    try:
                                                            
        entero = int(numero)
        
    except ValueError as err:
        
        numero = int(input("ERROR no ingreso un numero intente nuevamente: "))
        entero = numero
        
              
    return entero

            
def prueba():
    mensaje = ("ingrese un numero entero")
    valor = ingreso_entero(mensaje)
    print(valor)
    

if __name__ == "__main__":
      prueba()

