def poly_mul(a, b):
    res = 0
    while b:
        if b & 1: 
            res ^= a
        a <<= 1
        b >>= 1
    return res

def poly_mod(a, m):
    deg_m = m.bit_length() - 1
    while a.bit_length() - 1 >= deg_m:
        shift = a.bit_length() - m.bit_length()
        a ^= m << shift
    return a

p1 = 0b1011   
p2 = 0b1101   
m  = 0b10011  
product = poly_mul(p1, p2)
print("Product:", bin(product))
print("Modulo result:", bin(poly_mod(product, m)))