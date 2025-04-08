import argparse

class Args:

    def __init__(self,size: int,path: str, patterns: list[str],API_KEY_PATH:str):
        
        self.size = size
        self.path = path
        self.patterns = patterns
        self.API_KEY_PATH = API_KEY_PATH


    def debugPrint(self):

        print(
            f"""Args:
                size: {self.size}
                path: {self.path}
                patterns: {self.patterns}
                api_key: {self.API_KEY_PATH}
            """
            )

def argInit() -> argparse.Namespace:
    parser =  argparse.ArgumentParser()
    parser.add_argument("-s","--size", help="decides character limit on file for if it should be split into chunks or not [DEFAULT 1064].",type=int,default=1064)
    parser.add_argument("-p","--path", help="the file path to the code directory to add docstrings to [DEFAULT CURRENT DIRECTORY].",default="")
    parser.add_argument("-r","--regex",help="regex pattern to determine the files to add, this can also be included to only include specific directories too [DEFAULT ALLOWS ALL FILES AND PATHS]\n\nUsing -r <regexpattern> -r <regexpattern> will result in the current found filepath to be accepted if it matches to either pattern.",nargs='+',default=[])
    parser.add_argument("-a","--api",help="the path to the location of your API key [DEFAULT IS THE CURRENT PATH + API_KEY]",default="API_KEY")
    return parser.parse_args()

def handleArgs()-> Args:

    parser = argInit()

    return Args(
        parser.size,
        parser.path,
        parser.regex,
        parser.api
    )

     