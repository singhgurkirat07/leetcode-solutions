class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n=citations.size();
        vector<int> counter(n+1,0);
        for(int c:citations){
            counter[min(c,n)]++;
        }
        int papers=0;
        for(int h=n;h>0;h--){
            papers+=counter[h];
            if(papers>=h)return h;
        }
        return 0;
    }
};