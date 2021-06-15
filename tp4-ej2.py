################
# Ramrio Salcedo - @RamiroSalcedo
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    
    
    num1 = numero 
    num2 = otro_numero 
    
    if numero >= otro_numero:
        
        contador = otro_numero
        
        for i in range(num1):
             
            print(f"{contador} + 1 ")
            
            contador = contador + 1
            
            
    elif numero <= otro_numero:
        
        contador = numero
        
        for i in range(num2):
                  
            print(f"{contador} + 1 ")
            contador = contador + 1
                
            
            
    return contador 
           
    
    
    
    
def prueba():
    print("ingrese dos numeros que quiera sumar")
    numero = int(input("primer numero: "))
    otro_numero = int(input("segundo numero: "))
    resultado = suma_lenta(numero, otro_numero)  
    print(resultado)

if __name__ == "__main__":
    prueba()