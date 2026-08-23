# Binary Search
def binarysearch(array, search, lowindex, highindex):
    while lowindex <= highindex:
        avg = lowindex + (highindex - lowindex) // 2

        if array[avg] == search:
            return avg
        elif array[avg] < search:
            return avg + 1
        else:
            return avg - 1
    return -1
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
search = 20

result = binarysearch(numbers, search, 0, len(numbers) - 1)

if result == -1:
    print("Not found")
else:
    print("Found")