class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int>mp;
        for(auto n:nums){mp[n]++;}
        int max_freq=0,max_occ=0;
        for(auto p:mp){ 
            max_freq=max(max_freq,p.second);
        }
        for(auto p:mp){ if(p.second==max_freq){max_occ++;}}
        return max_freq*max_occ;
    }
};