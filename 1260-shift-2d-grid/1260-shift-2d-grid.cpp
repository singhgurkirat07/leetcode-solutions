class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {

        vector<int> matrix;

        int rows = grid.size();
        int cols = grid[0].size();

        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                matrix.push_back(grid[i][j]);
            }
        }

        int total = rows * cols;
        k %= total;

        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){

                int newIndex = i * cols + j;
                int oldIndex = (newIndex - k + total) % total;

                grid[i][j] = matrix[oldIndex];
            }
        }

        return grid;
    }
};