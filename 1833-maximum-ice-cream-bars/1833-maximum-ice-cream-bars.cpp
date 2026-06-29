class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        map<int,int>mp;int n=0;

        for(auto cost:costs){mp[cost]++;}

        while(!mp.empty()){
            auto it=mp.begin();
            if(coins>=it->first){
                coins-=it->first;
                it->second--;
                if (it->second == 0) {
                    mp.erase(it);
                }
                n++;
            }
            else{return n;}
        }
        return n;
    }
};