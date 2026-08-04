class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_ele=min(nums)
        max_ele=max(nums)
        ans=[]

        for i in range(min_ele,max_ele+1):
            if i not in nums:
                ans.append(i)

        return ans