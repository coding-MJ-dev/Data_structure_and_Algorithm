// 215. Kth Largest Element in an Array

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> hp;
        
        for (int n : nums) {
            hp.push(n);
            if (hp.size() > k) {
                hp.pop();
            }
        }
        return hp.top();
    }
};