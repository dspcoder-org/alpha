from anthropic import Anthropic
from openai import OpenAI
import os
import re

class generate:
    def __init__(self, base_question_path, description_path):
        self.claude_api_key = "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" #os.environ.get('API_KEY')
        self.anthropic = Anthropic(api_key=self.claude_api_key )
        self.gpt_api_key = "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"
        self.deepseek_api_key = "sk-4d694e3879854ee58a63e54ee3ec8d27"
        self.model_to_use = "gpt"
        self.gpt = OpenAI(api_key = self.gpt_api_key)
        self.deepseek = OpenAI(api_key=self.deepseek_api_key, base_url="https://api.deepseek.com")
        self.code_files_path = base_question_path
        self.description_path = description_path
        self.system_context = """
            Your task is to modify the provided code files to implement a new algorithm while maintaining the existing structure. The original files were written for a reverse_linked_list algorithm.

            ## File Overview and Purpose
            1. **util.h/hpp**: Contains declarations of structures and functions that will be hidden from users in the .a file.
            2. **lib.c/cpp**: Contains utility code and implementation details that should be hidden from users. This file:
            - Includes the setup_question. You need to update setup_question according to inputs and outputs of the new algorithm.
            -- setup_question is a function is used for parsing input and setting up the question for the user.
            -- it takes arc, argv can take additional inputs if question requires.
            - Contains utility functions
            - Incorporates the content of util.h (needed to compile as a standalone .a file)
            - Should not include a alogiritm implementation or function signature.
            3. **main.c/cpp**: The file users will see and can edit on the platform. This file should:
            - Include a function signature where users will write their solution
            - Leave the implementation of this function empty for users to complete
            4. **main_dev.c/cpp**: Similar to main.c but includes the correct solution for the problem. This file:
            - Will be used to generate a binary for comparison testing
            - Should directly incorporate util.h content rather than importing it
            - Must contain the correct solution implementation
            5. **test.py**: 
            - This contains test cases used for testing user code. 
            - generate 10 test cases covering edge cases, constraints, time and space complexity. 
            - self.RUN will always be 3.
            - Keep first 3 test cases length small and testing simple conditions.
            6. **readme.md**: 
            - Contains the problem description, input format, examples, and constraints only. 
            - Keep similar structure as original file
            7. **solution.md**: write following text in this file -> # Solutions will be added soon.
            8. **launch.json**: Configuration for launching/debugging. you only need to update args in the configurations which is argument used to run a.out executable. use argument from first test case

            ## Important Notes
            - Do not change the overall structure of these files as they are used in the backend.
            - Users can only see and edit: main.c, lib.a (created using lib.c), and util.h.
            - util.h is needed in lib.c or main_dev.c, copy its content directly rather than importing it.
            - Make all necessary modifications to implement the new algorithm while preserving the existing file structure and relationships.

            ## Output Format Requirements
            CRITICAL: Do NOT use markdown code blocks (```c or ``` or any similar syntax) in your response. 
            Present each file's code directly between the specified tags without any additional formatting.

            Please generate complete code for all required files implementing the new algorithm. Each file should be formatted exactly as follows:

            <lib.c>
            // Raw code here without any markdown formatting
            </lib.c>

            <main.c>
            // Raw code here without any markdown formatting  
            </main.c>

            <main_dev.c>
            // Raw code here without any markdown formatting
            </main_dev.c>

            <util.h>
            // Raw code here without any markdown formatting
            </util.h>

            <lib.cpp>
            // Raw code here without any markdown formatting
            </lib.cpp>
            
            <main.cpp>
            // Raw code here without any markdown formatting
            </main.cpp>
            
            <main_dev.cpp>
            // Raw code here without any markdown formatting
            </main_dev.cpp>
            
            <util.hpp>
            // Raw code here without any markdown formatting
            </util.hpp>

            <readme.md>
            // Raw content here without any markdown formatting
            </readme.md>

            <solution.md>
            // Raw content here without any markdown formatting
            # Solutions will be added soon.
            </solution.md>

            <test.py>
            // Raw code here without any markdown formatting
            </test.py>

            <launch.json>
            // Raw content here without any markdown formatting
            </launch.json>

            Ensure all code maintains consistent naming conventions, style, and structure with the original files, modifying only what's necessary to implement the new algorithm.
            """
        
    def create_folder_structure(self, question_folder_name, ques_save_path):
        # Define the folder structure
        structure = {
            question_folder_name: {
                "._tests": {},
                "c": {
                    "._dev": {},
                    "inc": {},
                    "lib": {},
                    "src": {}, 
                    ".vscode": {}
                },
                "cpp": {
                    "._dev": {},
                    "inc": {},
                    "lib": {},
                    "src": {},
                    ".vscode": {}
                },
            }
        }

        # Recursive function to create folders
        def create_folders(ques_save_path, substructure):
            for folder_name, subsubstructure in substructure.items():
                current_path = os.path.join(ques_save_path, folder_name)
                os.makedirs(current_path, exist_ok=True)
                if isinstance(subsubstructure, dict):
                    create_folders(current_path, subsubstructure)

        # Start the folder creation
        create_folders(ques_save_path, structure)
    
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
                except:
                    raise FileNotFoundError(f"Error: {file_name} not found.")

        # copy readme.md, solution.md and test.py
        
        code_content += f"\n readme.md \n"
        file_path = f"{self.code_files_path}/readme.md"
        try:
            with open(file_path, 'r') as file:
                code_content += file.read()
        except:
            raise FileNotFoundError(f"Error: {file_name} not found.")
            
        code_content += f"\n solution.md \n"
        file_path = f"{self.code_files_path}/solution.md"
        try:
            with open(file_path, 'r') as file:
                code_content += file.read()
        except:
            raise FileNotFoundError(f"Error: {file_name} not found.")
        
        code_content += f"\n test.py \n"
        file_path = f"{self.code_files_path}/._tests/test.py"
        try:
            with open(file_path, 'r') as file:
                code_content += file.read()
        except:
            raise FileNotFoundError(f"Error: {file_name} not found.")
        
        code_content += f"\n launch.json \n"
        file_path = f"{self.code_files_path}/vscode/launch.json"
        try:
            with open(file_path, 'r') as file:
                code_content += file.read()
        except:
            raise FileNotFoundError(f"Error: {file_name} not found.")
        
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
            file_path = None
            file_path_cpp = None
            
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
            elif filename == "launch.json":
                file_path = f"{save_path}/c/.vscode/launch.json"
                file_path_cpp = f"{save_path}/cpp/.vscode/launch.json"
            
            # Write the content to the respective file
            with open(file_path, 'w') as file:
                file.write(formatted_content)
                
            if file_path_cpp:
                with open(file_path_cpp, 'w') as file:
                    file.write(formatted_content)
    
    def get_response_from_llm(self, ques_name, ques_description):
        # Get response from llm
        # create a context
        self.system_context += self._read_code_files(["c", "cpp"], [["lib.c", "main.c", "main_dev.c", "util.h"], ["lib.cpp", "main.cpp", "main_dev.cpp", "util.hpp"] ])
        # Add question name and description
        ques_context = f"Question: {ques_name}  \n"
        ques_context += f"Description: {ques_description}  \n"
            
        
        out = ""
        if self.model_to_use == "claude":
            # Make the API call
            response = self.anthropic.messages.create(
                model="claude-3-opus-20240229",  # Latest model
                max_tokens=4096,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_context
                    },
                    {
                        "role": "user",
                        "content": ques_context
                    }
                ], 
                temperature = 0
            )
            out = response.content[0].text
            
        elif self.model_to_use == "gpt":
            response = self.gpt.chat.completions.create(
                model = "gpt-4o",
                max_tokens = 4096*2,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_context
                    },
                    {
                        "role": "user",
                        "content": ques_context
                    }
                ],
                temperature = 0
            )
            out = response.choices[0].message.content
            
        elif self.model_to_use == "deepseek":
            response = self.deepseek.chat.completions.create(
                model="deepseek-reasoner",
                max_tokens=8192,
                messages=[
                    {"role": "system", "content": self.system_context},
                    {"role": "user", "content": self.user_context}
                ],
                temperature=0,
            )
            out = response.choices[0].message.content
            
        return out
    
    def generate_question_files(self, ques_name, ques_description, question_folder_name, ques_save_path):
        
        # Get response from llm
        response = self.get_response_from_llm(ques_name, ques_description)
        # Write response to text file in current directory
        with open(f"./response.txt", "w") as file:
            file.write(response)
        # parse the response and write the code to respective files
        self.split_and_write_code(response, f"{ques_save_path}/{question_folder_name}")
        
    def generate_question(self, ques_name, ques_description, id, ques_save_path):
        
        print("============= Generating ============= ")
        # Make folder structure
        question_folder_name = f"{id}_{ques_name.lower().replace(' ', '_')}"
        self.create_folder_structure(question_folder_name, ques_save_path)
        
        # Generate question files and write them to the folder
        self.generate_question_files(ques_name, ques_description, question_folder_name, ques_save_path)
        
        print("============= Done ============= \n")
        
    def generate_prompt(self, new_question_name, context):
        
        print("============= Generating Prompt ============= ")
        # read the description file
        with open(f"{self.description_path}reverse_linked_list.txt", "r") as file:
            ques_description = file.read()
        
        new_question_prompt = "write description similar to this for following question \n" + new_question_name + "\n" + context
        out = ""
        if self.model_to_use == "claude":
            # Make the API call
            response = self.anthropic.messages.create(
                model="claude-3-opus-20240229",  # Latest model
                max_tokens=4096,
                messages=[
                    {
                        "role": "system",
                        "content": ques_description
                    },
                    {
                        "role": "user",
                        "content": new_question_prompt
                    }
                ], 
                temperature = 0.0
            )
            out = response.content[0].text
            
        elif self.model_to_use == "gpt":
            response = self.gpt.chat.completions.create(
                model = "gpt-4o",
                max_tokens = 4096*2,
                messages=[
                    {
                        "role": "system",
                        "content": ques_description
                    },
                    {
                        "role": "user",
                        "content": new_question_prompt
                    }
                ],
                temperature = 0.0
            )
            out = response.choices[0].message.content
            
        elif self.model_to_use == "deepseek":
            response = self.deepseek.chat.completions.create(
                model="deepseek-reasoner",
                max_tokens=8192,
                messages=[
                    {"role": "system", "content": ques_description},
                    {"role": "user", "content": new_question_prompt}
                ],
                temperature=0.0,
            )
            out = response.choices[0].message.content
            
        file_name = new_question_name.lower().replace(' ', '_')
        with open(f"{self.description_path}{file_name}.txt", "w") as file:
            file.write(out)
        print(f"{file_name}")
        print("============= Done ============= \n")
        
if __name__ == "__main__":
    base_question_path = "./base_question/"
    question_handle = generate(base_question_path)
    
    ques_name = "Detect cycle in linked list"
    id = "10102"
    ques_save_path = "./questions/"
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
    
    question_handle.generate_question(ques_name, ques_description, id, ques_save_path)
    