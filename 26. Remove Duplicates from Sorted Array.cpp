#include <vector>

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 1) {
            return nums.size();
        }
        
        int i = 1;
        int j = 1;
        while (i < nums.size()) {
            if (nums[i] != nums[j-1]) {
                nums[j] = nums[i];
                i++;
                j++;
            } 
            else {
                i++;
            }
        }
        return j;
    }
};