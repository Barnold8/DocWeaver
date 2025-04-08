from API_Request import *
from file import *
from argHandler import *
import warnings
import sys


# The file path "API_KEY" has to be the path to your api key for gemini (relative to main.py for simplicity sakes)

# idea is chunk via a length in the code, maybe every n words, 
# and have it synopsise up until that point, 
# and when that section is parsed, generate a new synopsis talking about that class or function
# each chunk contains the current function being synopsised
# may have to define bindings for programming language since each lang defines functions differently, [func,def,function,...] etc

# example 

#CHUNK 4: def writeline() | language python | args [] | imports [] | return type None
#Current synopsis of function: <gemini current synopsis>

#Contents:
# code here
# when you get to the end of a function (usually because youve found the EOF or another function declaration) prompt gemini with the synopsis of the function and tell it to write a docstring for it
# somehow add that docstring in

if __name__ == "__main__":

    warnings.filterwarnings("ignore", message="invalid escape sequence '\\.'", category=SyntaxWarning) # ignore annoying escape char with regex warning

    args = handleArgs()

    handleFiles(
        args.path,
        args.patterns,
        loadApiKey(args.API_KEY_PATH),
        args.size
    )
