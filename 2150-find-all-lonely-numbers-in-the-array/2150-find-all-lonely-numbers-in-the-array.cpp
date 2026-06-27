class Solution {
public:
    vector<int> findLonely(vector<int>& nums) {
        unordered_map<long long,int>mp;
        for(auto num:nums){mp[num]++;}
        vector<int>lonely;
        for(auto num:nums)
        {
            if(mp[num]==1 &&(mp.find(num-1)==mp.end() && mp.find(num+1)==mp.end()))
            {lonely.push_back(num);}
        }
        return lonely;
    }
};