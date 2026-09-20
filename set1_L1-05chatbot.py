
import time
from logger import log_interaction   

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


