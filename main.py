import os
from google import genai
from google.genai import types
from pprint import pprint


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return
    client = genai.Client(api_key=api_key)

    # # content streaming part
    # response = client.models.generate_content_stream(
    #     model="gemini-2.0-flash",
    #     config=types.GenerateContentConfig(
    #         system_instruction="You are a cat. Your name is Neko. can can only speak 2 words before you have to say meow",
    #         # thinking_config=types.ThinkingConfig(include_thoughts=True),
    #     ),
    #     contents="Explain how AI works in a 3 paragraphs",
    #     # stream=True,
    # )
    # for chuck in response:
    #     print(chuck.text, end="")

    # chat functionality
    chat = client.chats.create(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a cat. Your name is Neko. can can only speak 2 words before you have to say meow",
        ),
    )

    response = chat.send_message("I have 2 dogs in my house.")
    print(response.text)

    response = chat.send_message("How many paws are in my house?")
    print(response.text)

    for message in chat.get_history():
        print(f"role - {message.role}", end=": ")
        print(message.parts[0].text)


if __name__ == "__main__":
    main()
