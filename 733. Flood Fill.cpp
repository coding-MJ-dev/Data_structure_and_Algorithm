// 733. Flood Fill

class Solution {
private:
    void dfs(int r, int c, int from_color, int to_color, int rows, int cols, vector<vector<int>>& image) {
        if (r >= 0 && c >= 0 && r < rows && c < cols && image[r][c]==from_color) {
            image[r][c] = to_color;
            dfs(r+1, c, from_color, to_color, rows, cols, image);
            dfs(r-1, c, from_color, to_color, rows, cols, image);
            dfs(r, c+1, from_color, to_color, rows, cols, image);
            dfs(r, c-1, from_color, to_color, rows, cols, image);
        }
    }

public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int rows = image.size(), cols = image[0].size();
        int to_color = image[sr][sc];
        if (to_color == color) {
            return image;
        }
        dfs(sr, sc, to_color, color, rows, cols, image);
        return image;


    }
};