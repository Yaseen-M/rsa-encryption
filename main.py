def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_comprime(a, b):
    return hcf(a, b) == 1


def main():
    p = 8288669
    q = 2047933
    n = p * q

    totient = (p - 1) * (q - 1)
    print(is_comprime(totient, 5))


main()
