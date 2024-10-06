// 252. Meeting Rooms

class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        int maxEnd {-1};
        sort(intervals.begin(), intervals.end());
        for (auto& p : intervals) {
            int start = p[0];
            if (start < maxEnd) {
                return false;
            }
            maxEnd = p[1];
        }
        return true;
    }
};