// 611. Valid Triangle Number

#include <vector>
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int ans = 0;
        sort(nums.begin(), nums.end());
        for (int r = 2; r < nums.size(); r++) {
            int l = 0, m = r - 1;
            while (l < m) {
                if (nums[l] + nums[m] > nums[r]) {
                    ans += m - l;
                    m -= 1;
                } else {
                    l += 1;
                }
            }
        }
        return ans;
    }
};