from anthropic import Anthropic
import os
import re

class alpha:
    def __init__(self, base_question_path):
        self.api_key = "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" #os.environ.get('API_KEY')
        self.anthropic = Anthropic(api_key=self.api_key )
        self.start_context = """ 
                            You are tasked with modifying a set of code files for a reverse linked list data structure and algorithm (DSA) 
                            question. Your goal is to generate new code files for a different algorithm while maintaining the majority of the 
                            code and structure from the original files.
                            
                            """
        self.end_context =  """
                            Your task is to generate four new code files based on the original files, but implementing the new algorithm. Follow these guidelines:

                            1. Maintain the same overall structure as the original files.
                            2. Keep the majority of the code the same, including imports, class definitions, and helper functions.
                            3. Modify only the algorithm-specific code to implement the new algorithm.
                            4. Ensure that variable names, function names, and coding style remain consistent with the original files.
                            5. Update comments  to reflect the new algorithm, if necessary.
                            6. If the new algorithm requires additional helper functions or slight modifications to existing functions, implement them in a way that minimizes changes to the overall structure.
                            7. readme.md : try to keep similar structure here problem description, basic examples, constraints
                            8. solution.md : keep this file empty 
                            9. test.py : I want you make testing more aggresive. Make 20 test cases testing every edge case atleast with 3 times. if needed add more test cases. self.RUN will always be 3
                            
                            Remember, it's crucial to keep the structure and majority of the code as similar as possible to the original files. Only modify the parts directly related to implementing the new algorithm.

                            Please provide your generated code files in the following format:
                            
                            for C language

                            <lib.c>
                            [Generated code for lib.c]
                            </lib.c>

                            <main.c>
                            [Generated code for main.c]
                            </main.c>

                            <main_dev.c>
                            [Generated code for main_dev.c]
                            </main_dev.c>

                            <util.h>
                            [Generated code for util.h]
                            </util.h>
                            
                            for Cpp language
                            
                            <lib.cpp>
                            [Generated code for lib.c]
                            </lib.cpp>

                            <main.cpp >
                            [Generated code for main.c]
                            </main.cpp>

                            <main_dev.cpp>
                            [Generated code for main_dev.c]
                            </main_dev.cpp>

                            <util.hpp>
                            [Generated code for util.h]
                            </util.hpp>
                            
                            Common files 
                            
                            <readme.md>
                            [Generated code for util.h]
                            </readme.md>
                            
                            <solution.md>
                            [Generated code for util.h]
                            </solution.md>
                            
                            Test file
                            
                            <test.py>
                            [Generated code for util.h]
                            </test.py>

                            Ensure that each file contains the complete code, including any necessary imports, class definitions, and functions from the original files, with only the algorithm-specific parts modified to implement the new algorithm.
                            """
        self.code_files_path = base_question_path
        
    def create_folder_structure(self, question_folder_name, base_path):
        # Define the folder structure
        structure = {
            question_folder_name: {
                "._tests": {},
                "c": {
                    "._dev": {},
                    "inc": {},
                    "lib": {},
                    "src": {}
                },
                "cpp": {
                    "._dev": {},
                    "inc": {},
                    "lib": {},
                    "src": {},
                },
            }
        }

        # Recursive function to create folders
        def create_folders(base_path, substructure):
            for folder_name, subsubstructure in substructure.items():
                current_path = os.path.join(base_path, folder_name)
                os.makedirs(current_path, exist_ok=True)
                if isinstance(subsubstructure, dict):
                    create_folders(current_path, subsubstructure)

        # Start the folder creation
        create_folders(base_path, structure)
    
    def _read_code_files(self, languages , file_list):
        
        code_content = "<original_code>\n"
        
        # copy all code files to context
        for i, lang in enumerate(languages):
            for file_name in file_list[i]:
                code_content += f"\n {file_name} \n"
                file_path = f"{self.code_files_path}/{lang}/{file_name}"
                try:
                    with open(file_path, 'r') as file:
                        code_content += file.read()
                except FileNotFoundError:
                    code_content += f"// Error: {file_name} not found.\n"

        # copy readme.md, solution.md and test.py
        
        code_content += f"\n readme.md \n"
        file_path = f"{self.code_files_path}/readme.md"
        try:
            with open(file_path, 'r') as file:
                code_content += file.read()
        except FileNotFoundError:
            code_content += f"// Error: {file_name} not found.\n"
            
        code_content += f"\n solution.md \n"
        file_path = f"{self.code_files_path}/solution.md"
        try:
            with open(file_path, 'r') as file:
                code_content += file.read()
        except FileNotFoundError:
            code_content += f"// Error: {file_name} not found.\n"
        
        code_content += f"\n test.py \n"
        file_path = f"{self.code_files_path}/._tests/test.py"
        try:
            with open(file_path, 'r') as file:
                code_content += file.read()
        except FileNotFoundError:
            code_content += f"// Error: {file_name} not found.\n"
        
        code_content += "<original_code>"
        return code_content
    
    def split_and_write_code(self, string, save_path):
        # parse the string and write the code to respective files
        
        # Regular expression to match file sections like <filename.ext>...</filename.ext>
        file_pattern = r"<(.+?)>(.*?)</\1>"
        
        matches = re.findall(file_pattern, string, re.DOTALL)
        if not matches:
            print("No valid file sections found in the string.")
            return
        
        for filename, content in matches:
            # Strip leading/trailing whitespace from the content
            formatted_content = content.strip()
            
            if filename == "main.c":
                file_path = f"{save_path}/c/src/main.c"
            elif filename == "main_dev.c":
                file_path = f"{save_path}/c/._dev/main_dev.c"
            elif filename == "lib.c":
                file_path = f"{save_path}/c/._dev/lib.c"
            elif filename == "util.h":
                file_path = f"{save_path}/c/inc/util.h"
            elif filename == "main.cpp":
                file_path = f"{save_path}/cpp/src/main.cpp"
            elif filename == "main_dev.cpp":
                file_path = f"{save_path}/cpp/._dev/main_dev.cpp"
            elif filename == "lib.cpp":
                file_path = f"{save_path}/cpp/._dev/lib.cpp"
            elif filename == "util.hpp":
                file_path = f"{save_path}/cpp/inc/util.hpp"
            elif filename == "readme.md":
                file_path = f"{save_path}/readme.md"
            elif filename == "solution.md":
                file_path = f"{save_path}/solution.md"
            elif filename == "test.py":
                file_path = f"{save_path}/._tests/test.py"
            # Write the content to the respective file
            with open(file_path, 'w') as file:
                file.write(formatted_content)
    
    def get_response_from_llm(self, ques_name, ques_description):
        # Get response from llm
        # create a context
        context = self.start_context
        
        # Add question name and description
        context += f"Question: {ques_name}  \n"
        context += f"Description: {ques_description}  \n"
            
        context += self._read_code_files(["c", "cpp"], [["lib.c", "main.c", "main_dev.c", "util.h"], ["lib.cpp", "main.cpp", "main_dev.cpp", "util.hpp"] ])
        context += self.end_context
        
        # Make the API call
        response = self.anthropic.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": context
                }
            ]
        )
        return response.content[0].text
    
    def generate_question_files(self, ques_name, ques_description, question_folder_name, base_path):
        
        # Get response from llm
        response = self.get_response_from_llm(ques_name, ques_description)
        # Write response to text file in current directory
        with open(f"./response.txt", "w") as file:
            file.write(response)
        # parse the response and write the code to respective files
        self.split_and_write_code(response, f"{base_path}/{question_folder_name}")
        
    def generate_question(self, ques_name, ques_description, id, base_path):
        
        # Make folder structure
        question_folder_name = f"{id}_{ques_name.lower().replace(' ', '_')}"
        self.create_folder_structure(question_folder_name, base_path)
        
        # Generate question files and write them to the folder
        self.generate_question_files(ques_name, ques_description, question_folder_name, base_path)
        
        
