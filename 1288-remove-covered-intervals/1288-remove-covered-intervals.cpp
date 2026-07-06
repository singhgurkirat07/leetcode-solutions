class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty())return 0;
        sort(intervals.begin(), intervals.end(),[](vector<int>& a, vector<int>& b) {
        if (a[0] == b[0])
            return a[1] > b[1];   // larger end first
        return a[0] < b[0];       // smaller start first
     });
        int cnt=1;
        int max_end=intervals[0][1];
        for(auto i=1;i<intervals.size();i++){
            if (intervals[i][1]>max_end){cnt++;max_end=intervals[i][1];}
        }
        return cnt;
    }
};