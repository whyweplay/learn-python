def odd_iter():
	n=1
	while True:
		n=n+2
		yield n
def not_div(n):
	return lambda x:x%n>0
def primes():
	yield 2
	it=odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(not_div(n),it)
for n in primes():
	if n<1000:
		print(n)
	else:
		break