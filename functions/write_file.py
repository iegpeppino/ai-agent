import os

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