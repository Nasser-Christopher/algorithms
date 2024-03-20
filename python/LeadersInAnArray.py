# Given an array A of positive integers. Your task is to find the leaders in the array.
# An element of array is a leader if it is **greater than or equal to all the elements to its right side**.
# The rightmost element is always a leader.

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    # A is the Array, N is Length of Array
    def leaders(self, A, N):
        # if A[x] >= A[x+1] + A[x+2] + ... + A[N-1]
        # then add A[x] to the list of leaders
        
        # Create a list to store the leaders, and a variable to store the local max
        # slice the array from A[x] to A[N-1]
        # if A[x] >= max(slice) - A[x], then add A[x] to the list of leaders
        answer = [None]
        localMax = None
        arraySlice = None
        
        for i in range(N):
            arraySlice = A[i:N]
            localMax = max(arraySlice) - A[i]
            if A[i] >= localMax:
                answer.append(A[i])
        return answer