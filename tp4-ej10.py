def factores_primos(numero):
    
    primos = []
    
    for i in range(2, numero + 1):
        
        while numero % i == 0:
            
            primos.append(i)
            
            numero = numero / i
            
            
    return primos



def prueba():
    numero = int(input("ingrese un numero: "))
    tupla = factores_primos(numero)
    print(tupla)
            
 
if __name__ == "__main__":
    prueba()