def largest_prime_factor(n):
    assert n >= 2
    
    def list_of_primes():
        yield 2
        yield 3
        
        factor = 5
        increment = 2
        while factor ** 2 <= n:
            yield factor
            factor += increment
        
    ans = None
    for factor in list_of_primes():
        while n % factor == 0:
            ans = factor
            n /= factor
            
    if n > 1:
        return int(n)
    else:
        return ans
        
print(largest_prime_factor(600851475143))
