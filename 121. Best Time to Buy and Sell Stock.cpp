// 121. Best Time to Buy and Sell Stock


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = INT_MIN;
        // int res = 0;
        int buy = -prices[0];

        for (int& p : prices) {
            profit = max(p+buy, profit);
            buy = max(buy, -p);
        }
        return profit;
