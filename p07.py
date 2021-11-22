#Enunciado: What is the 10 001st prime number?


import math
def prime(n):
    '''Test de primalidad de un número'''
    for j in range(2,round(math.sqrt(n)) + 1): 
        if n % j == 0:
            return False 
    return True 
    # me dice si un numero es primo o no

def position_prime(n): 
    cont = 0
    number = 2
    while (cont < n):
        if prime(number):
            cont += 1
        number += 1

    final_prime = number - 1

    return final_prime
    # me dice el numero primo en la posicion num de una lista de num primos 

print(position_prime(10001))
