#ifndef UTIL_H
#define UTIL_H

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

#endif // UTIL_H