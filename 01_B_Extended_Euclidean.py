def extended_gcd(a, b):
    
    if a == 0:
        return (b, 0, 1)
    
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    
    while r != 0:
        quotient = old_r // r
        
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
        
 
    return (old_r, old_s, old_t)

a = 48
b = 18

gcd, x, y = extended_gcd(a, b)

print(f"The GCD of {a} and {b} is: {gcd}")
print(f"The coefficients are x = {x}, y = {y}")
print(f"Verification: ({a} * {x}) + ({b} * {y}) = {a*x + b*y}")

