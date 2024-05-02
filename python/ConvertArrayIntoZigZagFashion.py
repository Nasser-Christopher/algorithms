# Given an array arr of distinct elements of size N, the task is to rearrange the elements of the array in a zig-zag fashion
# so that the converted array should be in the below form:

# arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n].

# NOTE: If your transformation is correct, the output will be 1 else the output will be 0.

# Example:

# Input:
# N = 7
# Arr[] = {4, 3, 7, 8, 6, 2, 1}
# Output: 3 7 4 8 2 6 1
# Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1

# Your Task:
# You don't need to read input or print anything.
# Your task is to complete the function zigZag() which takes the array of integers arr and n as parameters and returns void.
# You need to modify the array itself.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


class Solution:
    # Program for zig-zag conversion of array
    # Approach (naive):
    # 1) Swap adjacent elements starting from 1st index to sort adjacent elements from small to large
    # 2) Swap adjacent elements starting from 0th index to sort adjacent elements from large to small
    # 3) Break the loop if no swapping is done (i.e. the array is already in zig-zag fashion)
    # 4) Return the modified array
    def zigZag(self, arr, n):
        while True:
            swapped = False
            for i in range(1, n - 1, 2):
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            for i in range(0, n - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            if not swapped:
                break
        return arr

    # As per the above approach, the time complexity is O(N) since each for loop runs N/2 times.
    # The first for loop runs N/2 times because it only iterates through the odd indices.
    # The second for loop runs N/2 times because it only iterates through the even indices.
    # Even in the worse case run time of O(2N), the time complexity is still O(N) as constants are ignored.
    # The space complexity is O(1) since array is modified in-place.


A = Solution()
print(
    A.zigZag([4, 3, 7, 8, 6, 2, 1], 7)
)  # [3, 7, 4, 8, 2, 6, 1] # NOTE: Apparently this is "wrong", and the "correct answer" is [4, 7, 3, 8, 2, 6, 1] (which is also a zigzag fashion)
print(
    A.zigZag(
        [
            6202,
            4625,
            5469,
            2038,
            5916,
            3405,
            5533,
            7004,
            2469,
            9853,
            4992,
            361,
            9819,
            3294,
            7195,
            4036,
            9404,
            8767,
            5404,
            1711,
            3214,
            3100,
            3751,
            2139,
            5437,
            4993,
            1759,
            9572,
            6270,
            3789,
            9623,
            2472,
            9493,
        ],
        33,
    )
)
