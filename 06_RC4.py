def rc4(key: bytes, data: bytes) -> bytes:
    # Key-Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    keylen = len(key)
    for i in range(256):
        j = (j + S[i] + key[i % keylen]) & 0xFF
        S[i], S[j] = S[j], S[i]
    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    out = bytearray()
    for byte in data:
        i = (i + 1) & 0xFF
        j = (j + S[i]) & 0xFF
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) & 0xFF]
        out.append(byte ^ K)
    return bytes(out)

# Helpers
def to_hex(b: bytes) -> str:
    return b.hex()

def from_hex(h: str) -> bytes:
    return bytes.fromhex(h)

# Example usage:
key = b"Key"
plaintext = b"Plaintext"
cipher = rc4(key, plaintext)
print("Cipher (hex):", to_hex(cipher))   # -> bbf316e8d940af0ad3
print("Decrypted:", rc4(key, cipher))    # -> b'Plaintext'
