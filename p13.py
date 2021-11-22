# Enunciado : Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# Escribo los números que dice el enunciado a un archivo txt

txt = open('peuler/num.txt','r')

num = 0
sum = 0 
remainder = 0 

for line in txt: 
    num = int(line)
    sum += num 
    
print(str(sum)[:10])

txt.close()

