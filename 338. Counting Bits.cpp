// 338. Counting Bits


class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res (n+1);

        if (n == 0) {
            return res;
        }
        res[0] = 0;
        res[1] = 1;
        if (n == 0) {
            return res;
        }

        int pivot = 1;
        for (int i = 2; i < n+1; i++) {
            if (i / 2 == pivot) {
                pivot = i; 
            }
            res[i] = 1 + res[i % pivot];

        }
        return res;
    }
};