# __author__ = Vishu Kamble
"""
A python program to mergeSort
"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)/2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    print "Merging: ", arr

arr = [54, 23,45,12,59, 29, 10, 4, 2,1,43]
mergeSort(arr)
print arr