'''
Kessler DuPont

This program is a python implementation of Euclids greatest common factor algorithm.
It also explores prime factorization and gcf calculations for a list of numbers.

'''

#import python libraries
import doctest
import sys
import math


def kGCF(m, n):
    '''
    kGCF: a recursive implementation of Euclids algorithm that returns the GCF of m and n

    >>> kGCF(8, 12)
    4

    >>> kGCF(136, 55)
    1

    >>> kGCF(5928, 294386)
    38
    '''
    #r is the remainder
    r = m % n
    assert 0 <= r < n
    if (r == 0):
        return n
    return kGCF(n, r)


def kGCF2(numbers):
    '''
    kGCF2:

    >>> kGCF(8, 12)
    4

    >>> kGCF(136, 55)
    1

    >>> kGCF(5928, 294386)
    38
    '''
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    factors = dict()
    dList = list()
    numSet = set()
    for n in numbers:
        pf = primeFactors(n)
        tmp = dict()
        for m in pf:
            if m in tmp.keys():
                tmp[m] += 1
            else:
                tmp[m] = pf[m]
            numSet.add(m)
        dList.append(tmp)
    for n in numSet:
        factors[n] = list()
    for d in dList:
        for k, v in d.items():
            factors[k].append(v)
    for k, v in factors.items():
        for d in dList:
            if k not in d.keys():
                factors[k] = [0]
        l = len(factors[k])
        factors[k] = min(factors[k])
    product = 1
    for k, v in factors.items():
        if v > 0:
            product *= k ** v
    return product


def primeFactors(n):

    f = dict()

    f[2] = 0

    # Print the number of two's that divide n
    while n % 2 == 0:
        n //= 2
        f[2] += 1

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(n**.5) + 1, 2):
        f[i] = 0
        # while i divides n , print i and divide n
        while n % i== 0:
            n //= i
            f[i] += 1

    # Condition if n is a prime
    # number greater than 2
    if n not in f.keys():
        f[n] = 0
    if n > 2:
        f[n] += 1

    return f


def kFactors(n):
    '''
    kFactors: a function that returns an ordered list of prime numbers that have a product equal to n

    >>> kFactors(12)
    [2, 2, 3]

    >>> kFactors(24)
    [2, 2, 2, 3]

    >>> kFactors(100)
    [2, 2, 5, 5]
    '''
    n = int(n)
    f = dict()

    f[2] = 0
    n2 = n
    while (n2 % 2 == 0 and n2 > 3):
        n2 //= 2
        f[2] += 1

    for i in range(3, int(math.sqrt(n) + 1), 2):
        f[i] = 0
        n3 = n
        if not sum(kFactors(i).values()) < 2:
            continue
        while (n3 % i == 0): # and sum(kFactors(i).values()) < 2:
            f[i] += 1
            n3 //= i


    print(f'f = {f}')
    if len(f) < 1:
        f[n] = 1
    return f


if __name__ == '__main__':
    '''
    The main function: opens interface for finding the GCF, or, if in debug mode, runs doctests
    '''

    #n = 3*11*7*2*2*2*5*5*5*5*5
    #print(f'factors of {n} = {primeFactors(n)}')
    numbers = input('Enter a list of numbers, separated by a comma and space, to find their GCF => ').split(', ')
    #numbers = [3*11*7*2*2*2*5*5*5*5*5, 3*11*7*2*2*2*5*5*5*5*5*4, 3*11*7*2*2*2*5*5*5*5*5*15, 3*11*7*2*2*2*5*5*5*5*5, 3*11*7*2*2*2*5*5*5*5*5, 3*11*7*2*2*2*5*5*5*5*5, 3*11*7*2*2*2*5*5*5*5*5, 3*11*7*2*2*2*5*5*5*5*5*9, 3*11*7*2*2*2*5*5*5*5*5*99]
    print(f'The GCF of {numbers} is {kGCF2(numbers)}')
    exit()

    numbers = input('Enter two numbers, separated by a comma and space, to find their GCF => ').split(', ')
    m = int(numbers[0])
    n = int(numbers[1])
    #list = list(map(lambda v: int(v), numbers))
    print(f'The GCF of {numbers} is {kGCF(*numbers)}')

    exit()
    if len(sys.argv) < 2:
        print('Invalid arguments...\nUse -help for directions on how to use the program.')
        exit()

    mode = sys.argv[1]

    if mode == '-help':
        print('use the condition -factors to find factors of a list of numbers (separated by a space)')
        print('use the condition -gcf to find the gcf of a list of numbers (separated by a space)')
        exit()

    commandIndexStart = next(i for i in xrange(len(sys.argv)) if '-i' == sys.argv[i])
    commandIndexStop = next(i for i in xrange(commandIndexStart, len(sys.argv)) if '-' in sys.argv[i])

    numbers = sys.argv[:]
    for arg in sys.argv[1:]:
        print(arg)



    print(f'mode is {mode}')
    print(f'number list:\n{numbers}')
    #numbers = input('Enter two numbers, separated by a comma and space, to find their GCF => ').split(', ')
    #list = list(map(lambda v: int(v), numbers))
    #print(f'The GCF of {list} is {kGCF(*list)}')
