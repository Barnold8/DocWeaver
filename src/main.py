from API_Request import *
import os

if __name__ == "__main__":
        
    PATH = file_path = os.path.realpath(__file__).split("main.py")[0]

    API_KEY = loadApiKey(PATH+"API_KEY")

    print(geminiRequest(API_KEY))