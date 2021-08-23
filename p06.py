# Enunciado: Find the difference between 
# the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Implementación usando fuerza bruta
def sum_squares(n):
    sum = 0 
    for i in range(1,n+1):
        sum += i**2
    return sum
    # suma de los n numeros al cuadrado

def square_sum(n): 
    sum = 0 
    for i in range(1,n+1): 
        sum += i 
    return sum ** 2
# suma de los n numeros, elevada al cuadrado
print(square_sum(100) - sum_squares(100))