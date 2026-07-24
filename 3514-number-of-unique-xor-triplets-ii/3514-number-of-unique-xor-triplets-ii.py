class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        st=set()
        ans=set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                st.add(nums[i]^nums[j])
        
        for i in st:
            for j in range(len(nums)):
                ans.add(nums[j]^i)

        return len(ans)
        
