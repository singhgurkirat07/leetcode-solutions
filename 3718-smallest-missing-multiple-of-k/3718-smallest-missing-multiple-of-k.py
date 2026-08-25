class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num=set(nums)
        ans=0
        n=k
        while n in num:
            n+=k
        return n
        
    