# BRUTE FORCE
# Time complexity: O(N*K)

def brute_force_max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr)- k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(sum, window_sum)
    
    return max_sum




# SLIDING WINDOWS


# Time complexity: O(N)
# Space complexity: O(1)

def max_sub_array_of_size_k(k, arr):

    max_sum, window_sum, window_start = 0, 0, 0

    for window_end in range(len(arr)):

        window_sum += arr[window_end] # add the next element
        # slide the window, we don't need to slide if we haven't hit the required window size of 'k'
        if window_end >= (k-1):
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] # subtract the element going out
            window_start += 1 # slide the window ahead

    return max_sum



# Time complexity: O(N + N) = O(N) asymptotically 
# Space complexity: O(1) (constant)

import math

def smallest_subarray_sum(s, arr):

    min_length = math.inf
    window_sum = 0
    window_start = 0
    for window_end in range(0, len(arr)):
        window_sum += arr[window_end] # add the next element
        # shrink the window as small as possible until the 'window_sum' is smaller than 's'
        while window_sum >= s:
            min_length = min(min_length, window_end = window_start +1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length

