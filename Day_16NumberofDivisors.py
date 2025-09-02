def count_divisors(N: int) -> int:
    count = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            if i == N // i:
                count += 1  # Perfect square (count only once)
            else:
                count += 2  # i and N//i are two divisors
        i += 1
    return count
N = 12
print(count_divisors(N)) 
