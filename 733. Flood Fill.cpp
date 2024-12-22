// 733. Flood Fill


class Solution {
public:
    void dfs(int i, int j, int rows, int cols, int origin, int color, vector<vector<int>>& image) {
        if (i < 0 || i == rows || j < 0 || j == cols || image[i][j] != origin) return;

        image[i][j] = color;
        dfs(i+1, j, rows, cols, origin, color, image);
        dfs(i-1, j, rows, cols, origin, color, image);
        dfs(i, j+1, rows, cols, origin, color, image);
        dfs(i, j-1, rows, cols, origin, color, image);
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int rows = image.size(), cols = image[0].size();
        int origin = image[sr][sc];
        if (origin != color) {
            dfs(sr, sc, rows, cols, origin, color, image);
        }
        
        return image;
    }
};


//// bfs
// #include <vector>
// #include <queue>
// using namespace std;

// class Solution {
// public:
//     vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
//         int currentColor = image[sr][sc];
//         if (currentColor == color) return image; // Avoid processing if the color is already the same

//         int rows = image.size();
//         int cols = image[0].size();

//         // Use an iterative BFS approach to avoid stack overflow with deep recursion
//         queue<pair<int, int>> q;
//         q.push({sr, sc});

//         while (!q.empty()) {
//             auto [x, y] = q.front();
//             q.pop();

//             if (x < 0 || x >= rows || y < 0 || y >= cols || image[x][y] != currentColor) {
//                 continue;
//             }

//             // Update the color of the current pixel
//             image[x][y] = color;

//             // Push adjacent pixels onto the queue
//             q.push({x + 1, y}); // Down
//             q.push({x - 1, y}); // Up
//             q.push({x, y + 1}); // Right
//             q.push({x, y - 1}); // Left
//         }

//         return image;
//     }
// };
