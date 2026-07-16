class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        vector<long long> prefixGcd;
        int mx=INT_MIN;
        for(int i=0;i<nums.size();i++){
            mx=max(mx,nums[i]);
            prefixGcd.push_back(gcd(nums[i],mx));
        }
        sort(prefixGcd.begin(),prefixGcd.end());

        int i=0,j=prefixGcd.size()-1;
        long long ans=0;
        while(i<j){
            ans+=gcd(prefixGcd[i],prefixGcd[j]);i++;j--;
        }
        return ans;
    }
};