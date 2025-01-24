// 1968. Array With Elements Not Equal to Average of Neighbors

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& n) {
        for(int i = 1;i<n.size()-1;i++){
            if((n[i] < n[i-1] and n[i] > n[i+1]) || (n[i] > n[i-1] and n[i] < n[i+1])){
                swap(n[i],n[i+1]);
            }
        }
        return n;
    }
};

// class Solution {
// public:
//     vector<int> rearrangeArray(vector<int>& nums) {
//         sort(nums.begin(), nums.end());
//         vector<int> ans;
//         int l = 0, r = nums.size() - 1;
//         while (l <= r) {
//             ans.push_back(nums[l]);
//             l++;
//             if (l < r) {
//                 ans.push_back(nums[r]);
//                 r--;
//             }
//         }
//         return ans;
//     }
// };