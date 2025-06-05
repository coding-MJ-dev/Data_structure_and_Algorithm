// 217. Contains Duplicate
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        int n = nums.size();
        sort(nums.begin(), nums.end()); // Sort the array

        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1])
                return true;
        }
        return false;
    }
};



// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {

//         int n = nums.size();
//         sort(nums.begin(), nums.end()); // Sort the array

//         for (int i = 1; i < n; i++) {
//             if (nums[i] == nums[i - 1])
//                 return true;
//         }
//         return false;
//     }
// };


// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
//         unordered_set<int> seen;
//         for (int num : nums) {
//             if (seen.count(num)) {
//                 return true;
//             }
//             seen.insert(num);
//         }
//         return false;
//     }
// };


// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
//         unordered_set <int> s;
//         for (int i = 0; i < nums.size(); i++) {
//             if (s.find(nums[i]) != s.end())
//                 return true;
//             else {
//                 s.insert(nums[i]);
//             }
//         }
//         return false;
//     }
// };