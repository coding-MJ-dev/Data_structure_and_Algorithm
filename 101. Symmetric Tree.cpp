// 101. Symmetric Tree

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
private:
    bool mirror(TreeNode* l, TreeNode* r) {
        if (!l && !r) {
            return true;
        }
        if (l == NULL || r == NULL) {
            return false;
        }
        if (l->val != r->val) {
            return false;
        }
        return mirror(l->right, r->left) && mirror(l->left, r->right);
    }

public:
    bool isSymmetric(TreeNode* root) {
        if (root==NULL) {return true;}
        return mirror(root->left, root->right);        
    }
};