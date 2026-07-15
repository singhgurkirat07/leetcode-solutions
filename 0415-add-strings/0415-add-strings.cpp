class Solution {
public:
    string addStrings(string num1, string num2) {
        int i=num1.length()-1,j=num2.length()-1,carry=0;
        string ans="";
        while(i>=0 && j>=0){
            int sum=carry;
            sum+=(num1[i]-'0')+(num2[j]-'0');
            i--;j--;
            carry=sum/10;
            sum%=10;
            ans+=to_string(sum);
        }
        while(i>=0){
            int sum=carry;
            sum+=(num1[i]-'0');
            carry=sum/10;
            sum%=10;
            ans+=to_string(sum);
            i--;
        }
        while(j>=0){
            int sum=carry;
            sum+=(num2[j]-'0');
            carry=sum/10;
            sum%=10;
            ans+=to_string(sum);
            j--;
        }
        if(carry){
            ans+=to_string(carry);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};