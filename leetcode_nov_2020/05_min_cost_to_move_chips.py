"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:     
        even = odd = 0
        for i in position:
            if i%2 == 0:
                even += 1
            else:
                odd += 1                
        return min(odd, even)