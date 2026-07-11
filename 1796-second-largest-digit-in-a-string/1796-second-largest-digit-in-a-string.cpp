class Solution {
public:
    int secondHighest(string s) {
        int max_val=INT_MIN,max_2val=INT_MIN;
        for( auto digit:s ){ 
            if(digit>='0' && digit<='9'){
                max_val=max(max_val,digit-'0');
            }
        }
        
        for( auto digit:s ){ 
            if(digit>='0' && digit<='9' && digit-'0'<max_val){
                max_2val=max(max_2val,digit-'0');
            }
        }
        if(max_2val!=INT_MIN )return max_2val;
        return -1;
    }
};