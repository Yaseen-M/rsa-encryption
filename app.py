import random


def hcf(a, b):
    # Returns highest common factor
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
    # Returns two distinct primes
    p = generate_prime(pow(10, 2), pow(10, 4))
    while True:
        q = generate_prime(pow(10, 2), pow(10, 4))
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


def letter_to_ascii(letter):
    return ord(letter)


def message_to_num(message):
    # Converts a message to list of ascii numbers
    return list(map(letter_to_ascii, message))


def get_message():
    message = input('Message to encrypt: ').replace(' ', '').upper()
    ascii_list = message_to_num(message)
    return ascii_list


def encrypt(m, e, n):
    non_padded = pow(m, e, n)
    # Returns padded number
    return int(str(random.randint(10, 19)) + str(non_padded) + str(random.randint(10, 19)))


def num_to_message(num):
    num = str(num)
    # Converts string of ascii numbers to string of corresponding letters
    message = ''.join([chr(int(num[i:i+2])) for i in range(0, len(num), 2)])
    return message


def decrypt(c, d, n):
    unpadded = int(str(c)[2:-2])
    num = (pow(unpadded, d, n))
    return num_to_message(num)


def main():
    m = get_message()
    # Returns two distinct primes
    p, q = generate_p_q()
    # n is the modulus for the pub and priv keys
    n = p * q
    totient = (p - 1) * (q - 1)
    e = generate_e(totient)
    d = generate_d(totient, e)
    c = [encrypt(num, e, n) for num in m]
    print('Encrypted: {}'.format(c))
    decrypted = ''.join([decrypt(i, d, n) for i in c])
    print('Decrypted: {}'.format(decrypted))


if __name__ == "__main__":
    # Only runs if program is run directly
    main()
