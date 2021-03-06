#Enunciado: 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?'''

def sum_digits(num): 
    ''' Retorna la suma de los digitos de un número'''
    num = str(num)
    list_digits = [int(n) for n in num]

    return sum(list_digits)

if __name__ == "__main__": 
    print(sum_digits(2**1000))


