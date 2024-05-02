# User function template for Python

# Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

# Note: If at any instance, there are no more subarrays of size greater than or equal to K,
# then reverse the last subarray (irrespective of its size).
# You shouldn't return any array, modify the given array in-place.

# Input:
# N = 5, K = 3
# arr[] = {1,2,3,4,5}
# Output: 3 2 1 5 4
# Explanation: First group consists of elements
# 1, 2, 3. Second group consists of 4,5.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        for i in range(0, N, K):
            arr[i : i + K] = arr[i : i + K][::-1]
        return arr


A = Solution()
print(A.reverseInGroups([1, 2, 3, 4, 5], 5, 3))  # [3, 2, 1, 5, 4]
