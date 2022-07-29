def containsNearbyDuplicate2(nums, k):
    seen = {}
        
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen[nums[i]] = i
        else:
            if abs(i-seen[nums[i]])<= k:
                return True
            seen[nums[i]] = i
    return False