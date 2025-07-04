import os
from google.genai import types

def get_files_info(working_directory, directory= None):

    workdir = os.path.abspath(working_directory)
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    else:
        target_dir = workdir
    

    # Handle errors
    if not target_dir.startswith(workdir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []

        for entry in os.listdir(target_dir):
            fullpath = os.path.join(target_dir, entry)
            size = 0
            isdir = os.path.isdir(fullpath)
            size = os.path.getsize(fullpath)
            files_info.append(f'- {entry}: file_size={size} bytes, is_dir={isdir}')

        return "\n".join(files_info)
    
    except Exception as e:
        return f'Error listing files: {e}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)