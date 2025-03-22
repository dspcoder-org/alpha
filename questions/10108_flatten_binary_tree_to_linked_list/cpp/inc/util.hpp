#ifndef UTIL_H
#define UTIL_H

#include <iostream>
#include <vector>

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
};

// Function declarations

TreeNode* setup_question(int argc, char* argv[]);
void print_flattened_tree(TreeNode* root);

#endif // UTIL_H