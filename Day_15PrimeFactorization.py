def prime_factorization(N: int):
    factors = []
    # Divide by 2 until N is odd
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    # Check odd numbers from 3 to sqrt(N)
    i = 3
    while i * i <= N:
        while N % i == 0:
            factors.append(i)
            N //= i
        i += 2
    # If N is still greater than 2, it's prime
    if N > 2:
        factors.append(N)
    return factors
N = 12
print(prime_factorization(N))
