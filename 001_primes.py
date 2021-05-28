import math

'''
example input:
2
1 10
9900000 10000000
first number - number of tests
next lines - min and max number between whom shall I output any prime numbers
'''
t = int(input())

for test in range(t):
    input_list = list(map(lambda x: int(x), input().split()))
    if len(input_list) < 2:
        j = input_list[0]
        k = int(input())
    else:
        j, k = input_list

    m = 1
    n = math.ceil(math.sqrt(k))
    if n >= j:
        m = j
        n = k
    sieve = list(range(2, n+1))
    L = sieve[0]
    primes = []
    while L * L <= n:
        L = sieve[0]
        if L >= m:
            primes.append(L)
        sieve = list(filter(lambda x: x % L != 0, sieve))
    primes = primes + list(filter(lambda x: x >= m, sieve))

    if n >= j:
        for prime in primes:
            print(prime)
        if test < t - 1:
            print()
    else:
        input_range = range(j, k+1)
        for prime in primes:
            input_range = list(filter(lambda x: x % prime != 0, input_range))
        for prime in input_range:
            print(prime)
        if test < t - 1:
            print()
