class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        vector<pair<int,int>> v;
        for( auto num:arr){v.push_back({__builtin_popcount(num),num});}
        vector<int> ans;
        sort(v.begin(), v.end());
        for(auto p:v){ans.push_back(p.second);}
        return ans;

    }
};