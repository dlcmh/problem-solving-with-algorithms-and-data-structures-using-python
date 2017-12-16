# [1] Assumes search is done in an ordered list
# [2] If middle item is the one being searched, we are done
# [3] If searched item is smaller than the middle item, we can eliminate the
#     middle item as well as the entire upper half of the list since the item,
#     if it is in the list, must be in the lower half.
# [4] If searched item is larger than the middle item, we can eliminate the
#     middle item as well as the entire lower half of the list since the item,
#     if it is in the list, must be in the upper half.

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item: # [2]
            found = True
        else:
            if item < alist[midpoint]: # [3]
                last = midpoint - 1
            else:
                first = midpoint + 1 # [4]

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42] # [1]
print(binarySearch(testlist, 3)) # => False
print(binarySearch(testlist, 13)) # => True
