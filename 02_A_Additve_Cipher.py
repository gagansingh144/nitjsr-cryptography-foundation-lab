def additive_cipher(text, shift, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    
    if mode == 'decrypt':
        shift = -shift
        
    for char in text.lower():
        if char in alphabet:
            
            original_index = alphabet.find(char)
            
            new_index = (original_index + shift) % 26
            
            result += alphabet[new_index]
        else:
            result += char
            
    return result

if __name__ == "__main__":
    message = "Hello, this is a secret message!"
    key = 5

    # Encryption
    encrypted_message = additive_cipher(message, key, 'encrypt')
    print(f"Original Message:  {message}")
    print(f"Encrypted Message: {encrypted_message}")

    # Decryption
    decrypted_message = additive_cipher(encrypted_message, key, 'decrypt')
    print(f"Decrypted Message: {decrypted_message}")