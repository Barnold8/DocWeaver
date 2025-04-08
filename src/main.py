from API_Request import *
from file import *
import warnings


# The file path "API_KEY" has to be the path to your api key for gemini (relative to main.py for simplicity sakes)

if __name__ == "__main__":

    warnings.filterwarnings("ignore", message="invalid escape sequence '\\.'", category=SyntaxWarning) # ignore annoying escape char with regex warning

    # PATH = file_path = os.path.realpath(__file__).split("main.py")[0]

    # API_KEY = loadApiKey(PATH+"API_KEY")

    # print(geminiRequest(API_KEY))

    fileChunks = fileChunking(
        loadFilePaths(".",["^.*\.py$"]),
        100000
    )



    


