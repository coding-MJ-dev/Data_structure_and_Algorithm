// 376. Wiggle Subsequence


class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }

        int last = 0, ans = 1;
        for (int i = 1; i < nums.size(); i++) {
            if ((nums[i] - nums[i - 1] > 0 && last <= 0) || (nums[i] - nums[i - 1] < 0 && last >= 0)) {
                last = nums[i] - nums[i - 1];
                ans += 1;
            }
        }
        return ans;
    }
};