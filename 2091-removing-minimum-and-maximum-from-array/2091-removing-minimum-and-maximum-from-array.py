class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        min_idx=0
        max_idx=0

        for i in range(len(nums)):
            if nums[i]>=nums[max_idx]:
                max_idx=i

            if nums[i]<=nums[min_idx]:
                min_idx=i
            
        left=min(min_idx,max_idx)
        right=max(min_idx,max_idx)

        left_removal=right+1
        right_removal=n-left
        dual_removal=left+1+(n-right)

        return min(left_removal,right_removal,dual_removal)
            
        
            