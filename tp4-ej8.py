################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ordenar_mayor_a_menor(uno, dos, tres):
    
    if uno > dos:
        
        if uno > tres:
            
            if tres < dos:
                t = ( uno, dos, tres)
            else:
                t = ( uno, tres, dos)
                
    elif dos > uno:
        
        if dos > tres:
            
            if uno > tres:
                t = ( dos, uno, tres)
                
            else:
                t = ( dos, tres, uno)
                
    else:
        
        if tres > dos:
            
            if tres > uno:
                
                if dos > uno:
                    t = ( tres, dos, uno)
                    
                else:
                    t = ( tres, uno, dos)
                    
    print(t)
    

def ordenar_menor_a_mayor(uno, dos, tres):
    
    
    
    if uno < dos:
        
        if uno < tres:
            
            if dos < tres:
                t = (uno, dos, tres)
            else:
                t = (uno, tres, dos)
                
                
    elif dos < uno:
        
        if dos < tres:
            
            if uno < tres:
                t = (dos, uno ,tres)
            else:
                t = (dos, tres, uno)
                
    else:
        
        if tres < uno:
            
            if tres < dos:
                
                if uno < dos:
                    t = (tres, uno, dos)
                    
                else:
                    t = (tres, dos, uno)
                    
                        
    print(t)                     






def prueba():
    ordenar_menor_a_mayor(3444, 4, 65)
    ordenar_mayor_a_menor(2, 32, 1)
    pass

if __name__ == "__main__":
    prueba()
                    
