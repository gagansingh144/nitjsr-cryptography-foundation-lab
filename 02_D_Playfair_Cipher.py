def generate_key_matrix(key):
    key = key.upper().replace("J", "I")  
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  
        if char not in used:
            matrix.append(char)
            used.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(text):
        if text[i].isalpha():
            prepared += text[i]
            if i+1 < len(text) and text[i] == text[i+1]:
                prepared += "X"
            i += 1
        else:
            i += 1
    if len(prepared) % 2 != 0:
        prepared += "X"
    return prepared

def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    text = prepare_text(plaintext)
    ciphertext = ""

    i = 0
    while i < len(text):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  
            ciphertext += matrix[r1][(c1+1)%5]
            ciphertext += matrix[r2][(c2+1)%5]
        elif c1 == c2:  
            ciphertext += matrix[(r1+1)%5][c1]
            ciphertext += matrix[(r2+1)%5][c2]
        else:  
            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]
        i += 2

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    plaintext = ""

    i = 0
    while i < len(ciphertext):
        a, b = ciphertext[i], ciphertext[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  
            plaintext += matrix[r1][(c1-1)%5]
            plaintext += matrix[r2][(c2-1)%5]
        elif c1 == c2:  
            plaintext += matrix[(r1-1)%5][c1]
            plaintext += matrix[(r2-1)%5][c2]
        else:  
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]
        i += 2

    return plaintext
if __name__ == "__main__":
    key = "MONARCHY"
    text = "HELLO WORLD"

    encrypted = playfair_encrypt(text, key)
    decrypted = playfair_decrypt(encrypted, key)

    print("Key Matrix:")
    for row in generate_key_matrix(key):
        print(row)

    print("\nPlaintext :", text)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
