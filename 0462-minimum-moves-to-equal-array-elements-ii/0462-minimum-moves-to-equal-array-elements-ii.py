class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        median=0

        if n%2==0:
            median=(nums[(n//2)-1]+nums[(n//2)])/2
        else:
            median=nums[n//2]
        
        moves=0
        for num in nums:
            moves+=abs(median-num)
        
        return int(moves)
        