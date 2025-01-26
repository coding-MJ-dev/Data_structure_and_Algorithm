// 808. Soup Servings

#include <vector>

class Solution {
public:
    vector<vector<double>> dp;
    double dfs(int a, int b) {
        if (a <= 0 && b <= 0) return 0.5;
        if (a <= 0) return 1.0;
        if (b <= 0) return 0.0;

        if (dp[a][b] != -1.0)
            return dp[a][b];

        double total = 0.0;
        total = (dfs(a-4, b) + dfs(a-3, b-1) + dfs(a-2, b-2) + dfs(a-1,b-3)) / 4;
        dp[a][b] = total;

        return dp[a][b];
    }

    double soupServings(int n) {
        if (n > 5000) return 1.0;
        
        n = ceil(n/25.0);
        dp.resize(n + 1, vector<double>(n + 1, -1.0));
        return dfs(n, n);
    }
};