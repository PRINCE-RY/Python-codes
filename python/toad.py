def is_prime(n):
   if n<=1:
      return False
   for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
	 							return False
   return True

prime={x for x in range(1,10)if is_prime(x)}
odd={x for x in range(1,10) if x%2!=0}
print(prime)
print(odd)
print(prime.union(odd))
print(prime.intersection(odd))
print(prime.difference(odd))
print(prime.symmetric_difference(odd))
