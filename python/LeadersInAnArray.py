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
        answer = []
        localMax = None
        arrayWindow = None
        
        for i in range(N):
            arrayWindow = A[i:N]
            localMax = max(arrayWindow)
            if A[i] >= localMax:
                answer.append(A[i])
                
        return answer
            
        
        