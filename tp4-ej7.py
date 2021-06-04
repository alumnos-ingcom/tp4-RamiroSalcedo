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
        
        

    return cociente, dividendo



def prueba():
    numero = float(input("ingrese dividendo "))
    otro_numero = float(input("ingrese divisor "))
    cociente, resto = division_lenta(numero, otro_numero)
    print(f"El cociente: {cociente}")
    print(f"El resto es: {resto}")


if __name__ == "__main__":
    prueba()