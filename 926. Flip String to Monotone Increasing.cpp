// 926. Flip String to Monotone Increasing


#include <string>
#include <algorithm>

class Solution {
    public:
        int minFlipsMonoIncr(std::string s) {
            int left_ones = 0;
            int right_zeros = count(s.begin(), s.end(), '0');
            int ans = right_zeros;
    
            for (char c : s) {
                if (c == '0') {
                    right_zeros--;
                } else {
                    left_ones += 1;
                }
                ans = std::min(ans, right_zeros + left_ones);
            }
    
            return ans;
        }
    };