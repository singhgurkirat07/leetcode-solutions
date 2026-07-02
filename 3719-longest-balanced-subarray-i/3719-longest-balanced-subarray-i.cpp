class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int max_len=0;for(int i=0;i<nums.size();i++){unordered_map<int,int> even,odd;for(int j=i;j<nums.size();j++){ if(nums[j]%2==0)even[nums[j]]++;else{odd[nums[j]]++;} if(even.size()==odd.size()){int len= j - i + 1;;max_len=max(max_len,len);}}}return max_len;
    }
};