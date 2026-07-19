# Importing the necessary libraries
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY')) # setting up the API key for the Anthropic client

def run_chat():

    user_goal = input("Type your goal for this chat: ")    

    print('You: (type exit to quit)')
    system_message = f"Your name is Tal, you are a helful coding debugger, answer brifely and be focus on the bug, it's cause and how to solve it. You start you response with explaining the bug and then you give him possible solutions. Never say something you don't know and present it as true info. Answer only q's about debbuging and code, don't answer other questions. Also, it is important for you to know that the user has a goal for tosy, and you shold hellp him achive that (it it is standing in the instructions erlier): {user_goal}. also, if they ask you a question that is not related to coding actual apps and not debugging, you should say: 'go to Talia' (The other assistant in the site)."
    history = []
    message_num = 1
    while True:
        print("      \n------------------------\n        ")
        user_input = input(f'message #{message_num} >> ')

        if user_input.lower() == 'exit': # Allow the user to exit the chat
            break
        elif user_input.lower() == 'restart': # Allow the user to restart the conversation
            history = []
            print("The history has been cleared. Starting a new conversation.")
            continue
        elif user_input.lower()=='/summary': 
            summary = client.messages.create(
                model='claude-haiku-4-5-20251001',
                max_tokens=300,
                temperature=0.7,
                system=system_message,
                messages=history + [{'role': 'user', 'content': 'Please provide a summary of our conversation so far.'}]
            )
            print(f'Summary: {summary.content[0].text}')
            continue


        history.append({'role': 'user', 'content': user_input})
       
        message_num += 1 # Counting the number of messages in the conversation

        response = client.messages.create(   #API call and setting the parameters for the response
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )
        
        reply = response.content[0].text
        print(f'Assistant: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()


