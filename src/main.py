from API_Request import *
from file import *
import warnings


# The file path "API_KEY" has to be the path to your api key for gemini (relative to main.py for simplicity sakes)


# idea is chunk via a length in the code, maybe every n words, 
# and have it synopsise up until that point, 
# and when that section is parsed, generate a new synopsis talking about that class or function
# each chunk contains the current function being synopsised

# example 

#CHUNK 4: def writeline()
#Contents:
# code here


if __name__ == "__main__":

    warnings.filterwarnings("ignore", message="invalid escape sequence '\\.'", category=SyntaxWarning) # ignore annoying escape char with regex warning

    # PATH = file_path = os.path.realpath(__file__).split("main.py")[0]
    API_KEY = loadApiKey(relativePath("API_KEY"))

    with open(relativePath("example.c"),"r",encoding="utf-8") as file:
        request = geminiRequest(API_KEY,file.read())
        writeCommentedFile(request)
    
        

    # fileChunks = fileChunking(
    #     loadFilePaths(".",["^.*\.py$"]),
    #     100000
    # )





    


