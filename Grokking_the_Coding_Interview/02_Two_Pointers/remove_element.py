def remove_element(arr, key):
    nextElement = 0
    for i in rnage(le(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1

    return nextElement