if __name__ == "__main__":
    base_question_path = "./base_question/"
    question_handle = alpha(base_question_path)
    
    ques_name = "Detect cycle in linked list"
    id = "10102"
    base_path = "./questions/"
    ques_description =  """
                        Problem Description
                            Given the head of a singly linked list, write a function to detect if the linked list contains a cycle. 
                            If a cycle is present, return true; otherwise, return false.

                        Input format: 
                            The input consists of two lines. The first line contains two space-separated integers n and pos, where n 
                            is the number of nodes in the linked list and pos is the index (0-indexed) of the node where the tail connects 
                            to. The second line contains n space-separated integers, the values of the nodes in the linked list.

                        Examples
                            Example 1:
                            Input: 
                                4 1
                                1 2 3 4
                            Output: true
                            Explanation: The linked list has a cycle because the last node (4) points back to the node at index 1 (value 2).
                            
                            Example 2:
                            Input: head = 
                                5 0
                                3 -3 4 0 2
                            Output: true
                            Explanation: The last node (value 2) links back to the head node, forming a cycle.
                            
                            Example 3:
                            Input: 
                                3 -1
                                2 0 1
                            Output: false
                            Explanation: The linked list does not have a cycle, as there is no node linking back to a previous node.
                        
                        Constraints
                            The number of nodes in the list is in the range [0, 10⁴].
                            -10⁵ ≤ Node.val ≤ 10⁵
                        """
    
    question_handle.generate_question(ques_name, ques_description, id, base_path)
    