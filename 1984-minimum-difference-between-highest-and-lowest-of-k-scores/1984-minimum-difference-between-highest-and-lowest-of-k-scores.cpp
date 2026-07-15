class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int left=0,right=left+k-1,ans=INT_MAX;
        sort(nums.begin(),nums.end());
        while(right<nums.size()){
            auto min_ele=min_element(nums.begin()+left,nums.begin()+right+1);
            auto max_ele=max_element(nums.begin()+left,nums.begin()+right+1);
            ans=min(ans,*max_ele-*min_ele);
            left++;right++;
        }
        return ans;
    }

};