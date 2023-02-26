"""
Question:
Maximum and minimum of an array using minimum number of comparisons

Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

Examples:

    Input: arr[] = {3, 5, 4, 1, 9}
    Output: Minimum element is: 1
                  Maximum element is: 9

    Input: arr[] = {22, 14, 8, 17, 35, 3}
    Output:  Minimum element is: 3
                  Maximum element is: 35

First of all, how do we return multiple values from a function? We can do it either using structures or pointers. 
We have created a structure named pair (which contains min and max) to return multiple values.
"""
# Note:
#     Python sort function use Timsort is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data.
# So it's node an optimal solution to find min and max with min comparison

def findMinMax(arr: list, low: int, high: int) -> (int, int):
    if low == high:
        return (arr[low], arr[high])

    if (high == low + 1):
        if arr[low] > arr[high]:
            return (arr[high], arr[low])
        else:
            return (arr[low], arr[high])

    mid = (high+low) // 2

    leftMinMax = findMinMax(arr, low, mid)
    rightMinMax = findMinMax(arr, mid, high)

    overallMin = min(leftMinMax[0], rightMinMax[0])
    overallMax = max(leftMinMax[1], rightMinMax[1])

    return (overallMin, overallMax)

"""
If n is odd:    3*(n-1)/2
If n is even:   1 Initial comparison for initializing min and max, and 3(n-2)/2 comparisons for rest of the elements
                      =  1 + 3*(n-2)/2 = 3n/2 -2
"""

arr = [3, 5, 4, 1, 9]
print("Minimum element is:", findMinMax(arr, 0, len(arr) - 1)[0])
print("Maximum element is:", findMinMax(arr, 0, len(arr) - 1)[1])
