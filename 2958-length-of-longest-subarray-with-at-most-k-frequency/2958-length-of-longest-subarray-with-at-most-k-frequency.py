class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        ans=0
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
                
            else:
                freq[nums[i]]+=1
                if freq[nums[i]]>k:
                    while freq[nums[i]]>k:
                        freq[nums[left]]-=1
                        left+=1
            right+=1
            ans=max(ans,right-left)
        return ans