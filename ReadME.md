# Description

***TODO***  *_this_*

# Get project

1. git clone https://github.com/Barnold8/DocWeaver.git
2. cd DocWeaver
3. python -m venv venv
4. pip install -r /path/to/requirements.txt


# Use project

## Options:

* `-h, --help`: Show this help message and exit.
* `-s SIZE, --size SIZE`: Decides the character limit on a file. If a file exceeds this limit, it will be split into chunks. [DEFAULT: 1064]
* `-p PATH, --path PATH`: The file path to the code directory to add docstrings to. [DEFAULT: CURRENT DIRECTORY]
* `-r REGEX, --regex REGEX`:
    * A regex pattern to determine which files to process.
    * Can also be used to include specific directories.
    * [DEFAULT: ALLOWS ALL FILES AND PATHS]
    * Using `-r <regexpattern> -r <regexpattern>` will result in the current found filepath being accepted if it matches either pattern.
* `-a API, --api API`: The path to the location of your API key. [DEFAULT: CURRENT PATH + API_KEY]