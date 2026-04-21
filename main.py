def binary_search(arr, n):
    start = 0
    end = len(arr) - 1
    while (start <= end):
        mid = (start + end) // 2
        if (n == arr[mid]):
            print(f"{n} is Found at index: {mid}")
            return
        if (n > arr[mid]):
            start = mid + 1
        if (n < arr[mid]):
            end = mid - 1
    print(f"{n} is Not Found")


arr = [50, 100, 231, 400]
binary_search(arr, 400)
