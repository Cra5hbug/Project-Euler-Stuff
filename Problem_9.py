def Pythagorean_triplets(limit):
    num1 = 1
    num2 = 1
    num3 = 1
    triplets = []
    for n in range(1, limit + 1):
        num1 = n
        for n in range(1, limit + 1):
            num2 = n
            for n in range(1, limit + 1):
                if num1 ** 2 + num2 ** 2 == num3 ** 2 and num1 + num2 + num3 == 1000:
                    triplets.append((num1, num2, num3))
                num3 = n
    return triplets
                    
def Pythagorean_triplets_modified(limit):
    num1 = 300
    num2 = 300
    num3 = 300
    for n in range(1, limit + 1):
        num1 = n
        for n in range(1, limit + 1):
            num2 = n
            for n in range(1, limit + 1):
                if num1 ** 2 + num2 ** 2 == num3 ** 2 and (num1 + num2 + num3 == 1000):
                    return num1 * num2 * num3
                num3 = n

    
    
foo = Pythagorean_triplets_modified(500)
print foo


