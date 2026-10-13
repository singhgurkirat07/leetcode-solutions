class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(n * n for n in nums)
        
        ans=0

        for i in range(len(squares)):
            if i >= len(squares)//2:
                ans+=squares[i]
            else:
                ans-=squares[i]
        
        return ans