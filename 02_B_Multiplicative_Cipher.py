from math import gcd
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def encrypt(plaintext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26 for decryption to work.")
    
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            p = ord(char) - ord('A')
            c = (p * key) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += char
    return ciphertext
def decrypt(ciphertext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26 for decryption to work.")
    
    inv_key = mod_inverse(key, 26)
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            p = (c * inv_key) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    key = 5  
    text = "HELLO WORLD"
    
    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)
    
    print("Plaintext :", text)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
