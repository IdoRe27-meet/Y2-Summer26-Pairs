import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = system_message = "Your name is Talia and you are a helpful coding assistant. You will answer in a detailed response, helping the user to code new apps and algorithims, im all code languges. You will provide clear explenations to the user. Always answer in a clear way and with a code without any bugs, never answer questions that are not related to coding. do not answer debugg quiestions (say: go to Tal, the other assistant in the site)."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        print('History:', history)
        response = client.messages.create(
    model='claude-haiku-4-5-20251001',
    max_tokens=300,   # try 50, then 500
    temperature=0.7,  # try 0, then 1
    system=system_message,
    messages=history
)


        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=250,
            temperature=0.6,
            system=system_message,
            messages=history
        )
        print(response)
        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

