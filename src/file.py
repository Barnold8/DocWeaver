def loadApiKey(path: str):
    
    key = None

    try:
        with open(path,"r") as file:
            key = file.readline()
    except FileNotFoundError as err:
        print(f"FILE_ERROR: {err}")
        exit(1)

    return key
