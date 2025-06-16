import  os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

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

    # Create list of message history
    messages = [
        types.Content(role= "user", parts=[types.Part(text=user_prompt)]),
    ]

    # Generate a response object using the ai model
    response = client.models.generate_content(
        model= "gemini-2.0-flash-001",
        contents= messages,
    )

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