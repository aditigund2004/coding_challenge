import math
N = 4
M = 6
gcd_val = math.gcd(N, M)   # Greatest Common Divisor
lcm_val = (N * M) // gcd_val   # Least Common Multiple
print("GCD:", gcd_val)   
print("LCM:", lcm_val)   
