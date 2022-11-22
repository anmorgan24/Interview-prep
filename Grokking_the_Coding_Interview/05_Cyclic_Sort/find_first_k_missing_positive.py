def find_first_k_missing_positive(nums, k):
    n = len(n)
    i = 0
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
        
    missingNumbers = []
    extraNumbers = set()
    for i in range(n):
        if len(missingNumbers)< k:
            if nums[i] != i + 1:
                missingNumbers.append(i+1)
                extraNumbers.add(nums[i])

    #add the remining missing numbers
    i = 1
    while len(missingNumbers) < k:
        candidateNumber = i + n
        #ignore if the array contains the candidate number
        if candidateNumber not in extraNumbers:
            missingNumbers.append(candidateNumber)
        i += 1

    return missingNumbers