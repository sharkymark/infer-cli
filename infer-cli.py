from google import genai
from groq import Groq
from openai import OpenAI
from huggingface_hub import InferenceClient
import os

def display_results(results):
    print("\nSearch Results:")
    for result in results:
        print(f"- {result}")

def search(router, model, search_criteria):
    if router == 'groq':
        return search_groq(model, search_criteria)
    elif router == 'hugging_face':
        return search_hugging_face(model, search_criteria)
    elif router == 'openrouter':
        return search_openrouter(model, search_criteria)
    elif router == 'google_gemini':
        return search_google_gemini(model, search_criteria)
    else:
        return []

def search_groq(selected_model, search_criteria):
    # Implement the search logic for Groq
    # https://github.com/groq/groq-python
    # https://console.groq.com/docs/quickstart
    # https://console.groq.com/docs/libraries

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": search_criteria,
            }
        ],
        model=selected_model,
    )
    return [chat_completion.choices[0].message.content]


def search_google_gemini(selected_model, search_criteria):
    # Implement the search logic for Google Gemini
    # https://ai.google.dev/gemini-api/docs/quickstart?lang=python

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model=selected_model, contents=search_criteria
    )
    return [response.text]

def search_hugging_face(selected_model, search_criteria):
    # Implement the search logic for Hugging Face
    # https://huggingface.co/docs/huggingface_hub/v0.13.2/en/guides/inference
    # https://huggingface.co/docs/huggingface_hub/guides/inference#legacy-inferenceapi-client
    # https://github.com/huggingface/hfapi
    # https://huggingface.co/docs/huggingface_hub/guides/inference


    api_key = os.getenv("HF_API_KEY")
    if not api_key:
        raise ValueError("Please set the HF_API_KEY environment variable.")

    # Initialize the InferenceApi with the selected model
    inference = InferenceClient(model=selected_model, token=api_key)

    # Send the search criteria (prompt) to the model
    response = inference.text_generation(search_criteria)
    # response = inference.question_answering(question=search_criteria)
    # (inputs=search_criteria)
    # Return the result as a list (consistent with your Groq/Gemini format)
    if isinstance(response, list) and response:  # Some models return a list
        return [response[0].get("generated_text", "No text returned")]
    elif isinstance(response, dict):  # Others return a dict
        return [response.get("generated_text", "No text returned")]
    else:
        return [str(response)]



def search_openrouter(selected_model, search_criteria):
    # Implement the search logic for OpenRouter
    # https://openrouter.ai/docs/quickstart

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENROUTER_API_KEY environment variable.")

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
    )
    try:
        completion = client.chat.completions.create(
            model=selected_model,
            messages=[
                {
                "role": "user",
                "content": search_criteria
                }
            ]
            )
        if not completion or not completion.choices:
            return ["No response from OpenRouter"]
        return [completion.choices[0].message.content]
    except Exception as e:
        return [f"Error: {str(e)}"]


def choose_model(routers):

    if routers == 'google_gemini':
        # https://ai.google.dev/gemini-api/docs/models
        # https://ai.google.dev/gemini-api/docs/models/experimental-models
        print("Choose a model:")
        print("1. Gemini 2.0 Flash")
        print("2. Gemini 2.0 Flash Experimental")
        print("3. Gemini 2.0 Flash Thinking")
        print("4. Gemini 2.0 Pro")

        choice = input("Enter your choice: ")

        if choice == '1':
            return 'gemini-2.0-flash'
        elif choice == '2':
            return 'gemini-2.0-flash-exp'
        elif choice == '3':
            return 'gemini-2.0-flash-thinking-exp-01-21'
        elif choice == '4':
            return 'gemini-2.0-pro-exp'
        else:
            print("Invalid choice. Defaulting to 1.")
            return 'gemini-2.0-flash'
    elif routers == 'groq':
        # https://console.groq.com/docs/models
        print("Choose a model:")
        print("1. Llama 3.3 70b")
        print("2. Llama 3 70b 8192")
        print("3. Deepseek R1")

        choice = input("Enter your choice: ")

        if choice == '1':
            return 'llama-3.3-70b-versatile'
        elif choice == '2':
            return 'llama3-70b-8192'
        elif choice == '3':
            return 'deepseek-r1-distill-llama-70b'
        else:
            print("Invalid choice. Defaulting to 1.")
            return 'llama3-3-70b-versatile'
    elif routers == 'openrouter':
        # https://openrouter.ai/models
        # curl https://openrouter.ai/api/v1/models
        print("Choose a model:")
        print("1. OpenAI: GPT 4o mini")
        print("2. OpenAI: GPT 4o search preview")
        print("3. Anthropic: Claude 3.7 Sonnet")

        choice = input("Enter your choice: ")

        if choice == '1':
            return 'openai/gpt-4o-mini-search-preview'
        elif choice == '2':
            return 'openai/gpt-4o-search-preview'
        elif choice == '3':
            return 'anthropic/claude-3.7-sonnet'
        else:
            print("Invalid choice. Defaulting to 1.")
            return 'openai/gpt-4o-mini-search-preview'
    elif routers == 'hugging_face':
        # https://huggingface.co/models
        print("Choose a model:")
        print("1. Meta Llama 3.2 3B")

        choice = input("Enter your choice: ")

        if choice == '1':
            return 'meta-llama/Llama-3.2-3B-Instruct'
        else:
            print("Invalid choice. Defaulting to 1.")
            return 'meta-llama/Llama-3.2-3B-Instruct'

def main_menu():
    while True:
        print("Choose an AI Router:")
        print("1. Groq")
        print("2. Hugging Face")
        print("3. OpenRouter")
        print("4. Google Gemini")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            router = 'groq'
        elif choice == '2':
            router = 'hugging_face'
        elif choice == '3':
            router = 'openrouter'
        elif choice == '4':
            router = 'google_gemini'
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        model = choose_model(router)
        search_criteria = input("Enter search criteria: ")
        results = search(router, model, search_criteria)
        display_results(results)

        while True:
            print("1. Enter another search for the same router/model")
            print("2. Go back to the main menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                search_criteria = input("Enter search criteria: ")
                results = search(router, model, search_criteria)
                display_results(results)
            elif sub_choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
