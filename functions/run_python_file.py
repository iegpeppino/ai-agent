import os, subprocess, sys
from datetime import time

def run_python_file(working_directory, file_path):

    abs_workdir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))

    # Check if filepath is inside working_directory
    if os.path.commonpath([abs_workdir, abs_filepath]) != abs_workdir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Check if filepath exists
    if not os.path.exists(abs_filepath):
        return f'Error: File "{file_path}" not found.'
    
    # Check if it is a python file
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try :
        result = subprocess.run(
            args= [sys.executable, file_path],
            cwd=abs_workdir,
            capture_output=True,
            text= True,
            timeout= 30
            )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    stdout = result.stdout
    stderr = result.stderr

    if not stdout and not stderr:
        return "No output produced."
    
    response = f'Ran "{file_path}"\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}'
    if result.returncode != 0:
        response += f'\nProcess exited with code {result.returncode}'

    return response
    