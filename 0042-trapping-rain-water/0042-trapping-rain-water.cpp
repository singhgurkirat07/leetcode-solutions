class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty())
            return 0;
        vector<int> leftpeak, rightpeak(height.size());
        int peak = height[0];
        for (auto h : height) {
            peak = max(peak, h);
            leftpeak.push_back(peak);
        }
        peak = height[height.size() - 1];
        for (int i = height.size() - 1; i >= 0; i--) {
            if (height[i] > peak) {
                peak = height[i];
            }
            rightpeak[i] = peak;
        }

        int water = 0;

        for (int i = 0; i < height.size(); i++) {
            water += min(leftpeak[i], rightpeak[i]) - height[i];
        }
        return water;
    }
};