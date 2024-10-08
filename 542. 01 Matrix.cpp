// 542. 01 Matrix

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int rows = mat.size(), cols = mat[0].size();
        queue<pair<int, int>> q;
        vector<vector<bool>> seen(rows, vector<bool>(cols, false));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j] == 0) {
                    pair<int, int> p = {i, j};
                    seen[i][j] = true;
                    q.push(p);
                }
            }        
        }
        int count = 1;
        vector<pair<int, int>> dirs = {{1,0}, {-1,0}, {0, 1}, {0,-1}};
        

        while (!q.empty()) {
            int l = q.size();
            for (int i = 0; i < l; i++) {
                pair<int, int> pos = q.front();
                q.pop();
                for (auto& d : dirs) {
                    int r = pos.first + d.first;
                    int c = pos.second + d.second;
                    if (r >= 0 && r < rows && c >= 0 && c < cols && mat[r][c] == 1 && seen[r][c] == false) {
                        mat[r][c] = count;
                        seen[r][c] = true;
                        q.push({r, c});
                    }
                }

            }
            count += 1;
        }

        return mat;
    }
};
