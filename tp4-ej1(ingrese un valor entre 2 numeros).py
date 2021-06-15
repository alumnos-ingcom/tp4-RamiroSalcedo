################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def ingreso_entero_restringido(mensaje, valormax=10, valormin=0):
    
    """valores maximos definidos"""
    numero = (input(mensaje + ": "))
    
    maximo = valormax
    minimo = valormin
    
    
    try:
        entero = int(numero)
        """Evalua que las condiciones se cumplan"""
        if entero > maximo:
            raise IngresoIncorrecto("Error se ha excedido del valor maximo")
        elif entero < minimo:
            raise IngresoIncorrecto("Error se ha excedido del valor minimo")
         
    except ValueError as err:
        """excepcion levantada"""
        raise IngresoIncorrecto("Error no ha ingresado un valor numerico") from err
    
    return entero


def prueba():
    
    mensaje = (f"ingrese un numero entre 0 y 10")
    minumero = ingreso_entero_restringido(mensaje)
    print(minumero)
    

if __name__ == "__main__":
    prueba()
