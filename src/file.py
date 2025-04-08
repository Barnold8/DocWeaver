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

def fileChunking(filePaths: List[str],chunkWidth: int = 4096 ) -> str:

    chunks = []
    globalChunk = ""
    chunkSize = 0
    formatString = ""
    formatHeaderLength = 9

    for file in filePaths:
        with open(file, "r",encoding="utf-8") as f: 

            fileName = file.split("\\")
            fileName = fileName[len(fileName)-1]
            
            formatString = "="*formatHeaderLength + f"\n\nFILE: {fileName}\nPATH:{file}\ncontents:\n"
            
            if len(globalChunk) - len(formatString) > chunkWidth:
                chunkSize = len(formatString)
                chunks.append(globalChunk)
                globalChunk += formatString
                globalChunk = "" 
            else:
                
                chunkSize += len(formatString)
                globalChunk += formatString


            lines = f.readlines()

            for line in lines:
                if len(globalChunk) - len(line)  > chunkWidth:
                    chunkSize = len(line)
                    chunks.append(globalChunk)
                    globalChunk += line
                    globalChunk = "" 
                else:
                    chunkSize += len(line)
                    globalChunk += line

    if len(globalChunk) > 0: 
        chunks.append(globalChunk)
        chunks.append("="*formatHeaderLength+"\n\nEND OF THE FILE CHUNKS")

    for chunk in chunks:
        print("$"*formatHeaderLength+f"\n\nCHUNK:\n{chunk}")

    return chunks

