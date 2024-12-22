// 242. Valid Anagram
#include <unordered_map>
#include <string>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        std::unordered_map<char,int> mp;

        for (char& c: s) mp[c]++;
        for (char& c: t) {
            if (mp[c] == 0) return false;
            mp[c]--;
        }
        return true;
    }
};


// class Solution {
// public:
//     bool isAnagram(string s, string t) {
//         if (s.length() != t.length()) return false;

//         sort(s.begin(), s.end());
//         sort(t.begin(), t.end());

//         return s == t;
//     }
// };




// class Solution {
// public:
//     bool isAnagram(string s, string t) {
//         if (s.length() != t.length()){
//             return false;
//         }

//         unordered_map<char, int> dicS, dicT;

//         for (int i = 0; i < s.size(); i++) {
//             dicS[s[i]]++;
//             dicT[t[i]]++;
//         }

//         for (auto& pair : dicS) {
//             char c = pair.first;
//             if (dicT.find(c) == dicT.end() || dicT[c] != pair.second) {
//                 return false;
//             }
//         }
//         return true;
//     }
// };
