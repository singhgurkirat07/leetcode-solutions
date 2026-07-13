class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        string s="123456789";
        vector<int> ans;
        long long lowLen=to_string(low).length(), highLen=to_string(high).length();
        for( auto i=lowLen;i<=highLen;i++){
            long long len=i,beg=0;
            while(beg+len<=s.length() ){
                long long num=stoi(s.substr(beg,len));
                if(num>=low && num<=high){
                ans.push_back(num);}
                beg++;
            }
        }
        return ans;

    }
};