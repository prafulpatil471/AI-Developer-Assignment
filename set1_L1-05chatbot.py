#---------------------Set 1 – L1‑05 Observability & Logging-------------------

import time
from logger import log_interaction   # make sure logger.py exists

def fake_ai_response(prompt: str) -> str:
    return f"Summary of: {prompt[:50]}..."

def count_tokens(text: str) -> int:
    return len(text.split())

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        start = time.time()
        response = fake_ai_response(user_input)
        latency = time.time() - start
        tokens_used = count_tokens(user_input) + count_tokens(response)

        print("Bot:", response)

        log_interaction(user_input, response, latency, tokens_used)

#---how to run --
#--open power shell and type  cd "C:\Users\INDIA\AI Developer Assignment"
#-then go to vs code--- type into You-- How are you?. 
#- chatbot is execute
#--- python set1_L1-05chatbot.py
