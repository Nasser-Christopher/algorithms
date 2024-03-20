# Given an array A of positive integers. Your task is to find the leaders in the array.
# An element of array is a leader if it is **greater than or equal to all the elements to its right side**.
# The rightmost element is always a leader.

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    # A is the Array, N is Length of Array
    def leaders(self, A, N):
        
        
        # Wrong Solution (Summation):
        # if A[x] >= A[x+1] + A[x+2] + ... + A[N-1]
        # then add A[x] to the list of leaders
        # 1.Create a list to store the leaders, and a variable to store the local max
        # 2.slice the array from A[x] to A[N-1]
        # 3.if A[x] >= max(slice) - A[x], then add A[x] to the list of leaders
        
        # Real Solution (Comparison):
        # The value at A[x] must be greater than the INDIVIDUAL VALUES to its right, not the summation of said values.
        # NOTE: using a for loop with a max() function will be O(n^2) time complexity, which fails the time limit.
        
        # 1.Create a list to store the leaders, and a variable to store the current max
        # 2.Start from the rightmost element, and add it to the list of leaders
        # 3.Slice the array from A[N-2] to A[0]
        # 4.if A[x] >= currentMax, then add A[x] to the list of leaders
        # 5.Update currentMax to A[x]
        # 6.Repeat steps 3-5 until the end of the array
        # 7.Reverse the list of leaders and return it
        answer = []
        
        currentMax = A[N-1]
        answer.append(currentMax)
        for i in range(N-2, -1, -1):
            if A[i] >= currentMax:
                currentMax = A[i]
                answer.append(currentMax)
        
        return answer[::-1]
            
        
A = Solution()
print(A.leaders([63,70,80,33,33,47,20], 7)) # [80, 47, 20]