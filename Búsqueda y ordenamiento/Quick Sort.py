import random

def quick_sort(arr):
    if len(arr) <= 1: 
        return arr

    pivot = random.choice(arr) #                                    7                   6

    smaller = [x for x in arr if x < pivot] #                       [6, 4]              [4]
    equal = [x for x in arr if x == pivot] #                        [7]                 [6]
    greater = [x for x in arr if x > pivot] #                       []                  []

    return quick_sort(smaller) + equal + quick_sort(greater) #      [6,4] + [7] []      [4] + [6] 

# [4,6,7]

# O(n log n) better case 
# O(nˆ2).    worse


print(quick_sort([6, 4, 7,1,2,10,5,2 , 2]))