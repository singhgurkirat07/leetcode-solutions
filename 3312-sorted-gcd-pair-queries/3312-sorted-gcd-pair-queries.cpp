class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        vector<int> freq(50001, 0);
        vector<long long> gcdFreq(50001);

        for (auto x : nums) {
            freq[x]++;
        }

        for (int g = 1; g <= 50000; g++) {
            long long cnt = 0;
            for (int m = g; m <= 50000; m += g) {
                cnt += freq[m];
            }
            gcdFreq[g] = cnt * (cnt - 1) / 2;
        }

        for (int g = 50000; g > 0; g--) {
            for (int m = 2; m * g <= 50000; m++) {
                gcdFreq[g] -= gcdFreq[g * m];
            }
        }

        vector<long long> prefix(50001);

        for (int i = 1; i <= 50000; i++) {
            prefix[i] = prefix[i - 1] + gcdFreq[i];
        }

        vector<int> ans;

        for (auto q : queries) {
            int g =
                upper_bound(prefix.begin(), prefix.end(), q) - prefix.begin();
            ans.push_back(g);
        }

        return ans;
    }
};