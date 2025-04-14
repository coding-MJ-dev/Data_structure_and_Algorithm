// 312. Burst Balloons
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    public:
        int maxCoins(vector<int>& nums) {
            vector<int> balloons(nums.size()+2, 1);
            int n = balloons.size();
    
            for (int i = 1; i < n-1; i++) {
                balloons[i] = nums[i-1];
            }
    
            vector<vector<int>> dp(n, vector<int>(n, 0));
    
            for (int left = n-2; left > 0; left--) {
                for (int right = left; right < n-1; right++) {
                    for (int i = left; i < right + 1; i++) {
                        int lastPop = balloons[left-1] * balloons[i] * balloons[right+1];
                        int remains = dp[left][i-1] + dp[i+1][right];
                        dp[left][right] = max(dp[left][right], lastPop + remains);
                    }
                }
            }
    
            return dp[1][n-2];
    
        }
    };