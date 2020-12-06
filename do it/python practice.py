import math

def isPrime(x):
    if all(x % i != 0 for i in range(2,math.ceil(math.sqrt(x)))):
        return True
    else:
        return False

def Primes(Y):
    ylist = list(range(2,Y))
    for k in range(2,math.ceil(math.sqrt(Y))):
        if isPrime(k):
            for m in range(2,Y):
                if k*m < Y:
                    if k*m in ylist:
                        ylist.remove(k*m)
                    else:
                        continue
                else:
                    continue
        else:
            continue
    return ylist

answer = 0
for t in Primes(100000):
    answer += t

print(answer)
