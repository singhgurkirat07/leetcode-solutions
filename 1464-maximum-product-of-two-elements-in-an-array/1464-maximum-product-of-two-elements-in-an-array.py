class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        idx1=0
        for i in range(len(nums)):
            if nums[i]>nums[idx1]:
                idx1=i
        max1=nums[idx1]
        nums.pop(idx1)

        idx2=0
        for i in range(len(nums)):
            if nums[i]>nums[idx2]:
                idx2=i
        max2=nums[idx2]
        nums.pop(idx2)
        
        return (max1-1)*(max2-1)

