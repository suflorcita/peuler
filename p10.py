import math
def prime(n):
    '''Test de primalidad de un número'''
    if (n < 2): return False
    for i in range(2, round(math.sqrt(n)) + 1): 
        if (n % i == 0): return False
    return True 


def sum_prime(n): 
    number = 1
    sum = 0
    while (number < n):
        if prime(number):
            sum += number
        number += 1
    return sum

# retorna la suma hasta cierto n
print(sum_prime(2*10**6))


# tarda, es ineficiente, habría que optimizarlo 