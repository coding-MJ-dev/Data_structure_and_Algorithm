// 238. Product of Array Except Self

#include <vector>

class Solution {
    public:
        std::vector<int> productExceptSelf(std::vector<int>& nums) {
            int prefix {1};
            int n = nums.size();
            std::vector<int> ans(nums.size(), 1);
    
            for (int i = 0; i < n; i++) {
                ans[i] *= prefix;
                prefix *= nums[i];
                // i++; 
            }
    
            int suffix {1};
            for (int i = n-1; i > -1; i--) {
                ans[i] *= suffix;
                suffix *= nums[i];
                // i++; 
            }
            return ans;
        }
    };