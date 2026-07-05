class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans,prefix,suffix(nums.size());
        int pre=1,suf=1;
        for(int j=0;j<nums.size();j++){prefix.push_back(pre);pre*=nums[j];}
        for(int j=nums.size()-1;j>=0;j--){suffix[j]=suf;suf*=nums[j];}
        for(int i=0;i<nums.size();i++){
            ans.push_back(prefix[i]*suffix[i]);
        }
        return ans;
    }
};