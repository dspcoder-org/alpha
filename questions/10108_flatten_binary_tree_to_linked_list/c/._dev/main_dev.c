#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

// Function prototypes
extern struct TreeNode* setup_question(int argc, char* argv[]);
extern void print_flattened_tree(struct TreeNode* root);

void flatten_binary_tree(struct TreeNode* root) {
    if (!root) return;

    struct TreeNode* stack[10000]; // Assuming input size is within 10^4
    int top = -1;

    stack[++top] = root;
    struct TreeNode* prev = NULL;

    while (top >= 0) {
        struct TreeNode* current = stack[top--];

        if (prev) {
            prev->right = current;
            prev->left = NULL; // Nullify the left child
        }

        if (current->right) stack[++top] = current->right;
        if (current->left) stack[++top] = current->left;

        prev = current;
    }
}

int main(int argc, char* argv[]) {
    struct TreeNode* root = setup_question(argc, argv);
    flatten_binary_tree(root);
    print_flattened_tree(root);
    return 0;
}
