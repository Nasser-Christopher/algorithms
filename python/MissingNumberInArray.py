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

# Approach:
# 1)


class Solution:
    def missingNumber(self, array, n):
        pass
        # code here


A = Solution()
print(A.missingNumber([1, 2, 3, 5], 5))  # 4
