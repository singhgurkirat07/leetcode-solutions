class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> mp;
        int left=0;
        int max_len=0,curr_len=0;
        if(s.length()==0)return 0;
        for (int i = 0; i < s.length(); i++) {

            if (mp.find(s[i]) != mp.end()) {
            left = max(left, mp[s[i]] + 1);
            }

            curr_len = i - left + 1;
            mp[s[i]] = i;
            max_len = max(max_len, curr_len);  
        }
        return max_len;
    }
};