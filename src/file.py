from typing import List,Pattern
import os
import re


def compilePatterns(patterns:List[str]) -> List[Pattern]: # not file specific so could be moved elsewhere
    return [re.compile(pattern) for pattern in patterns]

def getFiles(root,patterns: List[Pattern])-> List[str]:

    found_files = []
    if len(patterns) > 0:
        for root, subdirs, files in os.walk(root):
            for filename in files:                
                file_path = os.path.join(root, filename)
                for pattern in patterns:
                    if re.search(pattern, file_path):
                        found_files.append(file_path) 
    else:
        for root, subdirs, files in os.walk(root):
            for filename in files:                
                file_path = os.path.join(root, filename)   
                found_files.append(file_path) 
                  
    return found_files

def relativePath(path: str) -> str:
    ignoreList = ["","."]
    # I had this a simple one liner but nows its funny to make it even less readable while its still working
    return "\\".join(os.path.realpath(__file__).split("\\")[:-1]) if path in ignoreList else "\\".join(os.path.realpath(__file__).split("\\")[:-1])+"\\"+path 

def loadApiKey(path: str):
    
    key = None

    try:
        with open(path,"r") as file:
            key = file.readline()
    except FileNotFoundError as err:
        print(f"FILE_ERROR: {err}")
        exit(1)

    return key


def loadFilePaths(root: str, patterns: List[str] = []) -> List[str]:
    return getFiles(relativePath(root),compilePatterns(patterns))
