def insertionSort(lst):
    for i in range(1, len(lst)):

        currentValue = lst[i]

        j = i - 1

        while j >= 0 and currentValue < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            lst[j + 1] = currentValue

    return lst


x = [33, 22, 11, 66, 55]
print(insertionSort(x))
