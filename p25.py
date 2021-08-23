
#Enunciado: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

f = [1,1] 
n = 1
while f[n] < 10**999: 
    f.append(f[n-1] + f[n])
    n += 1

print(len(f))