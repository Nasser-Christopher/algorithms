# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

# Input:
# N = 5
# arr[]= {0 2 1 2 0}

# Output:
# 0 0 1 2 2

# Explanation:
# 0s 1s and 2s are segregated into ascending order.


# Constraints:
# 1 <= N <= 10^6
# 0 <= A[i] <= 2
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


# User function Template for python3
class Solution:

    # Function to sort the array of 0s, 1s and 2s
    # 1. "Dutch National Flag Algorithm" to solve this problem.
    # NOTE: A question of this caliber is highly specific to the Dutch National Flag Algorithm.
    # The Dutch National Flag Algorithm is a sorting algorithm that sorts an array of 0s, 1s, and 2s in a single traversal.
    # The algorithm traverses the array only once and does not use any extra space.
    # It has real world uses cases in sorting colors and solving problems related to arrays with three unique elements.

    def sort012(self, arr, n):
        low = 0
        high = n - 1
        mid = 0

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:  # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr
        # code here


A = Solution()
print(A.sort012([0, 2, 1, 2, 0], 5))  # [0, 0, 1, 2, 2]
