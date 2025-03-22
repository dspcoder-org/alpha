#include "util.hpp"
#include <vector>
#include <iostream>

void flatten_binary_tree(TreeNode* root) {
    // Write your code here
}

int main(int argc, char* argv[]) {
    
    // Setup the binary tree
    TreeNode* root = setup_question(argc, argv);

    // Call the user function to flatten the binary tree
    flatten_binary_tree(root);

    // Print the flattened tree
    print_flattened_tree(root);

    return 0;
}