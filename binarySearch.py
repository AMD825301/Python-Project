def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1

    while low <= high:

        mid = (low + high) // 2

        if lst[mid] == key:
            return mid

        elif lst[mid] > key:
            high = mid - 1

        else:
            low = mid + 1

    return -1


x = [10, 20, 30, 40, 50]

element = int(input("Enter the element you want to search: "))

result = binarySearch(x, element)

if result == -1:
    print("Element is not present.")

else:
    print("Element is present at index ", result)
