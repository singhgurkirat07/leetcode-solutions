class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int dip=-1;
        for(int i=nums.size()-2;i>=0;i--){
            if(nums[i]< nums[i+1]){dip=i;break;}
        }
        if(dip == -1){
            reverse(nums.begin(), nums.end());
              return;
        }
        int min=nums[dip+1],min_index=dip+1;;
        for(int i=dip+1;i<nums.size();i++){
            if(min>=nums[i] && nums[i]>nums[dip]){
                min=nums[i];
                min_index=i;
                }
        }
        swap(nums[dip],nums[min_index]);
        reverse(nums.begin()+dip+1,nums.end());
    }
};