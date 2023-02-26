"""
Chocolate Distribution Problem
Given an array of N integers where each value represents the number of
chocolates in a packet. Each packet can have a variable number of chocolates.
There are m students, the task is to distribute chocolate packets such that:

Each student gets one packet.
The difference between the number of chocolates in the packet with maximum
chocolates and the packet with minimum chocolates given to the students
is minimum.

Examples:
Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3
Output: Minimum Difference is 2
Explanation:
We have seven packets of chocolates and we need to pick three packets for 3 students 
If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.

Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
Output: Minimum Difference is 6

Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50} , m = 7 
Output: Minimum Difference is 10

Naive Approach for Chocolate Distribution Problem
The idea is to generate all subsets of size m of arr[0..n-1].
For every subset, find the difference between the maximum and minimum elements in it. Finally, return the minimum difference.

Efficient Approach for Chocolate Distribution Problem
The idea is based on the observation that to minimize the difference, we must choose consecutive elements from a sorted packet. We first sort the array arr[0..n-1], then find the subarray of size m with the minimum difference between the last and first elements.

Illustration:
Below is the illustration of example arr[] = [ 7,3,2,4,9,12,56 ] , m = 3

Chocolate Distribution Problem Solution

Follow the steps mentioned below to implement the approach:
Initially sort the given array. And declare a variable to store the minimum difference, and initialize it to INT_MAX. Let the variable be min_diff.
Find the subarray of size m such that the difference between the last (maximum in case of sorted) and first (minimum in case of sorted) elements of the subarray is minimum.
We will run a loop from 0 to (n-m), where n is the size of the given array and m is the size of the subarray.
We will calculate the maximum difference with the subarray and store it in diff = arr[highest index] – arr[lowest index]
Whenever we get a diff less than the min_diff, we will update the min_diff with diff.
"""


def findMinDiff(chocolates: list, n: int) -> int:
    """docstring for findMinDiffor"""
    chocolates.sort()

    min_diff = float('inf')  # is a way to represent infinity in Python
    for i in range(len(chocolates)-n+1):
        diff = chocolates[i+n-1] - chocolates[i]
        if diff < min_diff:
            min_diff = diff
    return int(min_diff)


# __import__('pprint').pprint(findMinDiff([7, 3, 2, 4, 9, 12, 56], 3))
