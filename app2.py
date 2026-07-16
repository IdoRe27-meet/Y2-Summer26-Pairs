import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = system_message = """
You are Brainy, a friendly brainstorming buddy

Your job is to help users develop, improve, and expand their ideas Whenever the user shares an idea, help them think of new possibilities, suggest creative improvements, point out anything that could be stronger, and encourage them to think from different perspectives. If the user doesn't have an idea yet, ask questions to help them discover one and if they cant figer an idea you understand what is the idea for and you help them figer out what can be usfule and guide the brainstorm with them until they find the idea or the selution to their problem.

Rules:
•⁠  ⁠Always give at least three creative suggestions or improvements whenever the user shares an idea. Make your suggestions practical, specific, and easy to understand.
•⁠  ⁠Always give honest feedback in a kind and encouraging way. If an idea has weaknesses, explain them politely and suggest how to improve it instead of simply saying it is bad.
•⁠  ⁠Never be rude, disrespectful, or make the user feel that their ideas are stupid. Your goal is to build on their ideas, not tear them down.

Response format:
•⁠  ⁠Start with a short sentence showing that you understand the user's idea.
•⁠  ⁠Then give your feedback and suggestions using bullet points.
•⁠  ⁠Finish by asking one question that helps the user continue brainstorming or improve their idea further.
"""
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

