from llm import generate  
from build import build
from koro import Koro
import os

class Questions_handler():
    def __init__(self):
        self.questions = []
        self.ques_save_path = "./questions/"
        self.koro_output_path = "./koro_output/"
        self.build_files_path = "./context/build_files/"
        
    def run_koro_all(self):
        # check all questions folder in self.ques_save_path directory, use os.listdir
        # run koro on all questions
        for dir in os.listdir(self.ques_save_path):
            if os.path.isdir(f"{self.ques_save_path}{dir}"):
                # build first then run koro
                print(f"Running Koro on {dir}")
                build_files = build(f"{self.ques_save_path}{dir}", self.build_files_path)
                build_files.build()
                
                koro_c = Koro(f"{self.ques_save_path}{dir}", "c", self.koro_output_path)
                koro_cpp = Koro(f"{self.ques_save_path}{dir}", "cpp", self.koro_output_path)
                koro_c.run_tests()
                koro_cpp.run_tests()


class Question_handle:
    def __init__(self, ques_name, ques_description, id):
        
        self.base_question_path = "./context/base_question/"
        self.ques_save_path = "./questions/"
        self.build_files_path = "./context/build_files/"
        self.koro_output_path = "./koro_output/"
        self.vscode_files_path = "./context/vscode_files/"
        self.ques_prompts = "./descriptions/"
        
        self.ques_name = ques_name
        self.ques_description = ques_description
        self.id = id
        self.ques_folder_name = f"{self.id}_{self.ques_name.lower().replace(' ', '_')}"
        self.question_path = f"{self.ques_save_path}{self.ques_folder_name}"
        
        self.generate = generate(self.base_question_path, self.ques_prompts)
        self.build = build(self.question_path, self.build_files_path, self.vscode_files_path, self.base_question_path)
        
    def run_koro(self):
        print("============= Koro ============= ")
        self.koro_c = Koro(self.question_path, "c", self.koro_output_path)
        self.koro_cpp = Koro(self.question_path, "cpp", self.koro_output_path)
        self.koro_c.run_tests()
        self.koro_cpp.run_tests()
        print("============= Done ============= \n")
        
    def test_make(self):
        print("============= Make ============= ")
        self.build.test_make_c()
        print("-----------------------------")
        self.build.test_make_cpp()
        print("============= Done ============= \n")
    
    def run(self):
        # context = ""
        # context += "Input the number of elements for the both linked list in argument n"
        # self.generate.generate_prompt("Intersection of Two Linked Lists", context)
        
        # self.generate.generate_question(ques_name, ques_description, id, self.ques_save_path)
        
        # self.build.copy_vscode_files()
        
        # self.build.remove_build_files() # removes .sh and makefile from question folder
        
        # self.build.copy_build_files() 
        
        # self.build.clean() # removes both a.out and libdspcoder.a
        
        # self.build.build_c()
        # self.build.build_cpp()
        # self.build.build()
        
        self.run_koro()
        
        # self.test_make()
        
        pass
    

# Question details  
ques_name = "intersection_of_two_linked_lists"
id = "10109" 
ques_description = ""
with open(f"./descriptions/{ques_name.lower().replace(' ', '_')}.txt", "r") as file:
    ques_description = file.read()

ques_description += """
    take all inputs in setup_question function as verify function is only available in lib.c and cant be imported 
"""


if __name__ == "__main__":
    ques = Question_handle(ques_name, ques_description, id)
    ques.run()
    
    # questions = Questions_handler()
    # questions.run_koro_all()
