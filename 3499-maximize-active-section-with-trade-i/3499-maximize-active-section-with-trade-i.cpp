class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        string t="1"+s+"1";
        int orgone=0;
        for(auto x:s){
            if(x=='1')orgone++;
        }
        vector<char>run;
        vector<int>freq;
        int n=t.length(),i=0,num=1;
        while(i<n-1){
            char ch=t[i];
            if(t[i+1]==ch){
                num++;
            }
            else{
                freq.push_back(num);
                run.push_back(ch);
                num=1;
            }
            i++;
        }
        run.push_back(t[n-1]);
        freq.push_back(num);
        
        int ans=orgone;
        for(int i=0;i+2<run.size();i++){
            if(run[i]=='0' && run[i+1]=='1' && run[i+2]=='0'){
                ans=max(ans,orgone+freq[i]+freq[i+2]);
            }
        }
        return ans;
    }
};