def gf_mul(a, b, m):
    res = 0
    while b:
        if b & 1:
            res ^= a
        b >>= 1
        a <<= 1
        if a.bit_length() >= m.bit_length():
            a ^= m
    return res

p1 = 0b1011   
p2 = 0b1101   
m  = 0b10011  
print("Efficient GF multiply:", bin(gf_mul(p1, p2, m)))