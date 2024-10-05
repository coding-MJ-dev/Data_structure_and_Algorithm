// 190. Reverse Bits


class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        long res {0};
        long digit;

        for (int i = 31; i >=0; i--) {
            digit = n & 1;
            res += digit << i;
            n >>= 1;
        }
        return res;
    }
};