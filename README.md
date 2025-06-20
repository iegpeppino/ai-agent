[lang Es](https://github.com/iegpeppino/ai-agent/blob/main/README.es.md)

# AI AGENT
___


### Description 

AI agent is a CLI tool built using Google's Gemini API.
It accepts a coding task from a prompt and chooses from
a set of predefined functions to accomplish said task. 
The agent uses these functions until the task is complete
or a maximum number of tries (predefined constant) is reached.
___
___
### Functions

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
___
___
### Requirements

- You'll need python 3.10+ installed on your system.
- Access to an Unix-like shell.
- Create an account on [Google AI Studio](https://aistudio.google.com/) to generate an *API KEY*.


___
___

### Set-Up

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
___
___
### Usage

There's a calculator python app in the /calculator directory to be used for tests. For example, you can go into **/calculator/main.py** and modifiy the **precedence** value for the "**+**" operator and then use the agent to review and correct the code like this:

```bash
python3 main.py "fix the bug in calculator, it isn't yielding accurate results in the sum operation"
```

You may also import new code and use the agent to work with it.

You can add a "--verbose" argument after your prompt and the program will print additional information about the prompt and response tokens. This information is useful for keeping track of your Google API usage and for considering charges to your account.



---
---