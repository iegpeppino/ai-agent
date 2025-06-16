import os

def write_file(working_directory, file_path, content):

    # Get absolute paths
    workdir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    directory = os.path.dirname(target_file)

    # Check if file_path is inside working directory
    #if os.path.commonpath([workdir, target_file]) != workdir:
        # not inside
    if not target_file.startswith(workdir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # If path doesn't exist, create directories
    if not os.path.exists(target_file):
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            return f'Error {e} creating directory: "{directory}"'
        
    # Check if file_path contains a file at the end
    if os.path.exists(target_file) and os.path.isdir(target_file):
        return f'Error: "{file_path}" is a directory and not a file'

    try:
        with open(target_file, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e} could not write contents to "{file_path}"'