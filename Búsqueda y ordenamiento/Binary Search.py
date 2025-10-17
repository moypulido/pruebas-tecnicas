def binary_search(array, target):
    start = 0
    end = len(array)- 1

    while start <= end:
        mid = (start + end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    
    return False


print(binary_search([1,2,3,4,5,6,7,8,9], 5))  # Output: 4