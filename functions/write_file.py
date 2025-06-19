import os
from google.genai import types

def write_file(working_directory, file_path, content):

    # Get absolute paths
    abs_workdir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))
    directory = os.path.dirname(abs_filepath)

    # Check if file_path is inside working directory
    #if os.path.commonpath([workdir, target_file]) != workdir:
        # not inside
    if not abs_filepath.startswith(abs_workdir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # If path doesn't exist, create directories
    if not os.path.exists(abs_filepath):
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            return f'Error {e} creating directory: "{directory}"'
        
    # Check if file_path contains a file at the end
    if os.path.exists(abs_filepath) and os.path.isdir(abs_filepath):
        return f'Error: "{file_path}" is a directory and not a file'

    try:
        with open(abs_filepath, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e} could not write contents to "{file_path}"'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to specified file on file_path, constrained to the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be written on, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file."
            )
        },
    ),
)
