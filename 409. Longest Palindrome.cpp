// 409. Longest Palindrome

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map <char, int> dic;
        for (char& c: s) {
            dic[c]++;
        }
        int ans = 0;
        int odd = 0;
        for (auto& p: dic) {
            if (p.second % 2 == 0) {
                ans += p.second;
            } else {
                odd = 1;
                ans += p.second -1;
            }
        }
        return ans + odd;
    }
};