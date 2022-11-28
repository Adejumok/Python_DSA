def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    sortedArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sortedArr.append(arr.pop(smallest))
    return sortedArr


ak = [4, 2, 3, 1]
print(f'The smallest number is at index {findSmallest(ak)}')
print(f'Sorted in ascending order: {selectionSort(ak)}')
