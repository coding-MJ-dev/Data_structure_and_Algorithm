// 74. Search a 2D Matrix


#include <vector>

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0, r = matrix.size() -1;
        int len = matrix[0].size();

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (target > matrix[m][len-1]) {
                l = m + 1;
            } else if (target < matrix[m][0]) {
                r = m - 1;
            } else {
                // std::cout << m;
                int left = 0, right = len -1;
                while (left <= right) {
                    int mid = left + (right - left) / 2;
                    if (matrix[m][mid] == target) {
                        return true;
                    } else if (target < matrix[m][mid]) {
                        right = mid - 1;
                    } else {
                        left = mid + 1;
                    }
                }
                return false;
            }
        }
        return false;
    }
};