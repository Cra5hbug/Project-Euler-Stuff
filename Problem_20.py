count = 0
import math
num = math.factorial(100)
for digit in str(num):
    count += int(digit)
print(count)
