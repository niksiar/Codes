"""
nice odd number

A nice odd number is an odd number whose number of its prime divisors itself is a prime divisor of that odd number.

Write a program that, by receiving n from the input, prints the sum of the nice odds in the interval [1, n] inversely.

If there were no nice odds in the desired range, the phrase NOT FOUND! Be displayed in the output.

"""

import math

def niceOdd(x, num):
    a = 0
    for n in range(2, num):
        if num % n == 0:
            is_prime = True
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                a = a + 1

    for n in range(2, num):
        if num % n == 0:
            is_prime = True
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
                if is_prime and a == n:
                    x = x + num

    return x


a = 0
x = 0
t = 0
number = int(input())
for num in range(1, number + 1, 2):
    niceOdd(x, num)
    t = t + niceOdd(x, num)
if t != 0:
    num = t
    reverse_number = 0
    while num > 0:
        reminder = num % 10
        reverse_number = (reverse_number * 10) + reminder
        num = num // 10
    print(reverse_number)
else:
    print("NOT FOUND!")
