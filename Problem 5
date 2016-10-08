#Not my solution, just someone else's that I thought was really smart

from common import primeSieve
from math import sqrt, log

def PE(N):
    primes=primeSieve(N+1) #returns list of all primes <=N
    sqrtN=sqrt(N)
    ans=1
    for p in primes:
        if p <= sqrtN:
            ans*=p**(int(log(N)/log(p)))
        else:
            ans*=p
    return ans

print(PE(20))
