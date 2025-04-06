#include "util.hpp"
#include <vector>
#include <iostream>

bool is_palindrome(LinkedList* head) {
    // Write your code here
}

int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to check if the linked list is a palindrome
    bool result = is_palindrome(head);

    // Print the result
    std::cout << (result ? "true" : "false") << std::endl;

    return 0;
}