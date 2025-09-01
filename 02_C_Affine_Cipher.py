from math import gcd
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def affine_encrypt(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            p = ord(char) - ord('A')
            c = (a * p + b) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += char
    return ciphertext
def affine_decrypt(ciphertext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    inv_a = mod_inverse(a, 26)
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            p = (inv_a * (c - b)) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    a, b = 5, 8   
    text = "HELLO WORLD"
    
    encrypted = affine_encrypt(text, a, b)
    decrypted = affine_decrypt(encrypted, a, b)
    
    print("Plaintext :", text)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
