class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        int suf=1;
        for(int j=0;j<nums.size();j++){ans.push_back(suf);suf*=nums[j];}
        suf=1;
        for(int i=nums.size()-1;i>=0;i--){
            
            ans[i]*=suf;
            suf*=nums[i];
        }
        return ans;
    }
};