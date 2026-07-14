class Solution {
public:
    int addDigits(int num) {
        while(to_string(num).length()>1){
            int n=0,len=to_string(num).length();
            string s=to_string(num);
            for (char c : s)
                n += c - '0';
            num=n;
        }
        return num;
    }
};