def f_ele_occur(arr, k):
    freq = {}  # dictionary for frequency count
    # Count frequencies
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    # Traverse array again to keep order
    for num in arr:
        if freq[num] == k:
            return num
    return -1  # if no element found
arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
print(f_ele_occur(arr, k))  