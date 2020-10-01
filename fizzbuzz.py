def fizzbuzz(n):
	return [str(n), "fizz", "buzz", "fizzbuzz"][(n%3 == 0) + (n%5 ==0)*2]
