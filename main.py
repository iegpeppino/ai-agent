import  os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt, MAX_ITERATIONS
from call_function import call_function, available_functions

def main ():

    # Load environment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Catch arguments from user input
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]    

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

  
    """
    Our main loop, iterates a sensible number of times
    getting a response from the model using generate_content()
    If the response elements contain function_call, the function is
    called, and its results appended to the messages that are used
    once again in the loop as arguments (continuous conversation between
    user and AI model).
    If there are no function_call it means either the model solved the prompt
    and doesn't need to call anymore functions or that it failed the prompt's task.
    """
    for i in range(MAX_ITERATIONS):
        func_called_flag = False # Flag if any functions are called
        response = generate_content(client, messages, verbose)
        if response.candidates:
            for candidate in response.candidates :
                messages.append(candidate.content) 
                for part in candidate.content.parts:    
                    if part.function_call:
                        func_called_flag = True
                        function_call = part.function_call
                        function_result = call_function(function_call, verbose)
                        messages.append(function_result)
        if func_called_flag:
            continue    
        else:
            print(response.text)
            break


def generate_content(client, messages, verbose):
    
    """
    Returns a response from our client's model using 
    the message history and verbose as arguments
    """
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


    
    return response

if __name__ == "__main__":
    main()

    # old Generate_content() logic

    
    # before handling function_calls inside loop

    # if not response.:
    #     return response.text

    # responses = []
    
    # for function_call_part in response.function_calls:
      
    #     function_call_result = call_function(function_call_part, verbose)
    #     if (
    #         not function_call_result.parts
    #         or not function_call_result.parts[0].function_response
    #     ):
    #         raise Exception("no response was caught from function")
    #     if verbose:
    #         print(f"-> {function_call_result.parts[0].function_response.response}")
    #     messages.append(function_call_result) # Append Type.Content to messages
    #     responses.append(function_call_result.parts[0])
    
    #     if not responses:
    #         raise Exception("no function responses where caught, exiting.")

        
                

