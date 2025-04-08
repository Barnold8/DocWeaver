from typing import List,Pattern
import os
import re

class File:

    x = 5

    def __init__(self,fileName,filePath):
        self.fileName = fileName
        self.filePath = filePath
        self.imports = [] # a list of strings that just say what imports are in a given file

        self.classes = None # this needs to be a dict that has the form 
                        # key: "whole class as string"
                            # or
                        # key: [class as string chunks]

        self.functions = None # this needs to be a dict that has the form 
                        # key: "whole function as string"
                            # or
                        # key: [function as string chunks]

def matchesPattern(text:str,patterns: List[str]) -> bool:

    if len(patterns) <= 0: # if theres no regex to match with, just allow all
        return True

    for pattern in patterns:
        if re.match(pattern,text):
            return True
    return False

def compilePatterns(patterns:List[str]) -> List[Pattern]: # not file specific so could be moved elsewhere
    return [re.compile(pattern) for pattern in patterns]

def needsChunked(filePath: str, byteSizeThreshold: int = 1064) -> bool :
    return os.path.getsize(filePath) > byteSizeThreshold

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

def writeCommentedFile(contents: dict, fileName: str = "example2") -> bool: 

    contentChunks = contents["candidates"][0]["content"]["parts"]

    try:
        with open(fileName,"w") as newFile:
            for chunk in contentChunks:
                textSplit = chunk["text"].split("<linebreak>")
                for line in textSplit:
                    newFile.writelines(line)
    except FileNotFoundError as err:
        print(f"FILE_ERROR: Problem writing {fileName}\n\n{err}")
        return False
    return True

def chunkByFunction():
    pass

def handleFiles(folderPath:str,patterns: List[str], API_KEY: str):
    # for loop over files and run either geminiRequestAll or geminiRequestChunked

    files = [file for file in getFiles(folderPath,patterns) if matchesPattern(file,patterns)]

    for file in files:
        print(file)

## the bin


# def fileChunking(filePaths: List[str],chunkWidth: int = 4096 ) -> List[str]:

#     # functions = None
#     # functionBuffer = ""
#     # writingFunction = False

#     for file in filePaths:
#          with open(file, "r",encoding="utf-8") as f: 
#             lines = f.readlines()
            
#             fileObject = File(
#                 filePath = file,
#                 fileName = file.split("\\")[1],
#             )
            
#             print(f"File:\n\n\tName: {fileObject.fileName}\n\tFilePath: {fileObject.filePath}\n")

#             l = []
#             for line in lines:
#                 l.append(line)

#             # for line in lines:
#             #     if not writingFunction and "def" in line:
#             #         writingFunction = True
#             #         functionBuffer += line
#             #     elif "def" in line:
#             #         print(functionBuffer)
#             #         exit()
#             #     else:
#             #         functionBuffer += line