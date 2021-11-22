#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


import math

def terna_pitagorica(m, n): 
	'''Genera una terna pitagórica '''
	a = m ** 2 - n ** 2
	b = 2 * m * n
	c = m ** 2 + n ** 2
	return a, b, c

if __name__ == "__main__": 
	a, b, c = 0, 0, 0
	m = 1
	n = 0
	f = True 

	while f: 
		for i in range(m): 
			n = i
			a, b, c = terna_pitagorica(m, n)
			if (a + b + c) == 1000: 
				f = False   
				break
		n = 0
		m += 1

	print(a * b * c)



