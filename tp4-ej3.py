################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrrenheit(centigrados):
    
    grados_f = (centigrados * 9 / 5) + 32
    
    
    
    return grados_f

def convertir_a_centigrados(fahrenheit):
    
    grados_c = (fahrenheit - 32) * 5 / 9
    
    
    
    return grados_c



def prueba():
    centigrados = float(input("ingrese cuantos grados celsius quiere convertir a fahrrenheit "))
    grados_f = convertir_a_fahrrenheit(centigrados)
    print(f"{centigrados} grados centigrados son equivalentes a {grados_f} grados fahrenheit")
    fahrenheit = float(input("ingrese cuantos grados fahrenheit quiere convertir a celsius "))
    grados_c = convertir_a_centigrados(fahrenheit)
    print(f"{fahrenheit} grados fahrenheit son equivalentes a {grados_c} grados celcius")
    

if __name__ == "__main__":
      prueba()
