//994. Rotting Oranges

class Solution {
    int orange {0};
    queue<pair<int,int>> rot;

public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    rot.push({i, j});
                } else if (grid[i][j] == 1) {
                    orange++;
                }
            }
        }

        int time {0};
        vector<pair<int, int>> dirs = {{1,0}, {-1,0}, {0,1}, {0, -1}};
        while (!rot.empty() && orange > 0) {
            int size = rot.size();
            while (size > 0) {
                int r = rot.front().first;
                int c = rot.front().second;
                rot.pop();
                size--;
                for (auto& dir: dirs){
                    int nr = r + dir.first;
                    int nc = c + dir.second;
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc]==1) {
                        rot.push({nr, nc});
                        grid[nr][nc] = 2;
                        orange--;
                    }
                }
                
            }
            time++;
        }
        if (orange > 0) {
            return -1;
        } else {
            return time;
        }

    }
};