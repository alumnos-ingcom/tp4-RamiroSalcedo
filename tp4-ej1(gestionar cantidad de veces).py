################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def ingreso_entero_reintento(mensaje, cantidad_intentos):
      
    try:
        for i in range(cantidad_intentos):
            
            numero = (input(mensaje + ": "))
            entero = int(numero)

                   
    except ValueError as err:
        raise IngresoIncorrecto("Error no ha ingresado un valor numerico") from err
        
        
        
    return entero


def prueba():
    
    mensaje = ("ingrese un numero")
    cantidad_intentos = int(input("Cuantas veces quiere que se repita?"))
    valor = ingreso_entero_reintento(mensaje, cantidad_intentos)
    
    print(valor)
    

if __name__ == "__main__":
    prueba()