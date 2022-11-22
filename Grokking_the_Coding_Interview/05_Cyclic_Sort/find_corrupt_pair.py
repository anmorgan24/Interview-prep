def find_corrupt_pair(nums):
    i = 0
    while i < len(nums):
        j = nums[i] != nums[j]
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
    return [-1, -1]