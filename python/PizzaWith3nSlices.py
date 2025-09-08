class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        pass
    
    
# if x->front + x->back > Choiceₓ + xₙ 
#   if x->front == x->back
        # Figure out which has the better Choiceₓ + xₙ 
#   else
#       go with the larger x (x->front or x-> back)
# else 
# Choiceₓ + xₙ are added up as long as xₙ (new Choiceₓ) + a new xₙ are greater than x->front/back
# This makes the choosing recursively pick the largest sum