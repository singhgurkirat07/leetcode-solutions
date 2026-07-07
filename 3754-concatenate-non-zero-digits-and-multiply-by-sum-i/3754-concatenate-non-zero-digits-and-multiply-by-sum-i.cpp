class Solution {
public:
    long long sumAndMultiply(int n) {
        long long sum=0;
        long long num=0,num_final=0;
        while(n>0){
            long long a=n%10;
            if(a!=0){
                sum+=a;
                num=num*10+a;
            }
            n/=10;
        }
        while(num>0){
            int a=num%10;
            num_final=num_final*10+a;
            num/=10;
        }
        return sum*num_final;
    }
};