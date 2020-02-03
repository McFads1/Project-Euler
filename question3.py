import math


def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    print(n)
    print(int(math.sqrt(n)) + 1)
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n, print i and divide n
        while n % i == 0:
            print(i)
            n = n / i
            print(n)
            print("----")

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


if __name__ == "__main__":
    primeFactors(600851475143)
