import sys
import shutil
import os
import subprocess


question_path = sys.argv[1]
lang = sys.argv[2]
work = sys.argv[3] if len(sys.argv) > 3 else "build"


class QuestionHandler:
    def __init__(self):
        self.build_folder_path = f"./build/"
        self.question_path = sys.argv[1]
        
        self.build_target_dir = f"{question_path}/{lang}/._dev/"  
        self.makefile_target_dir = f"{question_path}/{lang}/"
    
    def run(self):
        pass
    
    def test(self):
        pass
    
    def clean(self):
        pass
    
    def build(self):
        pass
    
    def generate(self):
        pass
    
    def make(self):
        pass
    
    
if __name__ == "__main__":
    
    obj = QuestionHandler()
    question_name = "Bubble Sort"
    additional_gpt_prompt = ""
    llm_model = "gpt" # gpt/claude
    obj.run(question_name, lang, additional_gpt_prompt)

