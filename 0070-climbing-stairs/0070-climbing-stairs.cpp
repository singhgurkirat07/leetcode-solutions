class Solution {
public:
    unordered_map<int,int> mp;
    int climbStairs(int n) {
        if(n==1){return 1;}
        if(n==2){return 2;}
        
        if(mp.find(n)!=mp.end()){return mp[n];}
        else{
            mp.insert({n,climbStairs(n-1)+climbStairs(n-2)});
            }
        return mp[n];
    }
};