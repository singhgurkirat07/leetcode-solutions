class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans=strs[0];
        for(int i=1;i<strs.size();i++){ 
            string curr_str="";
            for( int j=0;j<min(ans.size(), strs[i].size());j++){ 
            if(strs[i][j]!=ans[j]){break;}
            else{
                curr_str+=strs[i][j];
            }}
            ans=curr_str;
            if (ans.empty()) return "";
            }
        return ans;

    }
};