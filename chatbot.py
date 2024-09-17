import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    # Stores message history
    messages = []

    # While loop to keep chatbot running
    while True:
        # User's chat input
        message = input("You: ")

        # Stops chatbot if user inputs "quit" or "goodbye"
        if (message.lower() == "quit" or "goodbye" in message.lower()):
            print("Chatbot terminated.")
            break

        # Appends message to message history
        messages.append({"role": "user", "content": message})

        # Generates response
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = messages
        )

        # Prints response
        chat_message = response['choices'][0]['message']['content']
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})

print("Chatbot initiated! Type 'quit' to end the session.")
chatbot()