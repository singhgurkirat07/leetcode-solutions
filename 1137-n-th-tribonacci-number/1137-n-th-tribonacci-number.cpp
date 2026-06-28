class Solution {
public:
    unordered_map<int,int>mp;
    int tribonacci(int n) {
        if(n==0){return 0;}
        if(n==1 || n==2){return 1;}
        if(mp.find(n)!=mp.end()){
            return mp[n];
        }
        else{
            mp.insert({n,tribonacci(n-1)+tribonacci(n-3)+tribonacci(n-2)});
        }
        return mp[n];
    }
};