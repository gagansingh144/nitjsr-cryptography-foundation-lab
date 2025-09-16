# Python Program for implementation of RSA Algorithm

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo //= 2
    return res

# Function to find modular inverse of e modulo phi(n)
def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

# Function to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# RSA Key Generation
def generateKeys():
    p = 61   # small prime for example
    q = 53   # small prime for example
    
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e, where 1 < e < phi(n) and gcd(e, phi(n)) == 1
    e = 0
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break

    # Compute d such that e * d ≡ 1 (mod phi(n))
    d = modInverse(e, phi)

    return e, d, n

# Encrypt message using public key (e, n)
def encrypt(m, e, n):
    return power(m, e, n)

# Decrypt message using private key (d, n)
def decrypt(c, d, n):
    return power(c, d, n)

def convert_to_ascii(message):
    return [ord(char) for char in message]

def convert_to_string(ascii_values):
    return ''.join(chr(value) for value in ascii_values)

# Main execution
if __name__ == "__main__":
    # Generate RSA keys
    e, d, n = generateKeys()
  
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Message
    message = "hello"
    M = convert_to_ascii(message)
    print(f"Original Message: {message} -> {M}")

    # Encrypt the message
    encrypted_values = [encrypt(i, e, n) for i in M]
    print(f"Encrypted Message: {encrypted_values}")

    # Decrypt the message
    decrypted_values = [decrypt(c, d, n) for c in encrypted_values]
    decrypted_message = convert_to_string(decrypted_values)
    print(f"Decrypted Message: {decrypted_message}")
