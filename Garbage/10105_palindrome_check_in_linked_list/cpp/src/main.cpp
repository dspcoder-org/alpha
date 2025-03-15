#include "../inc/util.hpp"
#include <vector>
#include <iostream>

bool isPalindrome(LinkedList* head) {
    // Write your code here
}

int main() {
    
    // Setup the linked list
    LinkedList* head = setup_question();

    // Call the user function to check if the linked list is a palindrome
    bool result = isPalindrome(head);

    // Print the result
    std::cout << (result ? "true" : "false") << std::endl;

    return 0;
}