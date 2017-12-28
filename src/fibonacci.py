'''
Created on Jun 5, 2016

@author: vincent
'''

def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
		print()
		
gList = []
print(fib(20))
print(fib(30))				