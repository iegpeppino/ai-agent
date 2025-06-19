import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):

    workdir = os.path.abspath(working_directory)
    file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Handle errors
    if not file_path.startswith(workdir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_path, "r") as file:
            
            file_content_string = file.read(MAX_CHARS)

            if len(file.read()) > MAX_CHARS:
                return file_content_string.append(f'\n...File {file_path} truncated at 10000 characters')
            else:
                return file_content_string
                
    except Exception as e:
            return f'Error reading {file_path}'
    finally:
         file.close()

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the file contents from the specified filepath up to 10000 characters, constrained to their working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be read from, relative to the working directory.",
            ),
        },
    ),
)