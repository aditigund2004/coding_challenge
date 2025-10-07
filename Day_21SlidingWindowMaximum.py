#maintain a deque (double-ended queue) that stores indices of potential maximum ele for the current window.
from collections import deque
def sliding_win_maxi(arr, k):
    n = len(arr)
    if n * k == 0:
        return []
    if k == 1:
        return arr

    dq = deque()  # stores indices of useful ele in window
    output = []

    for i in range(n):
        # Remove ele that are out of window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove all ele smaller than the current one
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Add current ele index
        dq.append(i)

        # The front of the deque is the max ele of the current window
        if i >= k - 1:
            output.append(arr[dq[0]])

    return output
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_win_maxi(arr, k))  
