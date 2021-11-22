#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
#What is the value of this product?


def product(number): 
	'''Calcula el producto de n numeros dado un string que represente un numero'''
	product = 1
	for digit in number: 
		product *= int(digit)


	return product


if __name__ == "__main__": 
	number = ""; 
	max_num = ""; 
	max_prod = 0; 

	with open('p8_number.txt', 'r') as f:
	    for line in f: 
	    	line = line.rstrip('\n')
	    	number += line


	for i in range(1000 - 12): 
		# voy interando en todas las cuatros pares de numeros posibles
		num = number[i: i+13]			
		
		
			
		if (product(num)> max_prod): 			
			max_prod = product(num)
			max_num = num 


	print(max_prod)
	print(max_num)
