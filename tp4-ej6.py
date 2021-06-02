################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def minimo(lista):
    
    lst = []
    
    contador = 9999999999999
    
    for i in range(lista):
        
        valor = int(input("Ingrese valor: "))
        
        lst.append(valor)
        
        
        if contador > valor:
            
            menor = valor
            contador = menor
    
    
    print(f"El menor es {menor}")
    
    return menor


def maximo(lista):
    
    lst = []
    
    contador = -999999999999
    
    for i in range(lista):
        
        valor = int(input("Ingrese valor: "))
        
        lst.append(valor)
        
        
        if contador < valor:
            
            maximo = valor
            contador = maximo
    
    
    print(f"El maximo es {maximo}")
    
    return maximo



def prueba():
    
    minimo(3)
    maximo(3)
    pass


if __name__ == "__main__":
    prueba()

