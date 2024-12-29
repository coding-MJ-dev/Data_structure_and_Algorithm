// 21. Merge Two Sorted Lists

// Definition for singly-linked list.
#include <cstddef>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* ans = new ListNode();
        ListNode* cur = ans;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                cur->next = list1;
                cur = cur->next;
                list1 = list1->next;
            } else {
                cur->next = list2;
                cur = cur->next;
                list2 = list2->next;
            }
        }

        if (list1 != nullptr) {
            cur->next = list1;
        }
        if (list2 != nullptr) {
            cur->next = list2;
        }

        return ans->next;
    }
};


// class Solution {
// public:
//     ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
//         if (list1 == NULL && list2 == NULL) {
//             return NULL;
//         }
//         if (list1 == NULL) {
//             return list2;
//         }
//         if (list2 == NULL) {
//             return list1;
//         }

//         ListNode* dummy = new ListNode();
//         ListNode* curr = dummy;

//         while (list1 != NULL && list2 != NULL) {
//             if (list1->val <= list2->val) {
//                 curr->next = list1;
//                 list1 = list1->next;
//             }
//             else {
//                 curr->next = list2;
//                 list2 = list2->next;
//             }
//             curr = curr->next;
//         }
//         if (list1 != NULL) {
//             curr->next = list1;
//         } else {
//             curr->next = list2;
//         }
//         return dummy->next;
//     }
// };


