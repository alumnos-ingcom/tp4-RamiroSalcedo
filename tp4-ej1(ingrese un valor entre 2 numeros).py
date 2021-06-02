################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def recibir_entero_definido(valormax, valormin):
    
    """valores maximos definidos"""
    numero = (input(f"Ingrese un numero entre {valormin} y {valormax}: "))
    
    maximo = valormax
    minimo = valormin
    
    
    try:
        entero = int(numero)
        """Evalua que las condiciones se cumplan"""
        
        if entero >= maximo:
            print("error su numero excede el valor maximo admitido")
        elif entero <= minimo:
            print("error su numero excede el valor minimo admitido")
         
    except ValueError as err:
        """excepcion levantada"""
        raise IngresoIncorrecto("Error no ha ingresado un valor numerico") from err
    
    return entero


def prueba():
     
    minumero = recibir_entero_definido(100, 50)
    print(minumero)
    pass

if __name__ == "__main__":
    prueba()
