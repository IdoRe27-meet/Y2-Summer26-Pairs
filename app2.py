import os
from anthropic import Anthropic
from dotenv import load_dotenv



def run_chat():
    load_dotenv()
    client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    print('You: (type exit to quit)')
    system_message =  "Your name is Talia and you are a helpful coding assistant. You will answer in a detailed response, helping the user to code new apps and algorithims, im all code languges. You will provide clear explenations to the user. Always answer in a clear way and with a code without any bugs, never answer questions that are not related to coding. do not answer debugg quiestions (say: go to Tal, the other assistant in the site). Every time you are coding, only the code part, put [<your code>]. don't put anything besides the brackets, and inside them - the code!! not even ''' ."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        response = client.messages.create(
    model='claude-haiku-4-5-20251001',
    max_tokens=300,  
    temperature=0.7,  
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
        if '[' in reply and ']' in reply:
            code = reply[reply.find('[')+1:reply.find(']')]
        else:
            code = None
        print(f'Claude: {reply}')
        if code is not None:
            with open("script.py", "w", encoding="utf-8") as file:
                file.write(code)

        history.append({'role': 'assistant', 'content': reply})


