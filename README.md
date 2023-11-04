# Python Starter Project with Dependency Mgmt, Multiple config file support and Tests

It can be used for a regular python app or a lambda

# How to run/debug

Either run main.py as `python3 main.py` or run main method from IDE

Or run `runner.py` from IDE

Or run `pytest` from root folder to run all tests

NOTE: To Run/Debug the `.py` scripts within IntelliJ, make sure to change working directory to root of the project instead of sub-folder eg: `src/` or `test/` so that intellij will see all the files in relative position from root dir.
IntelliJ might pick the `src/` or `test/` as working directory, which will not work.

# Install dependencies
     $ pip3 install --target ./dist -r requirements.txt
    
    Let IntelliJ install dependencies on its own if you want to run the script using IntelliJ.

# Build Script: (run tests, create zip with dependencies)
     $ chmod + x build.sh
     $ ./build.sh

# Features

- dependency mgmt (requirements.txt)
- Multiple config file(profile) support based on an environment variable
- build script
- sample test with `pytest`
- lambda example (or a regular app)


# Requirements
- [Python 3.7+](https://www.python.org/downloads/) 


 

 # python-starter-project-with-dependency-mgmt-and-tests
