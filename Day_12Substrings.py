def substrings_with_k_distinct(s: str, k: int) -> int:
    n = len(s)
    count = 0
    
    # Generate all substrings
    for i in range(n):
        distinct = set()
        for j in range(i, n):
            distinct.add(s[j])  # add character
            if len(distinct) == k:
                count += 1
            elif len(distinct) > k:
                break  # no need to check further
    
    return count
s = "pqpqs"
k = 2
print(substrings_with_k_distinct(s, k))  
