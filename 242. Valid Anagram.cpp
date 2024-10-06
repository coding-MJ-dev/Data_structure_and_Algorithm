// 242. Valid Anagram


class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        unordered_map<char, int> dicS, dicT;

        for (int i = 0; i < s.size(); i++) {
            dicS[s[i]]++;
            dicT[t[i]]++;
        }

        for (auto& pair : dicS) {
            char c = pair.first;
            if (dicT.find(c) == dicT.end() || dicT[c] != pair.second) {
                return false;
            }
        }
        return true;
    }
};
