import random


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


def generate_p_q(length):
    p = generate_prime(pow(10, 6), pow(10, 7))
    while True:
        q = generate_prime(pow(10, 6), pow(10, 7))
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


def letter_to_num(letter):
    return ord(letter)


def message_to_num(message):
    return list(map(letter_to_num, message))


def get_message():
    message = input('Message to encrypt: ').upper()
    num_list = message_to_num(message)
    return int(''.join(str(x) for x in num_list))


def encrypt(m, e, n):
    return (pow(m, e, n))


def num_to_message(num):
    num = str(num)
    message = ''.join([chr(int(num[i:i+2])) for i in range(0, len(num), 2)])
    return message


def decrypt(c, d, n):
    num = (pow(c, d, n))
    return num_to_message(num)


def main():
    try:
        m = get_message()
        p, q = generate_p_q(len(str(m)))
        # n is the modulus for the pub and priv keys
        n = p * q
        totient = (p - 1) * (q - 1)

        e = generate_e(totient)
        d = generate_d(totient, e)
        c = encrypt(m, e, n)
        print('Encrypted: {}'.format(c))
        print('Decrypted: {}'.format(decrypt(c, d, n)))

    except:
        print('Uh oh! Something went wrong...')


main()
