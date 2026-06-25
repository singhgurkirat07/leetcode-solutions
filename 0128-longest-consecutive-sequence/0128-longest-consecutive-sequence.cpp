class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        
        sort(nums.begin(), nums.end());
        
        int len = 1, len_max = 1;
        
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] == nums[i-1] + 1){
                len++;
            }
            else if(nums[i] == nums[i-1]){
            continue;
            }
            else{
                len = 1;
            }
            len_max = max(len, len_max);
        }
        return len_max;
    }
};