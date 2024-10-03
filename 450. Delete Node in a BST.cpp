// 450. Delete Node in a BST


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) {
            return NULL;
        }
        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            if (!root->right && !root->left) {
                return NULL;
            } else if (!root->left) {
                return root->right;
            } else if (!root->right) {
                return root->left;
            } else {
                int newVal {};
                TreeNode* cur = root;
                cur = cur->right;
                while (cur->left) {
                    cur = cur->left;
                }
                newVal = cur->val;
                root->val = newVal;
                root->right = deleteNode(root->right, newVal);
                return root;
            }
        }
        return root;
    }
};

