################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def ingreso_entero_reintento():
      
    try:
        for i in range(1):
            
            numero = (input(f"Ingrese un numero: "))
            entero = int(numero)

                   
    except ValueError as err:
        raise IngresoIncorrecto("Error no ha ingresado un valor numerico") from err
        
        
        
    return entero


def prueba():
    valor = ingreso_entero_reintento()
    print(valor)
    pass

if __name__ == "__main__":
    prueba()