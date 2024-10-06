// 383. Ransom Note

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> rand;
        unordered_map<char, int> mag;

        for (char& c: ransomNote) {
            rand[c] ++;
        }
        for (char& c: magazine) {
            mag[c] ++;
        }

        for (pair p: rand) {
            char c = p.first;
            if (mag.find(c) == mag.end() || mag[c] < p.second) {
                return false;
            }
        }
        return true;
    }
};