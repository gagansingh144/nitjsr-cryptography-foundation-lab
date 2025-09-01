def modular_inverse(a, p):

    
    if a == 0:
        return None 
    
    old_r, r = p, a
    old_t, t = 0, 1
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_t, t = t, old_t - quotient * t
        
    if old_r > 1:
        return None
        
    if old_t < 0:
        old_t = old_t + p
        
    return old_t


a = 7
p = 19

inverse = modular_inverse(a, p)

if inverse is not None:
    print(f"The inverse of {a} in GF({p}) is: {inverse}")
    print(f"Verification: ({a} * {inverse}) mod {p} = {(a * inverse) % p}")
else:
    print(f"An inverse for {a} in GF({p}) does not exist.")

