import math

def is_square(n):
    sqrt_n = int(math.sqrt(n))
    if sqrt_n*sqrt_n == n:
        return float(sqrt_n)
    else:
        return -1

while True:
    n = int(input("enter positive integer >> "))
    if n == 0:
        break
    answer = is_square(n)
    print("{0:d}의 제곱근은 {1}".format(n, answer))
