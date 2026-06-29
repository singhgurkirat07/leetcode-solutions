class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        long long maj1=0,maj2=1;
        int cnt1=0,cnt2=0;
        for(int num:nums){
            if(num==maj1){cnt1++;}
            else if(num==maj2){cnt2++;}
            else if(cnt1==0){maj1=num;cnt1++;}
            else if(cnt2==0){maj2=num;cnt2++;}
            else{cnt1--;cnt2--;}
        }
        int counter1=0,counter2=0;
        vector<int> ans;
        for(auto num:nums){if(num==maj1){counter1++;}if(num==maj2){counter2++;}}
        if(counter1>nums.size()/3){ans.push_back(maj1);}
        if(counter2>nums.size()/3){ans.push_back(maj2);}
        return ans;
    }
};