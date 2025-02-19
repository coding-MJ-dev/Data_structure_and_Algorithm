// 1642. Furthest Building You Can Reach

#include <vector>
#include <queue>
using namespace std;

class Solution {
    public:
        int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
            priority_queue<int, vector<int>> maxHeap; // Min-heap to store ladder jumps
            int n = heights.size();
            
            for (int i = 0; i < n - 1; i++) {
                int diff = heights[i + 1] - heights[i];
                if (diff > 0) {
                    bricks -= diff;
                    maxHeap.push(diff);
                    if (bricks < 0) {
                        if (ladders > 0) {
                            bricks += maxHeap.top();
                            maxHeap.pop();
                            ladders -= 1;
                        }
                        else return i; // Stop if out of bricks
                    }
                }
            }
            return n - 1; // Reached the last building
        }
    };