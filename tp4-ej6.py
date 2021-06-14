################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def lista(cantidad_numeros):
    
    lst = []
    

    for i in range(cantidad_numeros):
        
        valor = int(input("Ingrese valor: "))
        
        lst.append(valor)


    return lst
    

def minimo(argumentolista, cantidad_numeros):
    
    
    
    
    
    contador = 99999999999
    
    for i in range(cantidad_numeros):
              
        valor = argumentolista[i]   
        
        if valor < contador:
            
            
            vminimo = valor
            contador = valor
    
    
    
    
    return vminimo


def maximo(argumentolista, cantidad_numeros):
    
    
    
    
    contador = -999999999999
    
    for i in range(cantidad_numeros):
        
        valor = argumentolista[i] 
        
        if valor > contador:
            
            vmaximo = valor
            contador = valor
    
    
    
    
    return vmaximo



def prueba():
    
    cantidad_numeros = int(input("ingrese cuantos valores quiere cargar en la lista: "))
    listita = lista(cantidad_numeros)
    
    min_n = minimo(listita, cantidad_numeros)
    print(f"El minimo es {min_n}")
    max_n = maximo(listita, cantidad_numeros)
    print(f"El maximo es {max_n}")


if __name__ == "__main__":
    prueba()

