class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<int> i_pos;
        vector<int> j_pos;
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                if(matrix[i][j]==0){
                    i_pos.push_back(i);
                    j_pos.push_back(j);
                }
            }
        }
        
        for( int i=0;i<i_pos.size();i++){
            for(int row=0;row<matrix.size();row++){
                matrix[row][j_pos[i]]=0;
            }
        }
        for( int i=0;i<i_pos.size();i++){
            for(int col=0;col<matrix[0].size();col++){
                matrix[i_pos[i]][col]=0;
            }
        }
    }
};