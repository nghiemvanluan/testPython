def bubble_sort(arr):
    def swap(a, b):
        arr[a], arr[b] = arr[b], arr[a]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[a - 1] > arr[a]:
                swap(a - 1, a)
                swapped = True
                    
    return arr