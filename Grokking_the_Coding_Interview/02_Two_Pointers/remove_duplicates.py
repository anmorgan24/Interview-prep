def remove_duplicates(arr):
    i = 0
    next_non_duplicate = 1

    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate # return length


'''
Time Complexity:
The time complexty will be O(N), where 'N' is the total number of elements
in the given array.

Space Complexity:
The algorithm runs in constant space O(1).
'''