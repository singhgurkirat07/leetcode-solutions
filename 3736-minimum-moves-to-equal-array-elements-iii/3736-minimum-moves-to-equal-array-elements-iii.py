class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxim=max(nums)
        moves=0

        for num in nums:
            moves+=maxim-num
        
        return moves