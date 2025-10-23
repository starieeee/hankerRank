def mergeList(lists):
    merge = []
    for lst in lists:
        merge.extend(lst)
    return sorted(merge)
print(mergeList([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))