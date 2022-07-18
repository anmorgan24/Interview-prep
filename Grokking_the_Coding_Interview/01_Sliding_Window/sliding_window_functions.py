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




# SLIDING WINDOW
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