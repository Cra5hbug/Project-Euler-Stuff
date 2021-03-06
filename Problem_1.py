sum = 0
for i in range(1000):
  if i%3 == 0 or i%5 == 0:
    sum += i
print sum


More elegant method:
def multiples_of_3_or_5():
  for x in range(1000):
    if x%3 == 0 or x%5 == 0:
      yield x
print sum(multiples_of_3_or_5())

More mathy(kinda ugly):
ans = 0
for num in range(0, 334):
    ans += 3 * num
for num in range(0, 200):
    ans += 5 * num
for num in range(1, 67):
    ans -= 15 * num
print ans 
