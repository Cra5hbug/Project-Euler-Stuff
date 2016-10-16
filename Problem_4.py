def is_palindrome(string):
    return string == string[::-1]

def largest_palindrome_n_digits(n):
    foo = []
    for number in range(9 * 10 ** (n-1), 10 * 10 ** (n-1)):
        num1 = number
        for number in range(9 * 10 ** (n-1), 10 * 10 ** (n-1)):
            num2 = number
            result = str(num1 * num2)
            if is_palindrome(result) == True:
                    foo.append((result, num1, num2))
    sorted_by_first = sorted(foo, key=lambda tup: tup[0])
    return sorted_by_first

        
bar = largest_palindrome_n_digits(3)
print(bar)

#I should really learn how to use lambda expressions...

VERSION 2 (Way better lol)
def is_palindrome(string):
    return string == string[::-1]

def largest_palindrome_n_digits(n):
    products = []
    for a in range(9 * 10 ** (n-1), 10 * 10 ** (n-1)):
        for b in range(9 * 10 ** (n-1), 10 * 10 ** (n-1)):
            p = a * b
            if is_palindrome(str(p)):
                products.append(int(p))
    return max(products)
bar = largest_palindrome_n_digits(3)
print(bar)
