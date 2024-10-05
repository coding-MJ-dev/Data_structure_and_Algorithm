// 200. Number of Islands

class Solution {
    int rows;
    int cols;
    // vector<vector<char>> grid;

public:
    void sink(int r, int c, vector<vector<char>>& grid) {

        if (0 <= r && r < rows && 0 <= c && c < cols && grid[r][c] == '1') {
            grid[r][c] = '0';

            sink(r+1, c, grid);
            sink(r-1, c, grid);
            sink(r, c+1, grid);
            sink(r, c-1, grid);
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        rows = grid.size();
        cols = grid[0].size();
        // grid = grid;

        int res = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    sink(i, j , grid);
                    res++;
                }
            }
        }
        return res;


    }
};