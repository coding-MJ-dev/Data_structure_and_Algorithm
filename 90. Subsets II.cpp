// 90. Subsets II

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        vector<int> cur;
        dfs(0, cur, ans, nums);
        return ans;
    }
private:
    void dfs(int i, vector<int>& cur, vector<vector<int>>& ans, vector<int>& nums) {
        if (i == nums.size()) {
            ans.push_back(cur);
            return;
        }

        cur.push_back(nums[i]);
        dfs(i+1, cur, ans, nums);
        while (i+1 < nums.size() && nums[i] == nums[i+1]) {
            i++;
        }
        cur.pop_back();
        dfs(i+1, cur, ans, nums);
    }
};



// class Solution {
// public:
//     void subArr(int ind, vector<int>& nums, vector<int>& ds, vector<vector<int>>& ans) {
//         ans.push_back(ds);
//         int len = nums.size();
        
//         for (int i = ind; i < len; i++) {
//             if (i > ind && nums[i] == nums[i - 1])  
//                 continue;  
            
//             ds.push_back(nums[i]);
//             subArr(i + 1, nums, ds, ans);
//             ds.pop_back();
//         }
//     }

//     vector<vector<int>> subsetsWithDup(vector<int>& nums) {
//         vector<vector<int>> ans;
//         vector<int> ds;
//         sort(nums.begin(), nums.end());  
//         subArr(0, nums, ds, ans);
//         return ans;
//     }
// };