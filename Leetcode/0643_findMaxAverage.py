def findMaxAverage(nums, k):
    window_start = 0
    window_sum = sum(nums[window_start:window_start+k])
    max_average = window_sum/k
        
    while True:
        window_start +=1
        if (window_start> len(nums)-k):
            break
                
        window_sum = window_sum - nums[window_start-1] + nums[window_start+k-1]
            
        if window_sum / k > max_average:
            max_average = window_sum/k
    return max_average