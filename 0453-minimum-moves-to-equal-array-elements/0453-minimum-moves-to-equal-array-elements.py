class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minim=min(nums)
        moves=0

        for num in nums:
            moves+=(num-minim)
        
        return moves
        