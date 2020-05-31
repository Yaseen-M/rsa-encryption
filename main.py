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


def generate_e(totient):
    e = 2
    while True:
        if is_comprime(e, totient):
            return e
        e += 1


def generate_d(totient, e):
    k = 1
    while True:
        d = (1 + (k * totient)) / e
        if d.is_integer():
            return int(d)
        k += 1


def generate_c(m, e, n):
    return (pow(m, e, n))


def decrypt(c, d, n):
    return (pow(c, d, n))


def main():
    p, q = generate_p_q()

    # n is the modulus for the pub and priv keys
    n = p * q
    totient = (p - 1) * (q - 1)

    e = generate_e(totient)
    d = generate_d(totient, e)
    c = generate_c(1234, e, n)
    print('Decrypted: ', decrypt(c, d, n))


main()
