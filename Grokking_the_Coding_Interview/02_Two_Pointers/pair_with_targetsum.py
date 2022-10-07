def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr)-1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1
        else: 
            right -= 1
    return [left, right]


'''
Time Complexity:
The time complexity will be O(N), where 'N" is the total number of elements 
in the given array.

Space Complexity
The algorithm runs in constant space O(1).
'''