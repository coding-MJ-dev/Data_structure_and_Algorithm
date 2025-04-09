// 1911. Maximum Alternating Subsequence Sum

#include <vector>
#include <algorithm>

class Solution {
    public:
        long long maxAlternatingSum(std::vector<int>& nums) {
            long long odd = 0, even = 0;
    
            for (int n: nums) {
                even = std::max(even, odd + n);
                odd = std::max(odd, even - n);
            }
            return even;
        }
    };