# Given a sorted array of positive integers.
# Your task is to rearrange the array elements alternatively
# i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.
# Note: Modify the original array itself. Do it without using any extra space. You do not have to return anything.

# Example 1:

# Input:
# n = 6
# arr[] = {1,2,3,4,5,6}
# Output: 6 1 5 2 4 3
# Explanation: Max element = 6, min = 1,
# second max = 5, second min = 2, and
# so on... Modified array is : 6 1 5 2 4 3.

# Your Task:
# The task is to complete the function rearrange() which rearranges elements as explained above.
# Printing of the modified array will be handled by driver code.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).


class Solution:
    def rearrange(self, arr, n):
        pass


A = Solution()
print(A.rearrange([1, 2, 3, 4, 5, 6], 6))  # [6, 1, 5, 2, 4, 3]
