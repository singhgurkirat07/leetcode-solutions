class Solution {
public:
    double area(vector<int> a,vector<int>b,vector<int> c){
        return abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2.0;
    }
    double largestTriangleArea(vector<vector<int>>& points) {
        double ans=0;
        for(int i=0;i<points.size();i++)
        {
            for(int j=i+1;j<points.size();j++){
                for(int k=j+1;k<points.size();k++){
                    double a=area(points[i],points[j],points[k]);
                    ans=max(ans,a);}}}
        return ans;
    }
};