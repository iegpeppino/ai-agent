import os

def get_file_content(working_directory, file_path):

    MAX_CHARS = 10000

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