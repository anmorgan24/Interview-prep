def containsNearbyDuplicate1(nums, k):
    if k==0:
        return True
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] == nums[j]):
                if abs(i-j)<=k:
                    return True
    else:
        return False