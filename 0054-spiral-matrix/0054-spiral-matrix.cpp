class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>ans;
        int left=0,right=matrix[0].size()-1;
        int top=0,bottom=matrix.size()-1;
        while(ans.size()<matrix.size()*matrix[0].size()){
            for(int i=left;i<=right;i++){
                ans.push_back(matrix[top][i]);
                
            }
            top++;
            for(int j=top;j<=bottom;j++){
                ans.push_back(matrix[j][right]);
                
            }
            right--;
            if(top<=bottom){
            for(int i=right;i>=left;i--){
                ans.push_back(matrix[bottom][i]);
                
            }
            bottom--;
            }
            if(left<=right){
            for(int j=bottom;j>=top;j--){
                ans.push_back(matrix[j][left]);
            }
            left++;
            }
        }
        return ans;
    }

};