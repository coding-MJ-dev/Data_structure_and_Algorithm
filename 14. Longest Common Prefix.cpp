// 14. Longest Common Prefix


#include <string>
#include <vector>

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 1) {
            return strs[0];
        }

        string ans {""};
        sort(strs.begin(), strs.end());
        int len1 = strs[0].size();
        int len2 = strs[strs.size()-1].size();
        int len = min(len1, len2);
        for (int i = 0; i < len; i++) {
            if (strs[0][i] == strs[strs.size()-1][i]) {
                // cout << strs[0][i];
                ans.push_back(strs[0][i]);
            } else {
                break;
            }
        }
        return ans;

    }
};
