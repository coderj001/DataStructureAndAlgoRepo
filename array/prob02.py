"""
Question:
Write a program to reverse an array or string

Given an array (or string), the task is to reverse the array/string.
Examples :

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

"""


# def reverseArray(arr: list) -> list:
#     return arr[::-1]

def reverseArray(arr: list) -> list:
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# test the function

arr = [1, 2, 3, 4, 5]
print(reverseArray(arr))

