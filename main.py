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
    p = generate_prime(2, 20)
    while True:
        q = generate_prime(2, 20)
        if p != q:
            break
    return p, q


def generate_e(totient):
    while True:
        e = random.randint(2, 10)
        if is_comprime(e, totient):
            return e


def generate_d(totient, e):
    i = 1
    while True:
        d = (1 + (i * totient)) / e
        if d.is_integer():
            return d
        i += 1


def generate_c(m, e, n):
    return (m ** e) % n


def decrypt(c, d, n):
    return (pow(c, d)) % n


def main():
    p, q = generate_p_q()

    # n is the modulus for the pub and priv keys
    n = p * q
    totient = (p - 1) * (q - 1)
    e = generate_e(totient)
    d = generate_d(totient, e)
    c = generate_c(4, e, n)

    print(c)
    print(decrypt(c, d, n))


main()
