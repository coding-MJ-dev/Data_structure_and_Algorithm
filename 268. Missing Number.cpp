// 268. Missing Number

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (i != nums[i]) {
                return i;
            }
        }
        return nums.size();
    }
};

// 누가 천재 처럼 풀어놨네.
// class Solution{
// public:
//     int missingNumber(vector<int>& nums) {
//         int n = nums.size();
//         int a = (n * (n+1))/2;
//         int b = 0;
//         for (int num : nums)
//             b += num;
//         return a - b;
//     }
// };