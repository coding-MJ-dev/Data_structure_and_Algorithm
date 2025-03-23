// 3. Longest Substring Without Repeating Characters


#include <string>
#include <unordered_map>
using namespace std;

class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            unordered_map<char, int> map;
            int left = 0, ans = 0;
            int n = s.length();
            for (int right = 0; right < n; right++) {
                if (map.find(s[right]) != map.end() && map[s[right]] >= left) {
                    left = map[s[right]] + 1;
                }
                map[s[right]] = right;
                ans = max(ans, right - left + 1);
            }
            return ans;
        }
    };
    
    
    
    
    