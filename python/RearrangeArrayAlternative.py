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

# Logic: Create two variables, one to store the local maximum and the other to store the local minimum.
# From the index at any point in between the array, the left element will be less, and the right element will be greater than the index's value.
# Given that the array is sorted, the first element will be the global minimum and the last element will be the global maximum.

# Approach:
# 1a) index 0 and N-1 are the global minimum and maximum values respectively.
# 1b) Two variables, left and right, are used to store the encountered next-in-line minimum and maximum values.
# 2) Traverse the array from the first element to the last element.
# 3a) If the index is even, store the next maximum value at the index and decrement the right pointer.
# 3b) If the index is odd, store the next minimum value at the index and increment the left pointer.
# 4) Return the modified array.


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
            print(
                f"arr[{i}] => {arr[i]}, left = {left}, right = {right}, maxElement = {maxElement}"
            )

        for i in range(n):
            print(
                f"arr[{i}] => {arr[i]}, arr[{i}] // maxElement = {arr[i] // maxElement}"
            )
            arr[i] = arr[i] // maxElement

        return arr


A = Solution()
print(A.rearrange([1, 2, 3, 4, 5, 6], 6))  # [6, 1, 5, 2, 4, 3]
print(
    A.rearrange([1969, 2677, 3142, 4631, 4764, 5748, 6476, 6487], 8)
)  # [6487, 1969, 6476, 2677, 5748, 3142, 4764, 4631]
