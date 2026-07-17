class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int ans = 0;

        for (int h = 0; h <= n; h++) {
            int cnt = 0;

            for (int i = 0; i < n; i++) {
                if (citations[i] >= h)
                    cnt++;
            }

            if (cnt >= h)
                ans = max(ans, h);
        }

        return ans;
    }
};