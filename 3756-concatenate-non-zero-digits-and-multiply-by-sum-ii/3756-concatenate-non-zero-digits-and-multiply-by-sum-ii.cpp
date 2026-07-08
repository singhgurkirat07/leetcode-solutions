class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        const long long MOD = 1e9 + 7;

        vector<long long> preSum, preNum, cnt, pow10;

        long long sum = 0, Num = 0;
        int cntNonzero = 0;

        int n = s.length();

        // Precompute powers of 10
        pow10.resize(n + 1);
        pow10[0] = 1;
        for (int i = 1; i <= n; i++)
            pow10[i] = (pow10[i - 1] * 10) % MOD;

        // Prefix preprocessing others
        for (int i = 0; i < n; i++) {
            int d = s[i] - '0';

            if (d != 0) {
                sum += d;
                Num = (Num * 10 + d) % MOD;
                cntNonzero++;
            }

            preSum.push_back(sum);
            preNum.push_back(Num);
            cnt.push_back(cntNonzero);
        }

        vector<int> ans;

        for (int i = 0; i < queries.size(); i++) {

            int l = queries[i][0];
            int r = queries[i][1];

            long long digitSum;
            long long num;
            int digits;

            if (l == 0) {
                digitSum = preSum[r];
                num = preNum[r];
            } else {
                digitSum = preSum[r] - preSum[l - 1];

                digits = cnt[r] - cnt[l - 1];

                num = (preNum[r]
                      - (preNum[l - 1] * pow10[digits]) % MOD
                      + MOD) % MOD;
            }

            ans.push_back((digitSum * num) % MOD);
        }

        return ans;
    }
};