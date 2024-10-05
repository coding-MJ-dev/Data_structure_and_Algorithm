// 63. Unique Paths II


class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size(), cols = obstacleGrid[0].size();
        vector<long> dp (cols, 0);
        dp[cols-1] = 1;

        for (int i = rows-1; i >= 0; i--) {
            for (int j = cols-1; j >= 0; j--) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                } else if (j < cols -1) {
                    dp[j] = dp[j] + dp[j+1];
                }
            }
        }
        return dp[0];
    }
};