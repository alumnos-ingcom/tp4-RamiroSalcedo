################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrrenheit(centigrados):
    
    grados_f = (centigrados * 9 / 5) + 32
    
    print(f"{centigrados} grados centigrados son equivalentes a {grados_f} grados fahrenheit")
    
    return grados_f

def convertir_a_centigrados(fahrenheit):
    
    grados_c = (fahrenheit - 32) * 5 / 9
    
    print(f"{fahrenheit} grados fahrenheit son equivalentes a {grados_c} grados celcius")
    
    return grados_c



def prueba():
    convertir_a_fahrrenheit(0)
    convertir_a_centigrados(32)
    pass

if __name__ == "__main__":
      prueba()
