// 572. Subtree of Another Tree


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
    bool same(TreeNode* l, TreeNode* r) {
        if (!l && !r) { return true; }
        if (!l || !r) { return false; }
        if (l->val != r->val) { return false; }
        return same(l->left, r->left) && same(l->right, r->right);
    }
    bool res {false};
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!subRoot) {return true;}
        if (!root) {return false;}
        if (root->val != subRoot->val) {
            res = (isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot));
        }
        else {
            return res = (isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot) ||same(root, subRoot));
        }
        
        return res;

        
    }
};