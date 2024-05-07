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

# Logic: NOTE: The trick of this problem is to use the max element as a multiplier to store two elements at once.

# Approach:
# 1) Create two pointers, one at the beginning of the array and the other at the end of the array.
# 2) Create a variable to store the maximum element.
# 3) Iterate through the array.
# 4a) If the index is even, add the maximum element to the current element and multiply by the maximum element.
# 4b) If the index is odd, add the minimum element to the current element and multiply by the maximum element.
# 5) Iterate through the array and divide each element by the maximum element.
# 6) Return the modified array.


# NOTE: The following is the ONLY possible solution to this specific problem.
# Without using Modulus and Division, the problem is unsolvable in O(1) space complexity.
class Solution:

    def rearrange(self, arr, n):
        left = 0
        right = n - 1
        maxElement = arr[-1] + 1

        for i in range(n):
            if i % 2 == 0:
                arr[i] += (arr[right] % maxElement) * maxElement
                right -= 1
            else:
                arr[i] += (arr[left] % maxElement) * maxElement
                left += 1

        for i in range(n):
            arr[i] = arr[i] // maxElement

        return arr


A = Solution()
print(A.rearrange([1, 2, 3, 4, 5, 6], 6))  # [6, 1, 5, 2, 4, 3]
print(
    A.rearrange([1969, 2677, 3142, 4631, 4764, 5748, 6476, 6487], 8)
)  # [6487, 1969, 6476, 2677, 5748, 3142, 4764, 4631]
