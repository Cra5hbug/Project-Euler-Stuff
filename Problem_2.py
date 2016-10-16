Sexy generator:

def fibsum(n):
    a,b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
gen = fibsum(4000000)
answer = 0
for n in gen:
    if n%2 == 0:
        answer += n
print answer
