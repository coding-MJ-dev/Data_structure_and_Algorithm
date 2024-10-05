// 191. Number of 1 Bits


class Solution {
public:
    int hammingWeight(int n) {
        int bit = 0;
        int res = 0;
        while (n > 0) {
            bit = n & 1;
            res += bit;
            n >>= 1;
        }
        return res;
    }
};