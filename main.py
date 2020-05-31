import random
import math


def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_comprime(a, b):
    return hcf(a, b) == 1


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def generate_prime(lower, upper):
    while True:
        n = random.randint(lower, upper)
        if is_prime(n):
            return n


def generate_p_q():
    p = generate_prime(100, 10000)
    while True:
        q = generate_prime(100, 10000)
        if p != q:
            break
    return p, q


def main():
    p, q = generate_p_q()

    # n is the modulus for the pub and priv keys
    n = p * q

    totient = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, totient - 1)
        if is_comprime(e, totient):
            break

    d = (1 % totient) / e
