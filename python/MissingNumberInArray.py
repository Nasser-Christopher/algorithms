# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

# Example 1:

# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4

# Your Task :
# You don't need to read input or print anything.
# Complete the function MissingNumber() that takes array and N as input parameters
# and returns the value of the missing number.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Logic: N is the largest value, so the expected value sum would be N*(N+1)/2
# There is always ONLY ONE missing element. So, the sum of the given array will be [N*(N+1)/2 - missing element]
# Thus you take the difference between the expected value sum and the sum of the given array to get the missing element.
# NOTE: The above logic only works if the array is sorted.
# In the case that the array is not sorted, you can sort the array and then apply the logic.
# if this is too slow, you can use the following approach:


# Approach:
# 1) Add up the array elements
# 2) Subtract the sum from the expected sum N*(N+1)/2
# 3) Return the difference number


class Solution:
    def missingNumber(self, array, n):
        expected = n * (n + 1) // 2
        evaluatedNow = None
        evaluated = 0
        while array != []:
            # following line is technically not needed; kept since answer submitted to GeeksForGeeks
            if evaluatedNow is None:
                evaluatedNow = array[-1]

            evaluatedNow = array.pop()
            evaluated += evaluatedNow

        return expected - evaluated
        # code here


A = Solution()
print(A.missingNumber([1, 2, 3, 5], 5))  # 4
