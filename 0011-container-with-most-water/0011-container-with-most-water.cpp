class Solution {
public:
    int maxArea(vector<int>& height) {
        int beg=0,end=height.size()-1;
        long long water=0;
        while(beg<end){
            long long area=1LL*min(height[beg],height[end])*(end-beg);
            water=max(area,water);
            if(height[beg]<height[end]){beg++;}else{end--;}
        }
        return water;
    }
};