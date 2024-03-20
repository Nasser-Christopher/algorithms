# Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array.
# Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.

# NOTE: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.
# ==============================================================================

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= N <= 10^5
# 0 <= A[i] <= 10^9
# ==============================================================================


class Solution:

    # Function to find equilibrium point in the array.
    # Must be done in O(n) time complexity and O(1) auxiliary space.
    # 1. Create a variable to store the total sum of the array
    # 2. Create a variable to store the left sum
    # 3. Iterate through the array
    # 4. For each iteration, subtract the current element from the total sum
    # 5. If the left sum is equal to the total sum, return the current index
    # 6. Add the current element to the left sum
    # 7. Repeat steps 3-6 until the end of the array
    # 8. Return -1 if no equilibrium point is found

    def equilibriumPoint(self, A, N):
        arrayTotalSum = sum(A)
        leftSum = None

        for i in range(N):
            arrayTotalSum -= A[i]
            if leftSum == arrayTotalSum:
                return i + 1
            leftSum = leftSum + A[i] if leftSum else A[i]
            if N == 1:
                return 1
            if N == 2 and A[i + 1] == 0:
                return i + 1
        return -1


A = Solution()
print(A.equilibriumPoint([1, 3, 5, 2, 2], 5))  # 3
print(A.equilibriumPoint([1], 1))  # 1
print(A.equilibriumPoint([1, 2, 3], 3))  # -1
print(A.equilibriumPoint([1, 0], 2))  # 1
