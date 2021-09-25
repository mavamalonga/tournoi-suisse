def factorial_recursive(n):
	if n == 1:
		return 1
	else:
		return n * factorial_recursive(n-1)


r = factorial_recursive(5)
print(r)