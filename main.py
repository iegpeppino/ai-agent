import  os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from function_schemas import schema_get_file_content, schema_run_python_file, schema_write_file, schema_get_files_info

def main ():

    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create instance of ai client using Gemini Api key
    client = genai.Client(api_key= api_key)

    if len(sys.argv) < 1:
        print("Please provide a prompt to execute")
        print("Exiting program")
        exit(1)
   
    user_prompt = sys.argv[1]

    #
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    # Create list of message history
    messages = [
        types.Content(role= "user", parts=[types.Part(text=user_prompt)]),
    ]

    #
    available_functions = types.Tool(
        function_declarations= [
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    # Generate a response object using the ai model
    response = client.models.generate_content(
        model= "gemini-2.0-flash-001",
        contents= messages,
        config= types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )

    if len(response.function_calls) > 0:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            print(f'User prompt: {user_prompt}')
            print(response.text)
            print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
            print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    else:
        print(response.text)

    
if __name__ == "__main__":
    main()