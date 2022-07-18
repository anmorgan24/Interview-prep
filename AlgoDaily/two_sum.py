def two_sum(arr,target):
    pointer_one=0
    pointer_two=len(arr)-1

    while pointer_one<pointer_two:
        if sum == target:
            return True
        elif sum < target:
            pointer_one += 1
        else:
            pointer_two -= 1

