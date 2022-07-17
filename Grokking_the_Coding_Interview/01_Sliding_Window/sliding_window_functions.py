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