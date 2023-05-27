import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    if gcd(a, m) != 1:
        raise ValueError("The numbers are not coprime.")
    r, prev_r = m, a
    x, prev_x = 0, 1

    while r != 0:
        quotient = prev_r // r
        prev_r, r = r, prev_r - quotient * r
        prev_x, x = x, prev_x - quotient * x

    return prev_x % m


def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        while d != n - 1:
            x = pow(x, 2, n)
            d *= 2

            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True


def generate_key_pair(key_size=1024):
    p = generate_large_prime(key_size // 2)
    q = generate_large_prime(key_size // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # A commonly used value for the public exponent

    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def generate_large_prime(key_size):
    while True:
        prime_candidate = random.randint(2 ** (key_size - 1), 2**key_size)
        if is_prime(prime_candidate):
            return prime_candidate


def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


if __name__ == "__main__":
    # usage example
    public_key, private_key = generate_key_pair()

    message = 1234321
    ciphertext = encrypt(message, public_key)
    decrypted_message = decrypt(ciphertext, private_key)

    print(f"Original Message: {message}")
    print(f"Encrypted Message: {ciphertext}")
    print(f"Decrypted Message: {decrypted_message}")
