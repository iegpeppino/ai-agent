import  os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from call_function import call_function, available_functions

def main ():

    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Catch arguments from user input
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.arg[1:] if not arg.startswith("--")]    

    if not args:
        print("No input prompt was detected")
        print('Usage: python main.py <prompt> [--verbose]')
        print('Ex: python main.py "This program is not printing output')
        sys.exit(1)

    user_prompt = " ".join(args)

    # Create instance of ai client using Gemini Api key
    client = genai.Client(api_key= api_key)

    # Create list of message history
    messages = [
        types.Content(role= "user", parts=[types.Part(text=user_prompt)]),
    ]

    # Calling generate content to call AI model using the prompt and args
    generate_content(client, messages, verbose)



def generate_content(client, messages, verbose):

    # Generate a response object using the ai model
    response = client.models.generate_content(
        model= "gemini-2.0-flash-001",
        contents= messages,
        config= types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )

    if verbose:
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

    if not response.function_calls:
        return response.text
    
    responses = []
    
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("no response was caught from function")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        responses.append(function_call_result.parts[0])

    if not responses:
        raise Exception("no function responses where caught, exiting.")
                

if __name__ == "__main__":
    main()