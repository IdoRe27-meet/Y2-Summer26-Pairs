from app1 import run_chat as run_chat_tal
from app2 import run_chat as run_chat_talia

def choose():
    chosen = input(
        "Please choose between those two agents:\n"
        "1. Tal - a debugger agent\n"
        "2. Talia - a coding agent: \n"
        ""
    )

    if chosen == "1":
        run_chat_tal()
    elif chosen =="2":
        run_chat_talia()
    else: 
        print("please choose a 1 or 2")
        choose()

choose()
