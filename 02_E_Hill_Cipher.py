import numpy as np

# Convert character to number (A=0,...,Z=25)
def char_to_num(c):
    return ord(c.upper()) - ord('A')

# Convert number to character
def num_to_char(n):
    return chr(n + ord('A'))

# Prepare text (remove spaces, pad with X)
def prepare_text(text, block_size):
    text = "".join([c.upper() for c in text if c.isalpha()])
    while len(text) % block_size != 0:
        text += "X"
    return text


def hill_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    text = prepare_text(plaintext, n)
    ciphertext = ""

    for i in range(0, len(text), n):
        block = [char_to_num(c) for c in text[i:i+n]]
        block_vec = np.array(block).reshape(n, 1)
        cipher_vec = np.dot(key_matrix, block_vec) % 26
        ciphertext += "".join(num_to_char(int(x)) for x in cipher_vec)
    return ciphertext
def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix))) 
    det_inv = None
    for i in range(26):
        if (det * i) % modulus == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError("Matrix determinant has no modular inverse. Invalid key.")
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    ) % modulus

    return matrix_mod_inv.astype(int)
def hill_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    key_inv = matrix_mod_inverse(key_matrix, 26)
    plaintext = ""

    for i in range(0, len(ciphertext), n):
        block = [char_to_num(c) for c in ciphertext[i:i+n]]
        block_vec = np.array(block).reshape(n, 1)
        plain_vec = np.dot(key_inv, block_vec) % 26
        plaintext += "".join(num_to_char(int(x)) for x in plain_vec)
    return plaintext
if __name__ == "__main__":
    key_matrix = np.array([[3, 3], [2, 5]])  
    text = "HELLO"

    encrypted = hill_encrypt(text, key_matrix)
    decrypted = hill_decrypt(encrypted, key_matrix)

    print("Key Matrix:\n", key_matrix)
    print("Plaintext :", text)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
