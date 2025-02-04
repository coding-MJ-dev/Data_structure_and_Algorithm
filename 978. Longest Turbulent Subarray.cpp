// 978. Longest Turbulent Subarray


class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int ans {1};
        int increasing {1}, decreasing {1};
        int pre_num = arr[0];

        for (int n : arr) {
            if (n > pre_num) {
                increasing = decreasing + 1;
                decreasing = 1;
            } else if (n < pre_num) {
                decreasing = increasing + 1;
                increasing = 1;
            } else {
                decreasing = 1;
                increasing = 1;
            }
            pre_num = n;
            ans = max({ans, increasing, decreasing});
        }

        return ans;
    }
};