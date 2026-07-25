class Solution {
public:
    int maxProduct(int n) {
        string s=to_string(n);
        int max1=-1,max1_idx=0,max2=-1;
        for(int i=0;i<s.length();i++){
            if(max1<s[i]-'0'){
                max1=s[i]-'0';
                max1_idx=i;
            }
        }
        for(int i=0;i<s.length();i++){
            if(max2<s[i]-'0' & i!=max1_idx){
                max2=s[i]-'0';
            }
        }
        return max2*max1;
    }
};