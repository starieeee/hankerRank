def minimumSwipe(arr):
    swipeCount = 0
    sortedArr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != sortedArr[i]:
            correctIndex = sortedArr[i]
            j = arr.index(correctIndex)
            arr[i], arr[j] = arr[j], arr[i]
            swipeCount += 1
    return swipeCount