
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    curr = 0
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] <= arrB[0]:
            merged_arr[curr] = arrA.pop(0)
        else:
            merged_arr[curr] = arrB.pop(0)
        curr += 1
    while len(arrA) != 0:
        merged_arr[curr] = arrA.pop(0)
        curr += 1
    while len(arrB) != 0:
        merged_arr[curr] = arrB.pop(0)
        curr += 1
    return merged_arr



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)



def merge_in_place(arr, start, mid, end):
    left = start
    right = mid+1
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            left += 1
        else:
            num = arr[right]
            index = right
            while index != left:
                arr[index] = arr[index-1]
                index -= 1
            arr[left] = num
            left += 1
            right += 1
            mid += 1


def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = l+(r-l)//2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid+1, r)
        merge_in_place(arr, l, mid, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
