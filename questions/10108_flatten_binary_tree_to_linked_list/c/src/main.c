#include "util.h"

void flatten_binary_tree(struct TreeNode* root) {
    // Write your code here
}

int main(int argc, char* argv[]) {

    // Setup the binary tree
    struct TreeNode* root = setup_question(argc, argv);
    
    // User function to flatten the binary tree
    flatten_binary_tree(root); 

    // Print the flattened tree
    print_flattened_tree(root);
    
    return 0;
}