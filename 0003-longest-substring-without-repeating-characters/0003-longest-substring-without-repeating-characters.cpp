class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string ans="";
        int max_len=0,curr_len=0;

        for(int i=0;i<s.length();i++){

            if(ans.find(s[i])==string::npos){
                ans+=s[i];
                curr_len+=1;
                max_len=max(max_len,curr_len);
            }


            else if(ans.find(s[i])!=string::npos){
                 while (ans.find(s[i]) != string::npos) {
                    ans.erase(ans.begin());
                    curr_len--;
                }
                ans+=s[i];
                curr_len++;;
                max_len=max(max_len,curr_len);
                }
        }
        return max_len;
    }
};