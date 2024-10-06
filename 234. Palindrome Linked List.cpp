// 234. Palindrome Linked List

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> front, end;
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* cur = head;

        while (fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            slow = slow->next;
        }
        while (slow != NULL) {
            front.push_back(cur->val);
            end.push_back(slow->val);

            cur = cur->next;
            slow = slow->next;
        }
        reverse(end.begin(), end.end());
        return front == end;
    }
};