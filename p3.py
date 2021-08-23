#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
import math
def largest_prime(n): 
    '''Retorna el primo más grande que es factor de un numero n'''
    while n >= 2:
        if n % 2 == 0: 
            max = 2
            n = n / 2
        else:
            for i in range(3,round(math.sqrt(n)) + 1, 2): 
                #se usa la misma idea que la criba de eratostenes
                if n % i == 0: 
                    max = i
                    n = n / i
    return max

print(largest_prime(600851475143))