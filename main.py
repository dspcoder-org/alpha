from anthropic import Anthropic
import os
import re

class alpha:
    def __init__(self):
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
                            5. Update comments and docstrings to reflect the new algorithm, if necessary.
                            6. If the new algorithm requires additional helper functions or slight modifications to existing functions, implement them in a way that minimizes changes to the overall structure.
                            
                            
                            Remember, it's crucial to keep the structure and majority of the code as similar as possible to the original files. Only modify the parts directly related to implementing the new algorithm.

                            Please provide your generated code files in the following format:

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

                            Ensure that each file contains the complete code, including any necessary imports, class definitions, and functions from the original files, with only the algorithm-specific parts modified to implement the new algorithm.
                            """
        self.code_files_path = "./code/"
        
    def _read_code_files(self, folder, file_list):
        
        code_content = "<original_code>\n"

        for file_name in file_list:
            code_content += f"\n {file_name} \n"
            file_path = f"{self.code_files_path}/{folder}/{file_name}"
            try:
                with open(file_path, 'r') as file:
                    code_content += file.read()
            except FileNotFoundError:
                code_content += f"// Error: {file_name} not found.\n"

        code_content += "<original_code>"
        return code_content
    
    def split_and_write_code(self, string, save_path):
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
                file_path = f"{save_path}/src/main.c"
            elif filename == "main_dev.c":
                file_path = f"{save_path}/._dev/main_dev.c"
            elif filename == "lib.c":
                file_path = f"{save_path}/._dev/lib.c"
            elif filename == "util.h":
                file_path = f"{save_path}/inc/util.h"
            elif filename == "main.cpp":
                file_path = f"{save_path}/src/main.cpp"
            elif filename == "main_dev.cpp":
                file_path = f"{save_path}/._dev/main_dev.cpp"
            elif filename == "lib.cpp":
                file_path = f"{save_path}/._dev/lib.cpp"
            elif filename == "util.hpp":
                file_path = f"{save_path}/inc/util.hpp"
            elif filename == "README.md":
                file_path = f"{save_path}/README.md"
            elif filename == "Solution.md":
                file_path = f"{save_path}/Solution.md"
            elif filename == "test.py":
                file_path = f"{save_path}/._tests/test.py"
            # Write the content to the respective file
            with open(file_path, 'w') as file:
                file.write(formatted_content)
    
    def get_files_from_llm(self, ques_name, ques_description, language):
        # create a context
        context = self.start_context
        
        # Add question name and description
        context += f"Question: {ques_name}  \n"
        context += f"Description: {ques_description}  \n"
        
        if language == "C":
            context += "Here are the original code files:  \n "
            context += self._read_code_files("C", ["lib.c", "main.c", "main_dev.c", "util.h"])
        elif language == "Cpp":
            context += "Here are the original code files:  \n "
            context += self._read_code_files("Cpp", ["lib.cpp", "main.cpp", "main_dev.cpp", "util.hpp"])
    
        context += self.end_context
        
        # Send request to claude 
        
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
    
    def generate_question_files(self, ques_name, ques_description, language, question_folder_name, base_path):
        if language == "C":
            # get response from LLM model
            response = self.get_files_from_llm(ques_name, ques_description, language)

            self.split_and_write_code(response, f"{base_path}/{question_folder_name}/C")
        
        elif language == "Cpp":
            # get response from LLM model
            response = self.get_files_from_llm(ques_name, ques_description, language)

            self.split_and_write_code(response, f"{base_path}/{question_folder_name}/Cpp")
        
        elif language == "C/Cpp":
            # get response from LLM model
            response = self.get_files_from_llm(ques_name, ques_description, "C")

            self.split_and_write_code(response, f"{base_path}/{question_folder_name}/C")
            
            response = self.get_files_from_llm(ques_name, ques_description, "Cpp")

            self.split_and_write_code(response, f"{base_path}/{question_folder_name}/Cpp")
        
        # return self.get_files_from_llm(ques_name, ques_description, language)
    
    def create_folder_structure(self, question_folder_name, base_path):
        # Define the folder structure
        structure = {
            question_folder_name: {
                "._tests": {},
                "C": {
                    "._dev": {},
                    "inc": {},
                    "lib": {},
                    "src": {}
                },
                "Cpp": {
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

    def question(self, ques_name, ques_description, language, id, base_path):
        
        # Make folder structure
        question_folder_name = f"{id}_{ques_name.lower().replace(' ', '_')}"
        self.create_folder_structure(question_folder_name, base_path)
        
        # Generate question files and write them to the folder
        self.generate_question_files(ques_name, ques_description, language, question_folder_name, base_path)
        
        
if __name__ == "__main__":
    qh = alpha()
    ques_name = "Detect cycle in linked list"
    language = "C"
    id = "10102"
    base_path = "./"
    with open("ReadMe.md", "r") as file:
        ques_description = file.read()
    
    print(qh.question(ques_name, ques_description, language, id, base_path))
    