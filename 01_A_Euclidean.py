def gcd_iterative(a, b):
 
  while b:
    a, b = b, a % b
  return a

num1 = 48
num2 = 18

greatest_common_divisor = gcd_iterative(num1, num2)
print(f"The GCD of {num1} and {num2} is: {greatest_common_divisor}")
