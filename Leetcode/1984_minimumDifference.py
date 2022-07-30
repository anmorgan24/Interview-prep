def minDifference(nums, k):
    nums.sort()
    min_diff = float('inf') # or 100001
    for i in range(len(nums)-k+1):
        min_diff = min(min_diff, nums[i+k-1]-nums[i])
    return min_diff