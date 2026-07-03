class Solution {
public:
    int bitwiseComplement(int n) {
        if(n==0){return 1;}
        string s = bitset<32>(n).to_string();
        s = s.substr(s.find('1'));
        for( auto &n:s){
            if(n=='1'){n='0';}else{n='1';}
        }
        
        return  stoll(s, nullptr, 2);
    }
};