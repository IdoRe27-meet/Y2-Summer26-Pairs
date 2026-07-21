import os
from anthropic import Anthropic
from dotenv import load_dotenv
from shared_memory import load_memory, save_memory


def run_chat():
    load_dotenv()
    client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    memory = load_memory()
    print('You: (type exit to quit)')
    system_message =  f'''Your name is Talia khamisy and you are in a gang and a helpful coding assistant. You will answer in a detailed response, helping the user to code new apps and algorithims, im all code languges. You will provide clear explenations to the user. Always answer in a clear way and with a code without any bugs, never answer questions that are not related to coding. do not answer debugg quiestions (say: go to Tal, the other assistant in the site). Every time you are coding, only the code part, put [your code]. don't put anything besides the brackets, and inside them - the code!! not even  Shared memory:
{memory}''' 
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        memory = load_memory()
   

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=2000,
            temperature=0.6,
            system=system_message,
            messages=history
        )
        print(response)
        reply = response.content[0].text
        save_memory({
            "last_user_message": user_input,
            "last_reply": reply
        })
        if '[' in reply and ']' in reply:
            code = reply[reply.find('[')+1:reply.find(']')]
        else:
            code = None
        print(f'Claude: {reply}')
        if code is not None:
            with open("Talia_code.py", "w", encoding="utf-8") as file:
                file.write(code)

        history.append({'role': 'assistant', 'content': reply})


run_chat()