// 70. Climbing Stairs


class Solution {
public:
    int climbStairs(int n) {
        int step1 = 1;
        int step2 = 1;

        if (n <= 2) {
            return n;
        }

        for (int i = 2; i < n+1; i++) {
            int temp = step1 + step2;
            step1 = step2;
            step2 = temp;
        }
        return step2;

    }
};
