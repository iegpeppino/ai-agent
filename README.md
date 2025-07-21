[![Python](https://img.shields.io/badge/code-Python-green?logo=python)](README.md)
[![ES](https://img.shields.io/badge/lang-ES-red?logo=translate)](README.es.md)

# AI AGENT 🤖
___

An AI powered Python CLI tool to perform promp actions using predefined functions.

## Description 

AI agent is a CLI tool built using Google's Gemini API.
It accepts a coding task from a prompt and chooses from
a set of predefined functions to accomplish said task. 

## Why ?

We live in an age of uncertainty regarding the concept of AI. This tool helps to mitigate the general sentiment of fear towards it (that it will take all of our jobs) and helps to consolidate a thought incline torwards taking this resource as a tool that can help us in tedious daily tasks (in this case, related to software development).

## Functioning

The program uses the Google Gemini API to perform tasks prompted through the CLI. 

The AI agent is given a list of predefined functions to perform these tasks.
The agent uses these functions until the task is complete
or a maximum number of tries (predefined constant) is reached.

> Calls to the AI are already pre-configured for it to behave as a code review and correction helper. This configuration can be found in the _config.py_ file.

This python program comes with four basic functions:

- __get_file_content__:
    - Returns a list of the contents from a given directory.
    and their sizes.
    - The directory has to be inside the working directory.
    - If no directory argument is None, it is set to the working directory.

- __get_files_info__:
    - Returns the contents of a file from a given file path.
    - The file path has to be inside the working directory.
    - The returned content is truncated if it exceeds a maximum
    of characters set in a constant.

- __write_file__:
    - Writes contents passed as arguments to a given file path.
    - The file path has to be inside the working directory.
    - If the file doesn't exist, it is created.

- __run_python_file__:
    - Runs a ".py" file from a given file path.
    - The file path has to be inside the working directory.
    - It can return stdout or stderr from the ran file.


> Additional functions can be created for the program to use. They'll have to be located in the **/functions** directory, alongside the function,  a **types.FunctionDeclaration()** has to be defined and added to the list of available functions in **call_function.py** for the AI client to use. 


## Pre-requisites

- You'll need python 3.10+ installed on your system.
- Access to an Unix-like shell.
- Create an account on [Google AI Studio](https://aistudio.google.com/) to generate an *API KEY*.


## Set-Up

- In the root directory, create a .env file, then store the ApiKey from Gemini:
```bash
GEMINI_API_KEY="your_api_key_here"
```

- Create and start a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

- Install the contents from requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

There's a calculator python app in the /calculator directory to be used for tests. For example, you can go into **/calculator/main.py** and modifiy the **precedence** value for the "**+**" operator and then use the agent to review and correct the code like this:

```bash
python3 main.py "fix the bug in calculator, it isn't yielding accurate results in the sum operation"
```

You may also import new code and use the agent to work with it.

You can add a "--verbose" argument after your prompt and the program will print additional information about the prompt and response tokens. This information is useful for keeping track of your Google API usage and for considering charges to your account.


## 🤝 Contributing

Feel free to fork the repository and open a pull request to the `main` branch.